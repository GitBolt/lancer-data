import json
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from get_language_info import get_language_breakdown
from utils import combine_dictionaries


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
    
    # Load existing daily count data
    with open('daily_count.json') as daily_count_file:
        daily_count_data = json.load(daily_count_file)

    daily_count = daily_count_data.get(github_name, {}).get("daily_count", {})
    existing_contribs = daily_count_data.get(github_name, {}).get("contributions", [])

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
    
    # Update the daily count for today
    daily_count[str(today)] = today_commit_count
    print("Lang Details: ", language_details, "\n")
    if existing_contribs:
        new_contributions = existing_contribs.append(language_details)
    else:
        new_contributions = [language_details]
    data[github_name] = {
        "contact_info": contact_info,
        "daily_count": daily_count,
        "total_commits": user["total_commits"],
        "contributions": new_contributions
    }

    with open('daily_count.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
