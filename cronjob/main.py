import json
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from get_language_info import get_language_breakdown
from utils import combine_dictionaries
from schemas import Contribution, User
import sqlalchemy as sa
import schedule
import time
from dotenv import load_dotenv


load_dotenv()


engine = sa.create_engine(os.environ["DB_URL"])
session = sa.orm.Session(engine)


github_key = os.getenv("GH_KEY1")
github_key2 = os.getenv("GH_KEY2")

headers = {"Authorization": f"token {github_key}"}
headers2 = {"Authorization": f"token {github_key2}"}

def main():
    switched_key = False

    with open('solana_devs.json') as json_file:
        json_data = json.load(json_file)
    
    with open('temp.json') as json_file:
        temp_data = json.load(json_file)

    for idx, user in enumerate(json_data):
        github_name = user["github_name"]
        contact_info = user["contact_info"]
        print("\nDev: ", github_name, f"Count: [{idx}]/{len(json_data)}")

        url = f'https://api.github.com/users/{github_name}/events?per_page=10'
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            switched_key = True
            print(response.text)
            print("[WARNING] Got rate limited, using new API key now")
            response = requests.get(url, headers=headers2)
            if response.status_code != 200:
                print(response.text)
                print("[ERROR] Rate limited with second API key, taking an hour break")
                time.sleep(3600)
                switched_key = False
                print("[UPDATE]: Back alive, continuing script...")
                continue
        else:
            switched_key = False
        
        events = response.json()
        

        push_events = [e for e in events if e["type"] == "PushEvent"]
        # print("Push Event Count: ", len(push_events))

        for idx, event in enumerate(push_events):
            created_date = event["created_at"].split("T")[0]
            today = datetime.now().date()
            if (created_date != today):
                continue
        
            if created_date not in temp_data:
                temp_data[created_date] = []

            lang_breakdown = {}
            commit_count = 0
            
            for commit in event["payload"]["commits"]:
                commit_res = requests.get(commit["url"], headers=headers2 if switched_key else headers)
                commit_info = commit_res.json()
                lang_data = get_language_breakdown(commit_info)
                
                if not lang_breakdown:
                    lang_breakdown = lang_data
                else:
                    lang_breakdown = combine_dictionaries(lang_breakdown, lang_data)
            
                commit_count += 1

            if any(x["githubId"] == github_name for x in temp_data[created_date]):
                for entry in temp_data[created_date]:
                    if entry["githubId"] == github_name:
                        entry["language_details"] = combine_dictionaries(lang_breakdown, entry["language_details"])
                        entry["commit_count"] += commit_count
                        print("Updated existing user with new data")
                        break

            else:
                temp_data[created_date].append({
                    'githubId': github_name,
                    'contact_info': contact_info,
                    'language_details': lang_breakdown,
                    'commit_count': commit_count
                }) 
            print(f"Finished event fetching: [{idx + 1}/{len(push_events)}]")

            print("Saving temp data")    
            with open('temp.json', 'w') as temp_file:
                json.dump(temp_data, temp_file, indent=4)


    with open('temp.json') as temp_file:
        sorted_data = json.load(temp_file)

    for idx, (date_str, contributions) in enumerate(sorted_data.items()):
        print(f"Adding: [{idx}/{len(sorted_data.items())}]")
        date = datetime.fromisoformat(date_str).date()
        print(f"Date: [{date}]")

        for contrib in contributions:
            githubId = contrib['githubId']
            print("Github Username: ", githubId)
            if (len(githubId) > 24):
                print("Actually skipped long GitHub ID")
                continue

            if (contrib["contact_info"].get("location")):
                del contrib['contact_info']['location']

            user = session.query(User).filter_by(githubId=githubId).first()
            if user is None:
                user = User(githubId=githubId, **contrib['contact_info'])
                session.add(user)
                session.flush()
                print("Added new user")

            print("Adding contribution...\n")
            contribution = Contribution(
                user_id=user.id,
                total_commits=contrib['commit_count'],
                breakdown=contrib['language_details'],
                total_lines=sum(
                    (language_data.get("additions", 0) + language_data.get("deletions", 0))
                    for language_data in contrib['language_details'].values()
                ),
                date=date
            )
            session.add(contribution)
        
            session.commit()



schedule.every().day.at("21:00", "Asia/Kolkata").do(main)
while True:
    schedule.run_pending()