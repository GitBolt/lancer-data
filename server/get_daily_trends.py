import json
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from get_language_info import get_language_breakdown
from utils import combine_dictionaries
from core.schemas import Contribution, User
import sqlalchemy as sa

engine = sa.create_engine("mysql+mysqlconnector://bolt:bolt@localhost:3306/lancer")
session = sa.orm.Session(engine)

load_dotenv()

github_key = os.getenv("GH_KEY1")
github_key2 = os.getenv("GH_KEY2")

headers = {"Authorization": f"token {github_key}"}

with open('data.json') as json_file:
    json_data = json.load(json_file)

print("Devs Count: ", len(json_data))

data = {}

# Get today's date in UTC
today = datetime.utcnow().date() - timedelta(days=2)

for idx, user in enumerate(json_data):
    github_name = user["github_name"]

    print(f"Fetching for {github_name} [{idx}/{len(json_data)}]")
    gh_name = user["contact_info"]["name"]
    contact_info = user["contact_info"]


    url = f'https://api.github.com/users/{github_name}/events'
    response = requests.get(url, headers=headers)
    events = response.json()

    today_commit_count = 0
    language_details = {"date": today.strftime("%Y-%m-%d")}

    # All the times user enter git push. A single push can have multiple commits (oof)
    for event in [e for e in events if e["type"] == "PushEvent"]:
        created_date = event["created_at"].split("T")[0] # Push date, not commit date
        event_date = datetime.fromisoformat(created_date).date()

        if event_date == today: # Pushes for only today
            
            for commit in event["payload"]["commits"]:
                commit_res = requests.get(commit["url"], headers=headers)
                commit_info = commit_res.json()
                lang_breakdown = get_language_breakdown(commit_info)
                if not language_details:
                    language_details = lang_breakdown
                else:
                    language_details = combine_dictionaries(language_details, lang_breakdown)
                today_commit_count += 1
            
    print("Lang Details: ", language_details, "\n")

    user = session.query(User).filter_by(github_name=github_name).first()


    language_details_simple = {}
    for language, contributions in language_details.items():
        if language == "date": continue
        additions = contributions["additions"]
        deletions = contributions["deletions"]
        language_details_simple[language] = additions + deletions

    if user is not None:
        contribution = Contribution(date=today, total_commits=today_commit_count, **language_details_simple)
        contribution.user = user
        session.add(contribution)
        session.commit()
    else:
        user = User(
            github_name=github_name,
            **contact_info
            )
        contribution = Contribution(date=today, **language_details_simple)
        user.contributions.append(contribution)
        session.add(user)
        session.commit()
    
