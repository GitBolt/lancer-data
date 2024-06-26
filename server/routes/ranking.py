from core.db import get_db
from sqlalchemy.orm import Session
from core.schemas import User
from fastapi import APIRouter, Depends, Query
from core.schemas import User, Contribution
from datetime import datetime, timedelta
from sqlalchemy import func, text


router = APIRouter(prefix="/ranking")


@router.get("/top_devs/language")
async def get_top_users_for_language(
    session: Session = Depends(get_db),
    language: str = Query(..., title="Language Name"),
    start_date: str = None,
    till: int = 7,
    limit: int = 5
):
    start = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else datetime.today() - timedelta(days=1)
    end_date = start + timedelta(days=till)

    print(start, end_date)

    data = session.query(Contribution).all()

    for i in data:
        print(i.date)
        
    query = text("""
            SELECT
                u.id,
                u.githubId,
                SUM(
                    CAST(JSON_UNQUOTE(JSON_EXTRACT(c.breakdown, CONCAT('$.', :language, '.additions'))) AS SIGNED) +
                    CAST(JSON_UNQUOTE(JSON_EXTRACT(c.breakdown, CONCAT('$.', :language, '.deletions'))) AS SIGNED)
                ) AS total_changes
            FROM
                `User` u
            JOIN
                `Contribution` c ON u.id = c.user_id
            WHERE
                c.date >= :start_date AND c.date <= :end_date
            GROUP BY
                u.id, u.githubId
            HAVING
                total_changes > 0
            ORDER BY
                total_changes DESC
            LIMIT
                :limit;
    """)

    result = session.execute(query, {"language": language, "start_date": start, "end_date": end_date, "limit": limit})

    data = result.fetchall()
    output_data = [
        {"github_name": name, "rank":rank, "lines_contributed": lines_contributed, "user_id": user_id}
        for rank, (user_id, name, lines_contributed) in enumerate(sorted(data, key=lambda x: x[2], reverse=True), start=1)
    ]
   
    return output_data


@router.get("/top_devs/all_languages")
async def get_top_users_for_language(
    session: Session = Depends(get_db),
    start_date: str = None,
    till: int = 7,
    limit: int = 5
):
    start = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else datetime.today() - timedelta(days=1)
    end_date = start + timedelta(days=till)

    print(start, end_date)

    top_x = (
        session.query(User, func.sum(Contribution.total_lines))
        .join(Contribution)
        .filter(Contribution.date >= start_date, Contribution.date <= end_date)
        .group_by(User)
        .order_by(func.sum(Contribution.total_lines).desc())
        .limit(limit)
        .all()
    )

    result = []
    for user, total_lines in top_x:
        result.append({
            "github_name": user.githubId,
            "lines_contributed": total_lines,
        })

    return result
    

@router.get("/top_devs/commits")
async def get_top_users_for_language(
    session: Session = Depends(get_db),
    start_date: str = None,
    till: int = 7,
    limit: int = 5
):
    start = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else datetime.today() - timedelta(days=1)
    end_date = start + timedelta(days=till)

    print(start, end_date)

    # Step 1: Create a subquery for summing up total_commits for each user within the date range.
    subquery = (
        session.query(Contribution.user_id.label('user_id'), func.sum(Contribution.total_commits).label('sum_commits'))
        .filter(Contribution.date >= start_date, Contribution.date <= end_date)
        .group_by(Contribution.user_id)
        .subquery()
    )

    # Step 2: Join this subquery with the User table and order the results.
    top_x = (
        session.query(User, subquery.c.sum_commits)
        .join(subquery, User.id == subquery.c.user_id)
        .order_by(subquery.c.sum_commits.desc())
        .limit(limit)
        .all()
    )

    result = []
    for user, total_commits in top_x:
        result.append({
            "github_name": user.githubId,
            "total_commits": total_commits,
        })

    return result