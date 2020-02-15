import requests
import os
import json


def get_files_list():
    url = "https://slack.com/api/files.list"
    files = []
    count = 1000
    slack_res = requests.get(url, params = {"token": os.environ["SLACK_TOKEN"], "count" : count}).json()
    if slack_res["ok"]:
        timestamp = [file.get("timestamp") for file in slack_res["files"]]
        file_id = [file.get("id") for file in slack_res["files"]]
        for i in range(len(slack_res["files"])):
            files.append({"timestamp": timestamp[i], "file_id": file_id[i]})
        return files
    else:
        return -1
