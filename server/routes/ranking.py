import os
from typing import Union
from core.db import get_db
from sqlalchemy.orm import Session
from core.schemas import User
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, Query
from fastapi import Request, HTTPException
from core.schemas import User, Contribution
from datetime import datetime, timedelta
from sqlalchemy import func, or_, desc, cast, Integer, String, select, text
from typing import List


router = APIRouter(prefix="/ranking")

@router.get("/commits")
def get_top_users(
    session: Session = Depends(get_db),
    start_date: str = None,
    till: int = 7,
    limit: int = 5 ,
):

    start_date = datetime.strptime(start_date, "%Y-%m-%d") if start_date else datetime.today() - timedelta(days=1)
    end_date = start_date + timedelta(days=till)

    top_users = (
        session.query(User)
        .join(Contribution, User.id == Contribution.user_id)
        .filter(Contribution.date >= start_date, Contribution.date < end_date)
        .group_by(User.id)
        .order_by(func.sum(Contribution.total_commits).desc())
        .limit(limit)
        .all()
    )

    return top_users


@router.get("/top_users")
async def get_top_users_for_language(
    session: Session = Depends(get_db),
    language: str = Query(..., title="Language Name"),
    start_date: str = None,
    till: int = 7,
    limit: int = 5
):
    start_date = datetime.strptime(start_date, "%Y-%m-%d") if start_date else datetime.today() - timedelta(days=1)
    end_date = start_date + timedelta(days=till)

    query = text("""
        SELECT u.id, u.github_name, SUM((c.breakdown->:language->>'additions')::integer) AS total_additions
        FROM "user" u
        JOIN "contribution" c ON u.id = c.user_id
        WHERE c.date >= :start_date AND c.date <= :end_date
        GROUP BY u.id, u.github_name
        HAVING SUM((c.breakdown->:language->>'additions')::integer) > 0
        ORDER BY total_additions DESC
        LIMIT :limit;
    """)

    result = session.execute(query, {"language": language, "start_date": start_date, "end_date": end_date, "limit": limit})

    data = result.fetchall()
    output_data = [
        {"name": name, "rank": rank, "lines_added": lines_added, "user_id": user_id}
        for rank, (user_id, name, lines_added) in enumerate(sorted(data, key=lambda x: x[2], reverse=True), start=1)
    ]
   
    return output_data