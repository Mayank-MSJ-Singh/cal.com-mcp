import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()


url = "https://api.cal.com/v2/teams/"
auth = os.getenv("CAL_COM_API_KEY")

headers = {
        "Authorization": auth,
    }

def cal_get_teams():
    response = requests.request("GET", url, headers=headers)

    return (response.text)

def cal_get_a_team(team_id):
    url_new = url + str(team_id)
    response = requests.request("GET", url_new, headers=headers)
    return (response.text)

def cal_delete_team(team_id):
    url_new = url + str(team_id)
    response = requests.request("DELETE", url_new, headers=headers)
    return (response.text)


if __name__ == "__main__":
    print(cal_get_a_team("72741"))
    pass