import requests
import os
import json

def get_files_list():
    url = "https://slack.com/api/files.list"
    slack_res = requests.get(url, params = {"token": os.environ["SLACK_TOKEN"]}).json()
    if slack_res["ok"]:
        channel_id = [i.get("timestamp") for i in slack_res["files"]]
        return channel_id
    else:
        return -1