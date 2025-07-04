import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()


url = "https://api.cal.com/v2/event-types/"
auth = os.getenv("CAL_COM_API_KEY")
cal_api_version = "2024-06-14"

headers = {
        "Authorization": auth,
        "cal-api-version": cal_api_version
    }


#There is a problem with get_all_event_types right Now!!!
def get_all_event_types():

    response = requests.request("GET", url, headers=headers)
    print(response.text)

def cal_get_event_type(eventTypeId):
    url_new = url + str(eventTypeId)
    response = requests.request("GET", url_new, headers=headers)

    return response.text

def cal_delete_event_type(eventTypeId):
    url_new = url + str(eventTypeId)
    response = requests.request("DELETE", url_new, headers=headers)
    return response.text


def cal_create_event_type(lengthInMinutes, title, slug):
        payload = {
            "bookingLimitsCount": {},
            "lengthInMinutes": lengthInMinutes,
            "title": title,
            "slug": slug,
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)

if __name__ == "__main__":
    #print(cal_get_event_type('2779104'))
    #print(cal_delete_event_type('2779104'))
    print(cal_get_event_type('2785245'))
    #get_all_event_types()
    #cal_create_event_type(15, 'wefw','232') #2785245
    pass