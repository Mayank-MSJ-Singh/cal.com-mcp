import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()


url = "https://api.cal.com/v2/event-types/"
auth = os.getenv("CAL_COM_API_KEY")
cal_api_version = "2024-06-14"

headers = {
        "Authorization": auth,
        "cal-api-version": cal_api_version
    }


#There is a problem with get_all_event_types right Now!!!
def get_all_event_types():

    response = requests.request("GET", url, headers=headers)
    print(response.text)

def cal_get_event_type(eventTypeId):
    url_new = url + str(eventTypeId)
    response = requests.request("GET", url_new, headers=headers)

    return response.text

def cal_delete_event_type(eventTypeId):
    url_new = url + str(eventTypeId)
    response = requests.request("DELETE", url_new, headers=headers)
    return response.text


def cal_create_event_type(
        lengthInMinutes: int,
        title: str,
        slug: str,
        # Simple optional parameters
        lengthInMinutesOptions: list = None,
        description: str = None,
        bookingFields: list = None,
        disableGuests: bool = None,
        slotInterval: int = None,
        minimumBookingNotice: int = None,
        beforeEventBuffer: int = None,
        afterEventBuffer: int = None,
        scheduleId: int = None,
        onlyShowFirstAvailableSlot: bool = None,
        offsetStart: int = None,
        requiresBookerEmailVerification: bool = None,
        hideCalendarNotes: bool = None,
        lockTimeZoneToggleOnBookingPage: bool = None,
        customName: str = None,
        useDestinationCalendarEmail: bool = None,
        hideCalendarEventDetails: bool = None,
        successRedirectUrl: str = None,
        hideOrganizerEmail: bool = None,
        # Complex/object parameters
        bookingLimitsCount: dict = None,
        bookingLimitsDuration: dict = None,
        bookingWindow: dict = None,
        bookerLayouts: dict = None,
        confirmationPolicy: dict = None,
        recurrence: dict = None,
        color: dict = None,
        seats: dict = None,
        destinationCalendar: dict = None,
        calVideoSettings: dict = None,
        locations: list = None
):
    # Start with required parameters
    payload = {
        "lengthInMinutes": lengthInMinutes,
        "title": title,
        "slug": slug
    }

    # Add simple optional parameters
    optional_simple = {
        "lengthInMinutesOptions": lengthInMinutesOptions,
        "description": description,
        "bookingFields": bookingFields,
        "disableGuests": disableGuests,
        "slotInterval": slotInterval,
        "minimumBookingNotice": minimumBookingNotice,
        "beforeEventBuffer": beforeEventBuffer,
        "afterEventBuffer": afterEventBuffer,
        "scheduleId": scheduleId,
        "onlyShowFirstAvailableSlot": onlyShowFirstAvailableSlot,
        "offsetStart": offsetStart,
        "requiresBookerEmailVerification": requiresBookerEmailVerification,
        "hideCalendarNotes": hideCalendarNotes,
        "lockTimeZoneToggleOnBookingPage": lockTimeZoneToggleOnBookingPage,
        "customName": customName,
        "useDestinationCalendarEmail": useDestinationCalendarEmail,
        "hideCalendarEventDetails": hideCalendarEventDetails,
        "successRedirectUrl": successRedirectUrl,
        "hideOrganizerEmail": hideOrganizerEmail,
    }

    # Add complex/object parameters
    optional_complex = {
        "bookingLimitsCount": bookingLimitsCount,
        "bookingLimitsDuration": bookingLimitsDuration,
        "bookingWindow": bookingWindow,
        "bookerLayouts": bookerLayouts,
        "confirmationPolicy": confirmationPolicy,
        "recurrence": recurrence,
        "color": color,
        "seats": seats,
        "destinationCalendar": destinationCalendar,
        "calVideoSettings": calVideoSettings,
        "locations": locations
    }

    # Add non-None simple parameters
    for key, value in optional_simple.items():
        if value is not None:
            payload[key] = value

    # Add non-None complex parameters
    for key, value in optional_complex.items():
        if value is not None:
            payload[key] = value

    response = requests.request("POST", url, json=payload, headers=headers)

    return (response.text)


def cal_update_event_type(
        eventTypeId: int,
        # Simple parameters
        lengthInMinutes: int = None,
        title: str = None,
        slug: str = None,
        lengthInMinutesOptions: list = None,
        description: str = None,
        bookingFields: list = None,
        disableGuests: bool = None,
        slotInterval: int = None,
        minimumBookingNotice: int = None,
        beforeEventBuffer: int = None,
        afterEventBuffer: int = None,
        scheduleId: int = None,
        onlyShowFirstAvailableSlot: bool = None,
        offsetStart: int = None,
        requiresBookerEmailVerification: bool = None,
        hideCalendarNotes: bool = None,
        lockTimeZoneToggleOnBookingPage: bool = None,
        customName: str = None,
        useDestinationCalendarEmail: bool = None,
        hideCalendarEventDetails: bool = None,
        successRedirectUrl: str = None,
        hideOrganizerEmail: bool = None,
        # Complex parameters
        bookingLimitsCount: dict = None,
        bookingLimitsDuration: dict = None,
        bookingWindow: dict = None,
        bookerLayouts: dict = None,
        confirmationPolicy: dict = None,
        recurrence: dict = None,
        color: dict = None,
        seats: dict = None,
        destinationCalendar: dict = None,
        calVideoSettings: dict = None,
        locations: list = None
):

    url_new = url + str(eventTypeId)
    # Start with empty payload
    payload = {}

    # Simple parameters mapping
    simple_params = {
        "lengthInMinutes": lengthInMinutes,
        "title": title,
        "slug": slug,
        "lengthInMinutesOptions": lengthInMinutesOptions,
        "description": description,
        "bookingFields": bookingFields,
        "disableGuests": disableGuests,
        "slotInterval": slotInterval,
        "minimumBookingNotice": minimumBookingNotice,
        "beforeEventBuffer": beforeEventBuffer,
        "afterEventBuffer": afterEventBuffer,
        "scheduleId": scheduleId,
        "onlyShowFirstAvailableSlot": onlyShowFirstAvailableSlot,
        "offsetStart": offsetStart,
        "requiresBookerEmailVerification": requiresBookerEmailVerification,
        "hideCalendarNotes": hideCalendarNotes,
        "lockTimeZoneToggleOnBookingPage": lockTimeZoneToggleOnBookingPage,
        "customName": customName,
        "useDestinationCalendarEmail": useDestinationCalendarEmail,
        "hideCalendarEventDetails": hideCalendarEventDetails,
        "successRedirectUrl": successRedirectUrl,
        "hideOrganizerEmail": hideOrganizerEmail
    }

    # Complex parameters mapping
    complex_params = {
        "bookingLimitsCount": bookingLimitsCount,
        "bookingLimitsDuration": bookingLimitsDuration,
        "bookingWindow": bookingWindow,
        "bookerLayouts": bookerLayouts,
        "confirmationPolicy": confirmationPolicy,
        "recurrence": recurrence,
        "color": color,
        "seats": seats,
        "destinationCalendar": destinationCalendar,
        "calVideoSettings": calVideoSettings,
        "locations": locations
    }

    # Add non-None simple parameters
    for key, value in simple_params.items():
        if value is not None:
            payload[key] = value

    # Add non-None complex parameters
    for key, value in complex_params.items():
        if value is not None:
            payload[key] = value

    response = requests.request("PATCH", url_new, json=payload, headers=headers)
    return (response.text)

if __name__ == "__main__":
    #print(cal_get_event_type('2779104'))
    #print(cal_delete_event_type('2779104'))
    print(cal_get_event_type('2785245'))
    #get_all_event_types()
    print(cal_create_event_type(15, 'new test event','new-test-event')) #2785245
    pass