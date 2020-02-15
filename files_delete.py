import requests
import os
import channel_list


def delete(file):
    url = "https://slack.com/api/files.delete"
    slack_res = requests.get(
        url, params={"token": os.environ["SLACK_TOKEN"], "file": file}).json()
    if slack_res["ok"]:
        print("delete files")
    else:
        print("failed")
