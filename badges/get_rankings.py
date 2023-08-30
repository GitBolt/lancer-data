from sqlalchemy import func, text
from db import *
from schemas import User, Contribution
from datetime import datetime, timedelta

titles = ["First", "Second", "Third", "Top 5", "Top 10"]


def get_top_users_by_commit():
    start = datetime.today().date() - timedelta(days=7)
    end_date = start + timedelta(days=7)

    date_range = f"{start.day} {start.strftime('%B')} - {end_date.day} {end_date.strftime('%B')}, {start.year}"

    ses = SessionLocal()

    top_x = (
        ses.query(User, func.sum(Contribution.total_commits))
        .join(Contribution)
        .filter(Contribution.date >= start, Contribution.date <= end_date)
        .group_by(User)
        .order_by(func.sum(Contribution.total_commits).desc())
        .limit(5)
        .all()
    )

    result = []
    for user, total_commits in top_x:
        result.append({
            "github_name": user.githubId,
            "id": user.id,
            "total_commits": total_commits,
        })

    return {"devs": result, "week": date_range}


def get_top_devs_by_lang(language) -> list[User]:
    start = datetime.today().date() - timedelta(days=7)
    end_date = start + timedelta(days=7)

    date_range = f"{start.day} {start.strftime('%B')} - {end_date.day} {end_date.strftime('%B')}, {start.year}"

    ses = SessionLocal()
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
            c.date BETWEEN :start_date AND :end_date
        GROUP BY
            u.id, u.githubId
        HAVING
            total_changes > 0
        ORDER BY
            total_changes DESC
        LIMIT
            :limit;
    """)

    query_result = ses.execute(query, {"language": language, "start_date": start, "end_date": end_date, "limit": 10})
    top_x = query_result.fetchall()
    result = []
    for details in top_x:
        result.append({
            "github_name": details[1],
            "id": details[0],
            "total_commits": int(details[2]),
        })

    return {"devs": result, "week": date_range}

