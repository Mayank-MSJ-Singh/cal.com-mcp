import requests
import json
from dotenv import load_dotenv
import os
import ast

load_dotenv()

url = "https://api.cal.com/v2/webhooks"
auth = os.getenv("CAL_COM_API_KEY")

headers = {
        "Authorization": auth,
        "Content-Type": "application/json"
    }

def str_to_bool(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.lower() in ("true", "1", "yes")
    return bool(value)


def cal_get_all_webhook(take : int = None, skip : int = None):
    querystring = {}
    if take is not None:
        querystring["take"] = str(take)
    if skip is not None:
        querystring["skip"] = str(skip)

    response = requests.request("GET", url, headers=headers, params=querystring)
    return (response.text)



def cal_create_webhook(
        active: bool,
        subscriberUrl: str,
        triggers: list,
        payloadTemplate: str = None,
        secret: str = None,
):
    """
    Creates a webhook for a specific event type
    Requires authentication as the event type owner

    Args:
        active: Whether webhook is active (required)
        subscriberUrl: URL to receive webhook payloads (required)
        triggers: List of trigger events (required)
        payloadTemplate: Custom payload template (optional)
        secret: Secret for verifying webhooks (optional)

    Returns:
        Response JSON or error details
    """

    triggers_list = ast.literal_eval(triggers)

    # Payload with required parameters
    payload = {
        "active": str_to_bool(active),
        "subscriberUrl": subscriberUrl,
        "triggers": triggers_list
    }

    # Add optional parameters
    if payloadTemplate is not None:
        payload["payloadTemplate"] = payloadTemplate
    if secret is not None:
        payload["secret"] = secret

    response = requests.request("POST", url, json=payload, headers=headers)
    return (response.text)

def cal_get_webhook(webhookId: str):
    url_new = f"{url}/{webhookId}"
    response = requests.request("GET", url_new, headers=headers)
    return (response.text)

def cal_delete_webhook(webhookId: str):

    url_new = f"{url}/{webhookId}"

    response = requests.request("DELETE", url_new, headers=headers)
    return response.text

def cal_update_webhook(
        webhookId: str,
        active: bool = None,
        subscriberUrl: str = None,
        triggers: list = None,
        payloadTemplate: str = None,
        secret: str = None,
):
    """
    Updates an existing webhook for a specific event type.

    Args:
        webhookId: ID of the webhook to update (required)
        active: Enable or disable the webhook (optional)
        subscriberUrl: New subscriber URL (optional)
        triggers: List of updated trigger events (optional)
        payloadTemplate: Updated custom payload template (optional)
        secret: Updated webhook secret (optional)

    Returns:
        Response JSON or error details
    """
    # Endpoint URL
    url_new = f"{url}/{webhookId}"

    # Prepare payload with only provided fields
    payload = {}
    if active is not None:
        payload["active"] = str_to_bool(active)
    if subscriberUrl is not None:
        payload["subscriberUrl"] = subscriberUrl
    if triggers is not None:
        payload["triggers"] = ast.literal_eval(triggers) if isinstance(triggers, str) else triggers
    if payloadTemplate is not None:
        payload["payloadTemplate"] = payloadTemplate
    if secret is not None:
        payload["secret"] = secret

    response = requests.request("PATCH", url_new, json=payload, headers=headers)
    return response.text





if __name__ == "__main__":
    pass



