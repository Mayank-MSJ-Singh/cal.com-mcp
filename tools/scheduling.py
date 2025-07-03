import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()


url = "https://api.cal.com/v2/schedules"
auth = os.getenv("CAL_COM_API_KEY")
cal_api_version = os.getenv("CAL_API_VERSION")



def cal_get_all_schedules():
    headers = {
        "Authorization": auth,
        "cal-api-version": cal_api_version
    }

    response = requests.request("GET", url, headers=headers)
    return(response.text)


def cal_create_a_schedule(name, timeZone, isDefault, availability=None, overrides=None, **extra_fields):
    payload = {
        "isDefault": isDefault,
        "name": name,
        "timeZone": timeZone,
    }
    # Merge in any extra fields
    payload.update(extra_fields)

    if availability:
        try:
            payload["availability"] = json.loads(availability)
        except json.JSONDecodeError:
            print("Invalid JSON in availability")
            return None

    if overrides:
        try:
            payload["overrides"] = json.loads(overrides)
        except json.JSONDecodeError:
            print("Invalid JSON in overrides")
            return None

    headers = {
        "Authorization": auth,
        "cal-api-version": cal_api_version,
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.text

def cal_get_default_schedule():
    url_new = url + "default"
    headers = {
        "Authorization": auth,
        "cal-api-version": cal_api_version
    }

    response = requests.request("GET", url_new, headers=headers)

    return (response.text)



if __name__ == "__main__":
    #print(cal_get_all_schedules())

    pass
