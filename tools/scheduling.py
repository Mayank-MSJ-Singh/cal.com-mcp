import requests

url = "https://api.cal.com/v2/schedules"
auth = ''

def cal_get_all_schedules():
    headers = {
        "Authorization": auth,
        "cal-api-version": "2024-06-11"
    }

    response = requests.request("GET", url, headers=headers)
    return(response.text)

if __name__ == "__main__":
    print(cal_get_all_schedules())