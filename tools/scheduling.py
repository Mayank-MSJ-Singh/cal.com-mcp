import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()


url = "https://api.cal.com/v2/schedules/"
auth = os.getenv("CAL_COM_API_KEY")
cal_api_version = os.getenv("CAL_API_VERSION")

headers = {
        "Authorization": auth,
        "cal-api-version": "2024-06-11"
    }



def cal_get_all_schedules():
    

    response = requests.request("GET", url, headers=headers)
    return response.text


def cal_create_a_schedule(name, timeZone, isDefault, availability=None, overrides=None, ):
    """
    Creates a schedule configuration in a simple way

    Parameters:
    name (str): Schedule name
    time_zone (str): Time zone (e.g., "America/New_York")
    is_default (bool): True if this is the default schedule
    availability (list): Optional, Each object contains days and times when the user is available.
                        If not passed, the default availability is Monday to Friday from 09:00 to 17:00.
                        (each must have days, start_time, end_time + can have some extra random field)
    overrides (list): Optional,  Need to change availability for a specific date?
                    Add an override.(each must have days, start_time, end_time
                    + can have some extra random field)

    Returns:
    dict: Ready-to-use schedule configuration
    """

    payload = {
        "isDefault": isDefault,
        "name": name,
        "timeZone": timeZone,
    }

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

def cal_update_a_schedule(
    schedule_id,
    name=None,
    timeZone=None,
    isDefault=None,
    availability=None,
    overrides=None
):

    """
    Updates a schedule configuration in a simple way.

    Parameters:
    schedule_id (int): The ID of the schedule to update (required)
    name (str): Optional new schedule name
    timeZone (str): Optional new time zone
    isDefault (bool): Optional, set as default schedule
    availability (list as JSON string): Optional, availability blocks
    overrides (list as JSON string): Optional, override blocks

    Returns:
    str: API response text
    """
    if not schedule_id:
        print("Missing required: schedule_id")
        return None
    url_new = url + str(schedule_id)

    payload = {}

    if name is not None:
        payload["name"] = name

    if timeZone is not None:
        payload["timeZone"] = timeZone

    if isDefault is not None:
        payload["isDefault"] = isDefault

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

    response = requests.request("PATCH", url_new, json=payload, headers=headers)

    return response.text

def cal_get_default_schedule():
    url_new = url + "default"
    response = requests.request("GET", url_new, headers=headers)

    return response.text

def cal_get_schedule(schedule_id):
    url_new = url + str(schedule_id)

    response = requests.request("GET", url_new, headers=headers)

    return response.text

def cal_delete_a_schedule(schedule_id):
    url_new = url + str(schedule_id)
    response = requests.request("DELETE", url_new, headers=headers)

    return response.text

if __name__ == "__main__":
    print(cal_get_all_schedules())

    pass
