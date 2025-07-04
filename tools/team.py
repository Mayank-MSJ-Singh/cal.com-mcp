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

def cal_create_a_team(name, slug = None, logoUrl = None, calVideoLogo = None, appLogo = None, appIconLogo = None, bio = None, hideBranding = False, isPrivate = None, hideBookATeamMember = None, metadata = None, theme = None, brandColor = None, darkBrandColor = None, bannerUrl = None, timeFormat = None, timeZone = "Europe/London", weekStart = "Sunday", autoAcceptCreator = True):
    payload = {
        "name": name,
        "hideBranding": hideBranding,
        "timeZone": timeZone,
        "weekStart": weekStart,
        "autoAcceptCreator": autoAcceptCreator,
        "metadata": {}
    }

    # Add optional parameters to payload if they're not None
    if slug is not None:
        payload["slug"] = slug
    if logoUrl is not None:
        payload["logoUrl"] = logoUrl
    if calVideoLogo is not None:
        payload["calVideoLogo"] = calVideoLogo
    if appLogo is not None:
        payload["appLogo"] = appLogo
    if appIconLogo is not None:
        payload["appIconLogo"] = appIconLogo
    if bio is not None:
        payload["bio"] = bio
    if isPrivate is not None:
        payload["isPrivate"] = isPrivate
    if hideBookATeamMember is not None:
        payload["hideBookATeamMember"] = hideBookATeamMember
    if theme is not None:
        payload["theme"] = theme
    if brandColor is not None:
        payload["brandColor"] = brandColor
    if darkBrandColor is not None:
        payload["darkBrandColor"] = darkBrandColor
    if bannerUrl is not None:
        payload["bannerUrl"] = bannerUrl
    if timeFormat is not None:
        payload["timeFormat"] = timeFormat

    # Handle metadata separately (overwrite initial empty dict if provided)
    if metadata is not None:
        payload["metadata"] = metadata


    response = requests.request("POST", url, json=payload, headers=headers)
    return response.text

if __name__ == "__main__":
    #print(cal_get_a_team("75458"))
    #cal_delete_team("75458")
    #print(cal_get_a_team("75458"))
    print(cal_create_a_team(
        name="My Test Team 1",
        bio="This is a test team created via API",
        hideBranding=True,
        isPrivate=True,
        hideBookATeamMember=True,
        metadata={"project": "test", "env": "dev"},
        theme="dark",
        brandColor="#FF5733",
        darkBrandColor="#C70039",
        timeZone="Asia/Kolkata",
        weekStart="Monday",
        autoAcceptCreator=False
    ))

    pass