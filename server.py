import json
import logging
import os
import requests


import requests

url = "https://api.cal.com/v2/schedules"

headers = {
    "Authorization": "cal_live_4744916169233664ad19a298a3882637",
    "cal-api-version": "2024-06-11"
}

response = requests.request("GET", url, headers=headers)

print(response.text)