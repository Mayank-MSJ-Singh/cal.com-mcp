import requests
import json
from dotenv import load_dotenv
import os
import ast

# Load environment variables
load_dotenv()

# API endpoint and auth
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
    """
        Creates a new event type by making a POST request to the Cal API endpoint.

        Builds a JSON payload from provided parameters and sends to the events endpoint.
        Required parameters must be provided, while optional parameters are included
        only when their value is not None.

        Required Parameters:
            lengthInMinutes (int): Duration of the event in minutes
            title (str): Display name for the event type
            slug (str): Unique identifier for the event type URL

        Optional Simple Parameters:
            lengthInMinutesOptions (list): Allow users to choose between different event lengths
            description (str): Event description shown to bookers
            bookingFields (list): Custom fields added to booking form (objects with type, label, placeholder)
            disableGuests (bool): Prevent bookers from adding guests
            slotInterval (int): Time between available slots (minutes)
            minimumBookingNotice (int): Minimum advance notice for bookings (minutes)
            beforeEventBuffer (int): Buffer time before events (minutes)
            afterEventBuffer (int): Buffer time after events (minutes)
            scheduleId (int): Custom schedule ID for this event
            onlyShowFirstAvailableSlot (bool): Limit availability to one slot/day
            offsetStart (int): Timeslot offset for bookers (minutes)
            requiresBookerEmailVerification (bool): Require email verification for booking
            hideCalendarNotes (bool): Hide calendar notes from bookers
            lockTimeZoneToggleOnBookingPage (bool): Disable timezone switching
            customName (str): Custom event name using template variables
            useDestinationCalendarEmail (bool): Use destination calendar's email
            hideCalendarEventDetails (bool): Hide event details in calendars
            successRedirectUrl (str): Custom redirect URL after booking
            hideOrganizerEmail (bool): Hide organizer's email address

        Optional Complex Parameters (dict objects):
            bookingLimitsCount: Limit total bookings per period
                - day (int): Daily booking limit
                - week (int): Weekly booking limit
                - month (int): Monthly booking limit
                - year (int): Yearly booking limit
                - disabled (bool): Disable limits

            bookingLimitsDuration: Limit total booking duration per period
                - day (int): Minutes/day (multiple of 15)
                - week (int): Minutes/week (multiple of 15)
                - month (int): Minutes/month (multiple of 15)
                - year (int): Minutes/year (multiple of 15)

            bookingWindow: Limit how far ahead bookings can be made
                - type (str): 'businessDays' | 'calendarDays' | 'range'
                - value (int): Days into future
                - rolling (bool): Rolling vs fixed window behavior

            bookerLayouts: Configure booker calendar views
                - defaultLayout (str): Default view ('month','week','column')
                - enabledLayouts (list): Available layouts

            confirmationPolicy: Manual confirmation settings
                - type (str): Policy type
                - blockUnconfirmedBookingsInBooker (bool): Block slots for unconfirmed bookings
                - noticeThreshold (dict): Time threshold settings
                    • unit (str): Time unit ('minutes','hours')
                    • count (int): Threshold value

            recurrence: Recurring event settings
                - interval (int): Repeat frequency count
                - occurrences (int): Total event instances
                - frequency (str): Time unit ('week','month','year')

            color: Event color theming
                - lightThemeHex (str): Hex code for light mode
                - darkThemeHex (str): Hex code for dark mode

            seats: Multi-seat event configuration
                - seatsPerTimeSlot (int): Available seats per slot
                - showAttendeeInfo (bool): Reveal attendees to others
                - showAvailabilityCount (bool): Show seat counter

            destinationCalendar: Calendar sync target
                - integration (str): Calendar service type
                - externalId (str): Target calendar ID

            calVideoSettings: Video meeting options
                - disableRecordingForOrganizer (bool): Block organizer recording
                - disableRecordingForGuests (bool): Block attendee recording
                - redirectUrlOnExit (dict): Post-call redirect URL

            locations (list): Physical/virtual event locations
                - type (str): Location type ('address')
                - address (str): Physical address
                - public (bool): Public visibility

        Returns:
            str: Raw response text from the API call

        Note:
            The function expects external dependencies:
            - `requests` module for HTTP calls
            - `()` function for parameter processing
            - Predefined `url` and `headers` variables
        """
    # Build payload with required fields
    payload = {
        "lengthInMinutes": (lengthInMinutes),
        "title": (title),
        "slug": (slug)
    }

    # Map optional parameters
    optional_params = {
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
        # Complex
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

    # Add non-None params with parsing
    for key, value in optional_params.items():
        if value is not None:
            payload[key] = (value)



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
    """
        Updates an existing event type by making a PATCH request to the Cal API endpoint.

        Builds a JSON payload from provided parameters and sends to the events endpoint.
        Only non-None parameters will be included in the update. At least one optional parameter
        must be provided for a valid update.

        Required Parameter:
            eventTypeId (int): ID of the event type to update

        Optional Parameters:
            lengthInMinutes (int): Duration of the event in minutes
            title (str): Display name for the event type
            slug (str): Unique identifier for the event type URL
            lengthInMinutesOptions (list): Allow users to choose between different event lengths
            description (str): Event description shown to bookers
            bookingFields (list): Custom fields added to booking form
            disableGuests (bool): Prevent bookers from adding guests
            slotInterval (int): Time between available slots (minutes)
            minimumBookingNotice (int): Minimum advance notice for bookings (minutes)
            beforeEventBuffer (int): Buffer time before events (minutes)
            afterEventBuffer (int): Buffer time after events (minutes)
            scheduleId (int): Custom schedule ID for this event
            onlyShowFirstAvailableSlot (bool): Limit availability to one slot/day
            offsetStart (int): Timeslot offset for bookers (minutes)
            requiresBookerEmailVerification (bool): Require email verification for booking
            hideCalendarNotes (bool): Hide calendar notes from bookers
            lockTimeZoneToggleOnBookingPage (bool): Disable timezone switching
            customName (str): Custom event name using template variables
            useDestinationCalendarEmail (bool): Use destination calendar's email
            hideCalendarEventDetails (bool): Hide event details in calendars
            successRedirectUrl (str): Custom redirect URL after booking
            hideOrganizerEmail (bool): Hide organizer's email address

            bookingLimitsCount (dict): Limit total bookings per period
                - day (int): Daily booking limit
                - week (int): Weekly booking limit
                - month (int): Monthly booking limit
                - year (int): Yearly booking limit
                - disabled (bool): Disable limits

            bookingLimitsDuration (dict): Limit total booking duration per period
                - day (int): Minutes/day (multiple of 15)
                - week (int): Minutes/week (multiple of 15)
                - month (int): Minutes/month (multiple of 15)
                - year (int): Minutes/year (multiple of 15)

            bookingWindow (dict): Limit how far ahead bookings can be made
                - type (str): 'business' | 'calendar' | 'range'
                - value (int): Days into future
                - rolling (bool): Rolling vs fixed window behavior

            bookerLayouts (dict): Configure booker calendar views
                - defaultLayout (str): Default view ('month','week','column')
                - enabledLayouts (list): Available layouts

            confirmationPolicy (dict): Manual confirmation settings
                - type (str): Policy type
                - blockUnconfirmedBookingsInBooker (bool): Block slots for unconfirmed bookings
                - noticeThreshold (dict): Time threshold settings
                    • unit (str): Time unit ('minutes','hours')
                    • count (int): Threshold value

            recurrence (dict): Recurring event settings
                - interval (int): Repeat frequency count
                - occurrences (int): Total event instances
                - frequency (str): Time unit ('week','month','year')

            color (dict): Event color theming
                - lightThemeHex (str): Hex code for light mode
                - darkThemeHex (str): Hex code for dark mode

            seats (dict): Multi-seat event configuration
                - seatsPerTimeSlot (int): Available seats per slot
                - showAttendeeInfo (bool): Reveal attendees to others
                - showAvailabilityCount (bool): Show seat counter

            destinationCalendar (dict): Calendar sync target
                - integration (str): Calendar service type
                - externalId (str): Target calendar ID

            calVideoSettings (dict): Video meeting options
                - disableRecordingForOrganizer (bool): Block organizer recording
                - disableRecordingForGuests (bool): Block attendee recording
                - redirectUrlOnExit (dict): Post-call redirect URL

            locations (list): Physical/virtual event locations
                - type (str): Location type ('address')
                - address (str): Physical address
                - public (bool): Public visibility

        Returns:
            str: Raw response text from the API call

        Note:
            - Requires `requests` module and predefined `url` and `headers`
            - Only provided parameters will be updated (partial update)
            - Complex parameters replace existing values (full object replacement)
        """

    url_new = url + str(eventTypeId)
    payload = {}

    params = {
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
        "hideOrganizerEmail": hideOrganizerEmail,
        # Complex
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

    for key, val in params.items():
        if val is not None:
            # convert ints for required numeric fields
            payload[key] = (val)

    response = requests.request("PATCH", url_new, json=payload, headers=headers)
    return (response.text)

if __name__ == "__main__":
    import uuid
    print("\n--- TESTING cal_get_event_type and cal_delete_event_type ---")

    # Create a test event type first
    created = cal_create_event_type(
        lengthInMinutes="30",
        title="Temp Event for GET/DELETE",
        slug="temp-event-get-delete",
        description="This will be fetched and then deleted"
    )

    try:
        data = json.loads(created)
        event_id = data["data"]["id"]
    except Exception as e:
        print("Failed to create event type:", e)
        event_id = None

    # Test: Get the event type
    if event_id:
        print("\nTest 1: cal_get_event_type")
        result = cal_get_event_type(event_id)
        print(result)

        # Test: Delete the event type
        print("\nTest 2: cal_delete_event_type")
        result = cal_delete_event_type(event_id)
        print(result)

        # Test: Try to get the deleted event type (should 404 or fail)
        print("\nTest 3: cal_get_event_type (after delete)")
        result = cal_get_event_type(event_id)
        print(result)
    else:
        print("Event ID not available for get/delete tests.")



    print("\n--- TESTING cal_create_event_type ---")

    created_event_ids = {}  # collect all created event IDs for future update tests


    def print_event_type_response(test_id, label, response):
        print(f"\nTest {test_id}: {label}")
        print(response)
        try:
            data = json.loads(response)
            if data.get("status") == "success":
                event_id = data["data"]["id"]
                created_event_ids[test_id] = event_id
        except Exception:
            pass


    # Test 4: Minimal required
    response = cal_create_event_type(
        lengthInMinutes="15",
        title="Simple Event",
        slug="simple-event"
    )
    print_event_type_response(4, "Only required fields", response)

    # Test 5: Basic optionals
    response = cal_create_event_type(
        lengthInMinutes="30",
        title="With Optionals",
        slug="with-optionals",
        description="This is optional description",
        disableGuests="true",
        hideOrganizerEmail="false"
    )
    print_event_type_response(5, "With simple optional booleans and description", response)

    # Test 6: With location (complex list of dicts)
    response = cal_create_event_type(
        lengthInMinutes="45",
        title="Event With Location",
        slug="event-location",
        locations='[{"type": "address", "address": "123 Mars Colony", "public": true}]'
    )
    print_event_type_response(6, "With locations list", response)

    # Test 7: All boolean toggles
    response = cal_create_event_type(
        lengthInMinutes="60",
        title="All Booleans",
        slug="all-booleans",
        disableGuests="true",
        onlyShowFirstAvailableSlot="false",
        requiresBookerEmailVerification="true",
        hideCalendarNotes="false",
        lockTimeZoneToggleOnBookingPage="true",
        useDestinationCalendarEmail="false",
        hideCalendarEventDetails="true",
        hideOrganizerEmail="true"
    )
    print_event_type_response(7, "All boolean flags", response)

    # Test 8: Booking limits + window + bookerLayouts( Creating Error) -------------------------------------
    '''
    response = cal_create_event_type(
        lengthInMinutes="90",
        title="With Limits",
        slug="with-limits",
        bookingLimitsCount='{"value": 3, "period": "day"}',
        bookingLimitsDuration='{"value": 60, "period": "week"}',
        bookingWindow='{"type": "calendarDays", "value": 14, "rolling": True}',
        bookerLayouts='{"defaultLayout": "week", "enabledLayouts": ["week", "month", "column"]}'
    )
    print_event_type_response(8, "With booking limits + window + bookerLayouts", response)
    '''

    # Test 9: Buffers and intervals
    response = cal_create_event_type(
        lengthInMinutes="30",
        title="Buffer Event",
        slug="buffer-event",
        beforeEventBuffer="10",
        afterEventBuffer="15",
        slotInterval="5",
        minimumBookingNotice="30"
    )
    print_event_type_response(9, "With buffer and slot configs", response)

    # Test 10: Confirmation, recurrence, color, seats, calVideoSettings
    response = cal_create_event_type(
        lengthInMinutes="45",
        title="Advanced Configs",
        slug="advanced-configs-v2",
        confirmationPolicy='{"type": "always"}',
        recurrence='{"disabled": false, "frequency": "weekly", "interval": 1, "occurrences": 5}',
        color='{"backgroundColor": "#ff0000", "textColor": "#ffffff"}',
        seats=None,
        calVideoSettings=None
    )

    print_event_type_response(10, "With confirmationPolicy, recurrence, color, seats, video", response)

    # Test 11: All simple optionals + successRedirectUrl + customName
    response = cal_create_event_type(
        lengthInMinutes="60",
        title="Redirect Test",
        slug="redirect-test",
        successRedirectUrl="https://nikki.com/success",
        customName="Redirect Event",
        disableGuests="false",
        hideOrganizerEmail="false"
    )
    print_event_type_response(11, "Success redirect + customName", response)

    # Test 12: With everything together (final blast) ( Creating Error) -------------------------------------
    response = cal_create_event_type(
        lengthInMinutes="60",
        title="Full Load Test",
        slug="full-load",
        lengthInMinutesOptions="[15, 30, 45, 60]",
        description="All options set here",
        bookingFields='[{"type": "name", "label": "Your Name", "placeholder": "Enter your full name", "disableOnPrefill": false}]',
        disableGuests="true",
        slotInterval="10",
        minimumBookingNotice="60",
        beforeEventBuffer="5",
        afterEventBuffer="5",
        scheduleId="731593",
        onlyShowFirstAvailableSlot="true",
        offsetStart="0",
        requiresBookerEmailVerification="true",
        hideCalendarNotes="false",
        lockTimeZoneToggleOnBookingPage="true",
        customName="Ultimate Event",
        useDestinationCalendarEmail="false",
        hideCalendarEventDetails="true",
        successRedirectUrl="https://nikki.com/done",
        hideOrganizerEmail="false",
        bookingLimitsCount='{"value": 5, "period": "week"}',
        bookingLimitsDuration='{"value": 180, "period": "day"}',
        bookingWindow='{"type": "calendarDays", "value": 7, "rolling": true}',
        bookerLayouts='{"defaultLayout": "week", "enabledLayouts": ["month", "week", "column"]}',
        confirmationPolicy='{"type": "always"}',
        recurrence='{"disabled": false, "frequency": "weekly", "interval": 1, "occurrences": 5}',
        color='{"backgroundColor": "#333", "textColor": "#fff"}',
        seats='{"value": 10}',
        destinationCalendar='{"integration": "google_calendar", "externalId": "mayanksingh8713491@gmail.com"}',
        calVideoSettings='{"provider": "zoom"}',
        locations='[{"type": "address", "address": "123 Main Street, Bangalore", "public": true}]'
    )

    print_event_type_response(12, "Everything included", response)

    print("\n--- TESTING cal_update_event_type ---")


    def print_update_response(test_id, label, response):
        print(f"\nTest {test_id}: {label}")
        print(response)


    try:
        # Use previously collected event IDs
        test_event_id = created_event_ids.get(4)
        if not test_event_id:
            raise ValueError("Event ID for Test 4 not found.")

        # Test 13: Update title
        response = cal_update_event_type(
            eventTypeId=test_event_id,
            title="Updated Title"
        )
        print_update_response(13, "Update only title", response)

        # Test 14: Change duration and slug
        response = cal_update_event_type(
            eventTypeId=test_event_id,
            lengthInMinutes="60",
            slug="updated-slug"
        )
        print_update_response(14, "Update length and slug", response)

        # Test 15: Update description and disableGuests
        response = cal_update_event_type(
            eventTypeId=created_event_ids.get(5),
            description="Updated description",
            disableGuests="true"
        )
        print_update_response(15, "Update description and disableGuests", response)

        # Test 16: Update locations
        response = cal_update_event_type(
            eventTypeId=created_event_ids.get(6),
            locations='[{"type": "zoom", "value": "zoom-link"}]'
        )
        print_update_response(16, "Update locations", response)

        # Test 17: All boolean flags update
        response = cal_update_event_type(
            eventTypeId=created_event_ids.get(7),
            onlyShowFirstAvailableSlot="false",
            requiresBookerEmailVerification="false",
            hideCalendarNotes="true",
            lockTimeZoneToggleOnBookingPage="true",
            useDestinationCalendarEmail="false",
            hideCalendarEventDetails="true",
            hideOrganizerEmail="true"
        )
        print_update_response(17, "Update all boolean options", response)

        # Test 18: Booking limits + booking window
        response = cal_update_event_type(
            eventTypeId=created_event_ids.get(8),
            bookingLimitsCount='{"value": 2, "period": "week"}',
            bookingWindow='{"minTimeBeforeEvent": 600, "maxTimeBeforeEvent": 3600000}'
        )
        print_update_response(18, "Update booking limits and window", response)

        # Test 19: Update buffers and intervals
        response = cal_update_event_type(
            eventTypeId=created_event_ids.get(9),
            beforeEventBuffer="5",
            afterEventBuffer="5",
            slotInterval="10",
            minimumBookingNotice="15"
        )
        print_update_response(19, "Update buffers and timing", response)

        # Test 20: Update all advanced configs
        response = cal_update_event_type(
            eventTypeId=created_event_ids.get(10),
            confirmationPolicy='{"type": "email"}',
            recurrence='{"frequency": "monthly", "interval": 1}',
            color='{"backgroundColor": "#00ff00", "textColor": "#000000"}',
            seats='{"value": 3}',
            calVideoSettings='{"provider": "meet"}',
            destinationCalendar='{"type": "google_calendar"}'
        )
        print_update_response(20, "Update confirmation, recurrence, colors", response)

        # Test 21: Update everything together
        response = cal_update_event_type(
            eventTypeId=created_event_ids.get(11),
            lengthInMinutes="45",
            title="Fully Updated Event",
            slug="fully-updated",
            description="Full update",
            bookingFields='[{"type": "email", "required": true}]',
            disableGuests="true",
            slotInterval="15",
            minimumBookingNotice="30",
            beforeEventBuffer="5",
            afterEventBuffer="5",
            scheduleId="56789",
            onlyShowFirstAvailableSlot="false",
            offsetStart="10",
            requiresBookerEmailVerification="true",
            hideCalendarNotes="false",
            lockTimeZoneToggleOnBookingPage="false",
            customName="Final Updated",
            useDestinationCalendarEmail="true",
            hideCalendarEventDetails="true",
            successRedirectUrl="https://example.com/done",
            hideOrganizerEmail="false",
            bookingLimitsCount='{"value": 2, "period": "month"}',
            bookingLimitsDuration='{"value": 30, "period": "day"}',
            bookingWindow='{"minTimeBeforeEvent": 900, "maxTimeBeforeEvent": 7200000}',
            bookerLayouts='{"fields": [{"type": "email"}]}',
            confirmationPolicy='{"type": "none"}',
            recurrence='{"frequency": "daily"}',
            color='{"backgroundColor": "#000", "textColor": "#fff"}',
            seats='{"value": 10}',
            destinationCalendar='{"type": "outlook"}',
            calVideoSettings='{"provider": "zoom"}',
            locations='[{"type": "custom", "value": "custom-link"}]'
        )
        print_update_response(21, "Update with everything", response)

    except Exception as e:
        print("\nUpdate Tests Failed:", e)

    print("\n--- CLEANING UP: Deleting all created event types ---")

    for test_id, event_id in created_event_ids.items():
        try:
            delete_response = cal_delete_event_type(event_id)
            print(f"Deleted event (Test {test_id}, ID {event_id}): {delete_response}")
        except Exception as e:
            print(f"Failed to delete event (Test {test_id}, ID {event_id}): {e}")
