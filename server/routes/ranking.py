import os
from typing import Union
from core.db import get_db
from sqlalchemy.orm import Session
from core.schemas import User
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends
from fastapi import Request
from core.schemas import User, Contribution
from datetime import datetime, timedelta
from sqlalchemy import func, or_
from typing import List


router = APIRouter(prefix="/ranking")

@router.get("/commits")
def get_top_users(
    session: Session = Depends(get_db),
    start_date: str = None,
    till: int = 1,
    limit: str = None ,
):

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
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

@router.get("/lines_of_code")
def get_top_users(
    session: Session = Depends(get_db),
    start_date: str = None,
    till: int = 1,
    limit: int = 5 ,
    languages: str = None,
):

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = start_date + timedelta(days=till)

    users = session.query(User).all()
    top_users = []
    for user in users:
        lines = 0
        for contribution in user.contributions:
            lines += contribution.Typescript + contribution.Javascript + contribution.Rust + contribution.Python + contribution.C + contribution.CSS + contribution.HTML + contribution.Golang + contribution.Solidity + contribution.CPP
        top_users.append((lines, user))
        
    top_users.sort(key=lambda x: x[0], reverse=True)
    return top_users[:limit]
