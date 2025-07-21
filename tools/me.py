import requests
import json
from dotenv import load_dotenv
import os
import ast

load_dotenv()

url = "https://api.cal.com/v2/me"
auth = os.getenv("CAL_COM_API_KEY")

headers = {
        "Authorization": auth,
        "Content-Type": "application/json"
    }





def cal_get_me():
    response = requests.request("GET", url, headers=headers)
    return response.text


def cal_update_my_profile(
        # Optional parameters (all can be None)
        email: str = None,
        name: str = None,
        timeFormat: int = None,
        defaultScheduleId: int = None,
        weekStart: str = None,
        timeZone: str = None,
        locale: str = None,
        avatarUrl: str = None,
        bio: str = None,
        metadata: dict = None,
):
    """
    Updates the authenticated user's profile

    Args:
        email: New email address
        name: Full name
        timeFormat: 12 or 24 (must be either 12 or 24 if provided)
        defaultScheduleId: ID of default schedule
        weekStart: Day of week ("Sunday", "Monday", etc.)
        timeZone: IANA timezone (e.g., "America/New_York")
        locale: Locale code (e.g., "en", "fr")
        avatarUrl: URL to avatar image
        bio: Biography text
        metadata: Custom metadata (max 50 keys, keys ≤40 chars, values ≤500 chars)

    Returns:
        API response text
    """
    # Initialize payload
    payload = {}

    # Validate and add parameters
    if email is not None:
        payload["email"] = (email)
    if name is not None:
        payload["name"] = (name)
    if timeFormat is not None:
        if (timeFormat) not in (12, 24):
            raise ValueError("timeFormat must be either 12 or 24")
        payload["timeFormat"] = (timeFormat)
    if defaultScheduleId is not None:
        payload["defaultScheduleId"] = (defaultScheduleId)
    if weekStart is not None:
        payload["weekStart"] = (weekStart)
    if timeZone is not None:
        payload["timeZone"] = (timeZone)
    if locale is not None:
        payload["locale"] = (locale)
    if avatarUrl is not None:
        payload["avatarUrl"] = (avatarUrl)
    if bio is not None:
        payload["bio"] = (bio)
    if metadata is not None:
        # Validate metadata constraints
        if len(metadata) > 50:
            raise ValueError("Metadata can have at most 50 keys")
        for key, value in metadata.items():
            if len(key) > 40:
                raise ValueError(f"Metadata key '{key}' exceeds 40 character limit")
            if isinstance(value, str) and len(value) > 500:
                raise ValueError(f"Metadata value for '{key}' exceeds 500 character limit")
        payload["metadata"] = (metadata)

    # Check if any parameters were provided
    if not payload:
        raise ValueError("At least one update parameter must be provided")

    response = requests.request("PATCH", url, json=payload, headers=headers)
    return response.text

if __name__ == "__main__":
    print(cal_get_me())