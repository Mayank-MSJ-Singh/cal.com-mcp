import requests
import json
from dotenv import load_dotenv
import os
import ast

load_dotenv()

url = "https://api.cal.com/v2/verified-resources"
auth = os.getenv("CAL_COM_API_KEY")

headers = {
        "Authorization": auth,
        "Content-Type": "application/json"
    }

def cal_request_email_verification_Code(email : str):

    url_new = f"{url}/emails/verification-code/request"
    payload = {"email": email}
    response = requests.request("POST", url_new, json=payload, headers=headers)

    return (response.text)

def cal_request_phone_verification_Code(phone : str):

    url_new = f"{url}/phones/verification-code/request"
    payload = {"phone": phone}
    response = requests.request("POST", url_new, json=payload, headers=headers)

    return (response.text)

def cal_verify_email_verification_Code(email : str, code : int):

    url_new = f"{url}/emails/verification-code/verify"
    payload = {"email": email,
               "code": code}
    response = requests.request("POST", url_new, json=payload, headers=headers)

    return (response.text)

def cal_verify_phone_verification_Code(phone : str, code : int):

    url_new = f"{url}/phones/verification-code/request"
    payload = {"phone": phone,
               "code": code}
    response = requests.request("POST", url_new, json=payload, headers=headers)

    return (response.text)

def cal_get_list_of_verified_emails(take : int = None, skip : int = None):
    url_new = f"{url}/emails"

    querystring = {}
    if take is not None:
        querystring["take"] = take
    if skip is not None:
        querystring["skip"] = skip

    response = requests.request("GET", url_new, headers=headers, params=querystring)

    return (response.text)

def cal_get_list_of_verified_phones(take : int = None, skip : int = None):
    url_new = f"{url}/phones"

    querystring = {}
    if take is not None:
        querystring["take"] = take
    if skip is not None:
        querystring["skip"] = skip

    response = requests.request("GET", url_new, headers=headers, params=querystring)

    return (response.text)

if __name__ == "__main__":
    #print(cal_request_email_verification_Code("mayanksingh8713491@gmail.com"))
    #print(cal_request_phone_verification_Code("+919318338221"))
    #print(cal_verify_email_verification_Code("mayanksingh8713491@gmail.com", '039528'))
    #print(cal_verify_phone_verification_Code("+919318338221",""))
    #print(cal_get_list_of_verified_phones())
    pass