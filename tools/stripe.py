import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://api.cal.com/v2/stripe"

auth = os.getenv("CAL_COM_API_KEY")

headers = {
        "Authorization": auth,
        "Content-Type": "application/json"
    }

def cal_get_stripe_connect_url():
    url_new = f"{url}/connect"
    response = requests.request("GET", url_new, headers=headers)
    return response.text

def cal_save_stripe_credentials(state : str,code : str):

    url_new = f"{url}/save"

    querystring = {"state": state, "code": code}

    response = requests.request("GET", url_new, headers=headers, params=querystring)
    return response.text

def cal_check_stripe_connection():

    url_new = f"{url}/check"

    response = requests.request("GET", url_new, headers=headers)
    return response.text

if __name__ == '__main__':
    #print(cal_get_stripe_connect_url())
    #cal_save_stripe_credentials(, code)
    #print(cal_check_stripe_connection())
    pass



