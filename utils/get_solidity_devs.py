import requests
import json
import os


github_key = os.getenv("GH_KEY1")
github_key2 = os.getenv("GH_KEY2")

headers = {"Authorization": f"token {github_key}"}

base_url = "https://api.github.com/search/users"
query_params = {
    "q": "followers:>2 repos:>1 language:Solidity type:user",
    "per_page": 100,
    "page": 1
}


user_data_list = []

response = requests.get(base_url, params=query_params)
total_count = response.json()["total_count"]
print("Total Users:", total_count)

total_pages = (total_count + 9) // 10

for page in range(11, total_pages + 1):
    query_params["page"] = page


    response = requests.get(base_url, params=query_params, headers=headers)
    print(response.text)
    users = response.json()["items"]
    print(len(users))
    for user in users:
        github_name = user["login"]
        user_url = f"https://api.github.com/users/{github_name}"
        user_response = requests.get(user_url, headers=headers)

        user_info = user_response.json()

   
        contact_info = {
            "website": user_info.get("blog"),
            "twitter": user_info.get("twitter_username"),
            "email": user_info.get("email"),
            "name": user_info.get("name"),
            "location": user_info.get("location")
        }
        
        user_data = {
            "github_name": github_name,
            "contact_info": contact_info
        }
        
        user_data_list.append(user_data)

    with open("github_users.json", "w") as json_file:
        json.dump(user_data_list, json_file, indent=4)

    print(f"Processed page {page}/{total_pages}")

print("User data saved to 'github_users.json'")
