import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()


url = "https://api.cal.com/v2/event-types/"
auth = os.getenv("CAL_COM_API_KEY")
cal_api_version = os.getenv("CAL_API_VERSION")

headers = {
        "Authorization": auth,
        "cal-api-version": cal_api_version
    }

def cal_get_event_type(eventTypeId):
    url_new = url + eventTypeId
    response = requests.request("GET", url_new, headers=headers)

    return response.text

def cal_delete_event_type(eventTypeId):
    url_new = url + eventTypeId
    response = requests.request("DELETE", url_new, headers=headers)
    return response.text

if __name__ == "__main__":
    #print(cal_get_event_type('2779104'))
    #print(cal_delete_event_type('2779104'))
    #print(cal_get_event_type('2779104'))
    pass