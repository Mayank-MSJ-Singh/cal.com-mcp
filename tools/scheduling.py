import requests

url = "https://api.cal.com/v2/schedules"
auth = 'cal_live_4744916169233664ad19a298a3882637'

def cal_get_all_schedules():
    headers = {
        "Authorization": auth,
        "cal-api-version": "2024-06-11"
    }

    response = requests.request("GET", url, headers=headers)
    return(response.text)
def cal_create_a_schedule(name, timeZone, isDefault):
    payload = {
        "isDefault": isDefault,
        "name": name,
        "timeZone": timeZone,
        "availability": [
            {
                "days": ["Monday", "Tuesday"],
                "startTime": "17:00",
                "endTime": "19:00"
            },
            {
                "days": ["Wednesday", "Thursday"],
                "startTime": "16:00",
                "endTime": "20:00"
            }
        ],
        "overrides": [
            {
                "date": "2024-05-20",
                "startTime": "18:00",
                "endTime": "21:00"
            }
        ]
    }

    headers = {
        "Authorization": "<authorization>",
        "cal-api-version": "<cal-api-version>",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.text

if __name__ == "__main__":
    print(cal_get_all_schedules())