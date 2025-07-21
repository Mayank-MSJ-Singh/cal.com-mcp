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


def cal_get_all_webhook(take : int = None, skip : int = None):
    querystring = {}
    if take is not None:
        querystring["take"] = (take)
    if skip is not None:
        querystring["skip"] = (skip)

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

    triggers_list = (triggers)

    # Payload with required parameters
    payload = {
        "active": (active),
        "subscriberUrl": (subscriberUrl),
        "triggers": triggers_list
    }

    # Add optional parameters
    if payloadTemplate is not None:
        payload["payloadTemplate"] = str(payloadTemplate)
    if secret is not None:
        payload["secret"] = (secret)

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
        payload["active"] = (active)
    if subscriberUrl is not None:
        payload["subscriberUrl"] = (subscriberUrl)
    if triggers is not None:
        payload["triggers"] = (triggers)
    if payloadTemplate is not None:
        payload["payloadTemplate"] = str(payloadTemplate)
    if secret is not None:
        payload["secret"] = (secret)

    response = requests.request("PATCH", url_new, json=payload, headers=headers)
    return response.text





if __name__ == '__main__':
    import uuid

    print("---- TESTING cal_get_all_webhook ----")

    print("Test 1: take=5 (int)")
    print(cal_get_all_webhook(take=5))

    print("\nTest 2: take='5' (str)")
    print(cal_get_all_webhook(take='5'))

    print("\nTest 3: take=10, skip=2 (int)")
    print(cal_get_all_webhook(take=10, skip=2))

    print("\nTest 4: take='10', skip='2' (str)")
    print(cal_get_all_webhook(take='10', skip='2'))

    print("---- TESTING cal_create_webhook with unique URLs ----")

    def unique_url():
        return f"https://example.com/webhook/{uuid.uuid4()}"

    print("\nTest 5: active=True (bool), triggers=list")
    print(cal_create_webhook(
        active=True,
        subscriberUrl=unique_url(),
        triggers=["BOOKING_CREATED"]
    ))

    print("\nTest 6: active='true' (str), triggers='[...]' (str)")
    print(cal_create_webhook(
        active='true',
        subscriberUrl=unique_url(),
        triggers='["BOOKING_CREATED"]'
    ))

    print("\nTest 7: active='false', multiple triggers")
    print(cal_create_webhook(
        active='false',
        subscriberUrl=unique_url(),
        triggers='["BOOKING_CREATED", "BOOKING_CANCELLED", "MEETING_STARTED"]'
    ))

    print("\nTest 8: active=False (bool), payloadTemplate and secret")
    print(cal_create_webhook(
        active=False,
        subscriberUrl=unique_url(),
        triggers=["BOOKING_PAID"],
        payloadTemplate='{"custom":"{{booker.name}}"}',
        secret="my-secret"
    ))

    print("\nTest 9: active='false', triggers with valid list (str)")
    print(cal_create_webhook(
        active='false',
        subscriberUrl=unique_url(),
        triggers='["BOOKING_REJECTED", "MEETING_STARTED"]'
    ))

    print("\nTest 10: triggers with single valid trigger as str")
    print(cal_create_webhook(
        active='true',
        subscriberUrl=unique_url(),
        triggers='["MEETING_STARTED"]'
    ))

    print("---- TESTING cal_get_webhook / cal_update_webhook / cal_delete_webhook ----")


    # Helper to create a webhook and return its ID
    def create_test_webhook():
        response = cal_create_webhook(
            active=True,
            subscriberUrl=f"https://example.com/webhook/{uuid.uuid4()}",
            triggers=["BOOKING_CREATED"]
        )
        data = json.loads(response)
        return data["data"]["id"] if "data" in data else None


    # Test 11: Create webhook, then get it
    print("\nTest 11: Create + Get webhook")
    webhook_id = create_test_webhook()
    if webhook_id:
        print("Created:", webhook_id)
        print("Fetched:", cal_get_webhook(webhook_id))
    else:
        print("Webhook creation failed.")

    # Test 12: Update webhook active to false
    print("\nTest 12: Update webhook - active=False")
    if webhook_id:
        print(cal_update_webhook(
            webhookId=webhook_id,
            active=False
        ))

    # Test 13: Update webhook - new subscriberUrl (stringified)
    print("\nTest 13: Update webhook - subscriberUrl as string")
    if webhook_id:
        new_url = f"https://example.com/webhook/{uuid.uuid4()}"
        print(cal_update_webhook(
            webhookId=webhook_id,
            subscriberUrl=f'"{new_url}"'  # passing as a quoted string
        ))

    # Test 14: Update webhook - multiple triggers (stringified list)
    print("\nTest 14: Update webhook - triggers as string")
    if webhook_id:
        print(cal_update_webhook(
            webhookId=webhook_id,
            triggers='["BOOKING_CANCELLED", "MEETING_STARTED"]'
        ))

    # Test 15: Update webhook - payloadTemplate and secret
    print("\nTest 15: Update webhook - payloadTemplate + secret")
    if webhook_id:
        print(cal_update_webhook(
            webhookId=webhook_id,
            payloadTemplate='{"custom":"{{booker.name}}"}',
            secret="updated-secret"
        ))

    # Test 16: Delete webhook
    print("\nTest 16: Delete webhook")
    if webhook_id:
        print(cal_delete_webhook(webhook_id))