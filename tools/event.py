import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()


url = "https://api.cal.com/v2/schedules"
auth = os.getenv("CAL_COM_API_KEY")
cal_api_version = os.getenv("CAL_API_VERSION")


if __name__ == "__main__":
    pass