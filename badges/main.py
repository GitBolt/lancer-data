from db import *
from create_nft import createNFT
from get_rankings import get_top_devs_by_lang, get_top_users_by_commit
import schedule
from datetime import datetime
import time


languages = ['typescript', 'javascript', 'css', 'html', 'python', 'ruby', 'golang', 'java', 'rust', 'solidity', 'csharp', 'c', 'cpp', 'json']
titles = ["First", "Second", "Third", "Top 5", "Top 10"]


def assign_language_badges():
    print("Getting Badges for Language Rankings...")
    for language in languages:
        print("Language:", language)

        top_devs = get_top_devs_by_lang(language)
        devs = top_devs["devs"]
        week = top_devs["week"]

        for idx, dev in enumerate(devs):
            title_idx = min(idx, 4)
            title = titles[title_idx]
            print("Dev:", dev["github_name"])

            res = createNFT(dev, title, "Contributions", week, language)
            print(res, "\n")

def assign_commit_badges():
    top_devs = get_top_users_by_commit()
    devs = top_devs["devs"]
    week = top_devs["week"]

    for idx, dev in enumerate(devs):
        title_idx = min(idx, 4)
        title = titles[title_idx]
        res = createNFT(dev, title, "Commits", week, None)
        print(res, "\n")


def main():
    assign_language_badges()
    print("Language Ranking Done. Doing for commit ranking...")
    assign_commit_badges()

schedule.every().day.at("12:00").do(main)
print("Script Started. Server Time: ", datetime.utcnow())
while True:
    schedule.run_pending()
    time.sleep(1)

