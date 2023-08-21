import json
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from get_language_info import get_language_breakdown
from utils import combine_dictionaries
from core.schemas import Contribution, User
import sqlalchemy as sa

load_dotenv()


engine = sa.create_engine(os.environ["DB_URL"])
session = sa.orm.Session(engine)


github_key = os.getenv("GH_KEY1")
github_key2 = os.getenv("GH_KEY2")

headers = {"Authorization": f"token {github_key}"}

with open('new_data.json') as json_file:
    json_data = json.load(json_file)

print("Devs Count: ", len(json_data))

data = {}

# Get today's date in UTC

today = datetime.utcnow().date()

for idx, user in enumerate(json_data):
    github_name = user["github_name"]

    print(f"Fetching for {github_name} [{idx}/{len(json_data)}]")
    contact_info = user["contact_info"]
    try:
        del contact_info["website"]
    except:
        pass
    # del contact_info["location"]

    try:
        url = f'https://api.github.com/users/{github_name}/events'
        response = requests.get(url, headers=headers)
        print(response)
        events = response.json()

        today_commit_count = 0
        
        language_details = {}

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

        user = session.query(User).filter_by(githubId=github_name).first()
        if user is None:
            print("Adding User")
            user = User(
                githubId=github_name,
                **contact_info
                )  
            session.add(user)
            session.flush()

        if language_details != {}:
            contribution = Contribution(
                user_id = user.id,
                total_commits=today_commit_count, 
                breakdown=language_details, 
                total_lines=sum((language_data.get("additions", 0) + language_data.get("deletions", 0)) for language_data in language_details.values()),
                date=today,
                )

            session.add(contribution)
        res = session.commit()
    except Exception as e:
        print(e)
        continue