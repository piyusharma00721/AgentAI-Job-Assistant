from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from datetime import datetime, timedelta
from database.crud import store_event
from database.db import SessionLocal


def get_upcoming_events(creds: Credentials, days_ahead: int = 7):
    """
    🔍 Fetches upcoming calendar events with detailed metadata.
    """
    service = build("calendar", "v3", credentials=creds)

    now = datetime.utcnow().isoformat() + 'Z'
    end = (datetime.utcnow() + timedelta(days=days_ahead)).isoformat() + 'Z'

    try:
        events_result = service.events().list(
            calendarId='primary',
            timeMin=now,
            timeMax=end,
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])
        enhanced_events = []

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))

            # 📍 Location
            location = event.get('location', 'N/A')

            # 👥 Attendees
            attendees_info = []
            for attendee in event.get('attendees', []):
                attendees_info.append({
                    "email": attendee.get('email'),
                    "displayName": attendee.get('displayName', 'N/A'),
                    "responseStatus": attendee.get('responseStatus'),
                    "organizer": attendee.get('organizer', False)
                })

            # 🔗 Meet Link
            hangout_link = event.get('hangoutLink', 'N/A')

            # 📎 Attachments
            attachments_info = []
            for attachment in event.get('attachments', []):
                attachments_info.append({
                    "title": attachment.get('title'),
                    "fileUrl": attachment.get('fileUrl')
                })

            # 📝 Description
            description = event.get('description', 'No description')

            enhanced_events.append({
                "📌 Title": event.get("summary", "No Title"),
                "🕒 Start": start,
                "🕓 End": end,
                "📍 Location": location,
                "👥 Attendees": attendees_info,
                "🔗 Meet Link": hangout_link,
                "📎 Attachments": attachments_info,
                "📝 Description": description
            })

        return enhanced_events

    except Exception as e:
        return [{"❌ Error": str(e)}]
    
def fetch_and_store_user_events(creds, user_email: str):
    events = get_upcoming_events(creds)
    db = SessionLocal()
    for event in events:
        event["event_id"] = str(event.get("id") or "")  # Needed for uniqueness and type safety
        store_event(db, user_email, event)
    db.close()
    return events