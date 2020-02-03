import requests
import os
import json

def get_channel_list():
    url = "https://slack.com/api/channels.list"
    slack_res = requests.get(url, params = {"token": os.environ["SLACK_TOKEN"]}).json()

    if slack_res["ok"]:
        channel_id = [i.get("id") for i in slack_res["channels"]]
        return channel_id
    else:
        return -1
