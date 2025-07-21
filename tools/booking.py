#Not Working Properly
#Not Working Properly
#Not Working Properly

import requests
import json
from dotenv import load_dotenv
import os
import ast

load_dotenv()

url = "https://api.cal.com/v2/bookings"

auth = os.getenv("CAL_COM_API_KEY")

headers = {
        "Authorization": auth,
        "cal-api-version": "2024-08-13",
        "Content-Type": "application/json"
    }

def cal_get_all_bookings(
        status=None,
        attendeeEmail=None,
        attendeeName=None,
        bookingUid=None,
        eventTypeIds=None,
        eventTypeId=None,
        teamsIds=None,
        teamId=None,
        afterStart=None,
        beforeEnd=None,
        afterCreatedAt=None,
        beforeCreatedAt=None,
        afterUpdatedAt=None,
        beforeUpdatedAt=None,
        sortStart=None,
        sortEnd=None,
        sortCreated=None,
        sortUpdatedAt=None,
        take=100,
        skip=0
):
    """
    Retrieves bookings with extensive filtering and sorting options

    Args:
        status: Filter by status (list or comma-separated string)
        attendeeEmail: Filter by attendee email
        attendeeName: Filter by attendee name
        bookingUid: Filter by booking UID
        eventTypeIds: Filter by event type IDs (list or comma-separated string)
        eventTypeId: Filter by single event type ID
        teamsIds: Filter by team IDs (list or comma-separated string)
        teamId: Filter by single team ID
        afterStart: Filter bookings starting after this date (ISO format)
        beforeEnd: Filter bookings ending before this date (ISO format)
        afterCreatedAt: Filter bookings created after this date
        beforeCreatedAt: Filter bookings created before this date
        afterUpdatedAt: Filter bookings updated after this date
        beforeUpdatedAt: Filter bookings updated before this date
        sortStart: Sort by start time ("asc" or "desc")
        sortEnd: Sort by end time ("asc" or "desc")
        sortCreated: Sort by creation time ("asc" or "desc")
        sortUpdatedAt: Sort by update time ("asc" or "desc")
        take: Number of results to return (default 100)
        skip: Number of results to skip (default 0)

    Returns:
        JSON response with bookings
    """
    querystring = {}
    # Add simple parameters
    simple_params = {
        "attendeeEmail": attendeeEmail,
        "attendeeName": attendeeName,
        "bookingUid": bookingUid,
        "eventTypeId": eventTypeId,
        "teamId": teamId,
        "afterStart": afterStart,
        "beforeEnd": beforeEnd,
        "afterCreatedAt": afterCreatedAt,
        "beforeCreatedAt": beforeCreatedAt,
        "afterUpdatedAt": afterUpdatedAt,
        "beforeUpdatedAt": beforeUpdatedAt,
        "sortStart": sortStart,
        "sortEnd": sortEnd,
        "sortCreated": sortCreated,
        "sortUpdatedAt": sortUpdatedAt,
        "take": take,
        "skip": skip,
        "eventTypeIds": eventTypeIds,
        "teamsIds": teamsIds,
    }

    # Add non-None simple parameters
    for key, value in simple_params.items():
        if value is not None:
            querystring[key] = value

    if status is not None:
        querystring['status'] = ast.literal_eval(status)

    response = requests.request("GET", url, headers=headers, params=querystring)

    return (response.text)


def cal_create_booking(
        start: str,
        attendee: dict,
        eventTypeId: int = None,
        eventTypeSlug: str = None,
        username: str = None,
        teamSlug: str = None,
        organizationSlug: str = None,
        bookingFieldsResponses: dict = None,
        guests: list = None,
        meetingUrl: str = None,
        location: dict = None,
        metadata: dict = None,
        lengthInMinutes: int = None,
        routing: dict = None,
        recurrenceCount: int = None
):
    """
    Creates a new booking with the specified parameters

    Args:
        start (str): Start time in ISO 8601 format (UTC) - REQUIRED
        attendee (dict): Attendee details - REQUIRED
            Must include:
                name (str) - REQUIRED
                timeZone (str) - REQUIRED
                email (str, optional)
                phoneNumber (str, optional)
                language (str, optional)
        eventTypeId (int): Event type ID
        eventTypeSlug (str): Event type slug
        username (str): Username of event owner
        teamSlug (str): Team slug
        organizationSlug (str): Organization slug
        bookingFieldsResponses (dict): Custom booking field responses
        guests (list): List of guest email addresses
        meetingUrl (str): DEPRECATED - Use location instead
        location (dict): Location object (type must be "address")
        metadata (dict): Additional metadata (max 50 keys)
        lengthInMinutes (int): Custom booking duration
        routing (dict): Routing information including:
            responseId (int) - REQUIRED
            teamMemberIds (list) - REQUIRED
            teamMemberEmail (str, optional)
            skipContactOwner (bool, optional)
            crmAppSlug (str, optional)
            crmOwnerRecordType (str, optional)
        recurrenceCount (int): Number of recurrences

    Returns:
        JSON response with booking details
    """

    payload = {
        'start': start,
        'attendee': attendee,
    }
    
    top_level_params = {
        "eventTypeId": eventTypeId,
        "eventTypeSlug": eventTypeSlug,
        "username": username,
        "teamSlug": teamSlug,
        "organizationSlug": organizationSlug,
        "bookingFieldsResponses": bookingFieldsResponses,
        "meetingUrl": meetingUrl,
        "location": location,
        "metadata": metadata,
        "lengthInMinutes": lengthInMinutes,
        "routing": routing,
        "recurrenceCount": recurrenceCount
    }

    # Add non-None top-level parameters
    for key, value in top_level_params.items():
        if value is not None:
            payload[key] = value

    if guests is not None:
        payload['guests'] = ast.literal_eval(guests)

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.text

if __name__ == "__main__":
    #print(cal_get_all_bookings(status='["upcoming","past"]'))
    a = {"name": "John Doe","email": "john.doe@example.com","timeZone": "America/New_York","phoneNumber": "+919876543210","language": "it"}
    print(cal_create_booking("2035-07-08T10:00:00Z",a, 2798202))
    pass