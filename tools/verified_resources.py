import requests
import json
from dotenv import load_dotenv
import os
import ast

load_dotenv()

url = "https://api.cal.com/v2/verified-resources/emails/verification-code"
auth = os.getenv("CAL_COM_API_KEY")

headers = {
        "Authorization": auth,
        "Content-Type": "application/json"
    }