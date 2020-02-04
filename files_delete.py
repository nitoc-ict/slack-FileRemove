import requests
import os
import channel_list


def delete_files_list(files):
    url = "https://slack.com/api/files.delete"
    for file in files:
        slack_res = requests.get(
            url, params={"token": os.environ["SLACK_TOKEN"], "file": file}).json()
    if slack_res["ok"]:
        print("delete files")
