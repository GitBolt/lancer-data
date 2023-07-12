import json
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

github_key = os.getenv("GH_KEY1")
github_key2 = os.getenv("GH_KEY2")

headers = {"Authorization": f"token {github_key}"}

with open('data.json') as json_file:
    json_data = json.load(json_file)

print(len(json_data), "Devs")

data = {}

# Get today's date in UTC
today = datetime.utcnow().date() - timedelta(days=2)

for user in json_data:
    github_name = user["github_name"]
    gh_name = user["contact_info"]["name"]
    contact_info = user["contact_info"]
    
    # Load existing daily count data
    with open('daily_count.json') as daily_count_file:
        daily_count_data = json.load(daily_count_file)

    daily_count = daily_count_data.get(github_name, {}).get("daily_count", {})
    url = f'https://api.github.com/users/{github_name}/events'
    response = requests.get(url, headers=headers)
    events = response.json()
    commit_count = 0

    for event in events:
        created_date = event["created_at"].split("T")[0]
        event_date = datetime.fromisoformat(created_date).date()
        print(event_date, today)
        if event["type"] == "PushEvent" and event_date == today:
            print(event)
            commit_count += len([e for e in event["payload"]["commits"] if e["author"]["name"] == gh_name])

    # # Update the daily count for today
    # daily_count[str(today)] = commit_count

    # data[github_name] = {
    #     "contact_info": contact_info,
    #     "daily_count": daily_count,
    #     "total_commits": user["total_commits"]
    # }

    # with open('daily_count.json', 'w') as json_file:
    #     json.dump(data, json_file, indent=4)
    
    break
