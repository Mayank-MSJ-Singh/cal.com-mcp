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

def cal_create_a_team(
    name: str,
    slug: str = None,
    logoUrl: str = None,
    calVideoLogo: str = None,
    appLogo: str = None,
    appIconLogo: str = None,
    bio: str = None,
    hideBranding: bool = False,
    isPrivate: bool = None,
    hideBookATeamMember: bool = None,
    metadata: dict = None,
    theme: str = None,
    brandColor: str = None,
    darkBrandColor: str = None,
    bannerUrl: str = None,
    timeFormat: int = None,
    timeZone: str = "Europe/London",
    weekStart: str = "Sunday",
    autoAcceptCreator: bool = True
):


    # Initialize payload with required fields and defaults
    payload = {
        "name": name,
        "hideBranding": hideBranding,
        "timeZone": timeZone,
        "weekStart": weekStart,
        "autoAcceptCreator": autoAcceptCreator,
        "metadata": metadata or {}  # Use provided metadata or empty dict
    }

    # Optional parameters with conditional addition
    optional_params = {
        "slug": slug,
        "logoUrl": logoUrl,
        "calVideoLogo": calVideoLogo,
        "appLogo": appLogo,
        "appIconLogo": appIconLogo,
        "bio": bio,
        "isPrivate": isPrivate,
        "hideBookATeamMember": hideBookATeamMember,
        "theme": theme,
        "brandColor": brandColor,
        "darkBrandColor": darkBrandColor,
        "bannerUrl": bannerUrl,
        "timeFormat": timeFormat
    }

    # Add provided optional parameters to payload
    for key, value in optional_params.items():
        if value is not None:
            payload[key] = value


    response = requests.request("POST", url, json=payload, headers=headers)
    return response.text


def update_team(
        teamId: int,
        name: str = None,
        slug: str = None,
        logoUrl: str = None,
        calVideoLogo: str = None,
        appLogo: str = None,
        appIconLogo: str = None,
        bio: str = None,
        hideBranding: bool = None,
        isPrivate: bool = None,
        hideBookATeamMember: bool = None,
        metadata: dict = None,
        theme: str = None,
        brandColor: str = None,
        darkBrandColor: str = None,
        bannerUrl: str = None,
        timeFormat: int = None,
        timeZone: str = None,
        weekStart: str = None,
        bookingLimits: str = None,
        includeManagedEventsInLimits: bool = None
):
    url_new = url + str(teamId)

    # Start with empty payload
    payload = {}

    # Map all possible parameters
    optional_params = {
        "name": name,
        "slug": slug,
        "logoUrl": logoUrl,
        "calVideoLogo": calVideoLogo,
        "appLogo": appLogo,
        "appIconLogo": appIconLogo,
        "bio": bio,
        "hideBranding": hideBranding,
        "isPrivate": isPrivate,
        "hideBookATeamMember": hideBookATeamMember,
        "metadata": metadata,
        "theme": theme,
        "brandColor": brandColor,
        "darkBrandColor": darkBrandColor,
        "bannerUrl": bannerUrl,
        "timeFormat": timeFormat,
        "timeZone": timeZone,
        "weekStart": weekStart,
        "bookingLimits": bookingLimits,
        "includeManagedEventsInLimits": includeManagedEventsInLimits
    }

    # Add only provided parameters to payload
    for key, value in optional_params.items():
        if value is not None:
            payload[key] = value

    response = requests.request("PATCH", url_new, json=payload, headers=headers)
    return response.text

if __name__ == "__main__":
    #print(cal_get_a_team("75458"))
    #cal_delete_team("75458")
    #print(cal_get_a_team("75458"))
    print(cal_get_teams())
    '''
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
    '''
    pass