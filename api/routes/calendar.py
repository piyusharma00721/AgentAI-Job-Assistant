# api/routes/calendar.py

from fastapi import APIRouter, HTTPException, Query, Depends
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from database.db import SessionLocal
from database.models import UserToken
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import CalendarEvent

router = APIRouter()

@router.get("/events")
def get_user_calendar_events(email: str = Query(..., description="User's Gmail address")):
    db = SessionLocal()
    user = db.query(UserToken).filter_by(email=email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not authorized or token not found.")

    # Construct credentials from stored tokens
    creds = Credentials(
        token=user.access_token,
        refresh_token=user.refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id="YOUR_CLIENT_ID",               # Optional if using .env flow
        client_secret="YOUR_CLIENT_SECRET",       # Optional if using .env flow
        scopes=["https://www.googleapis.com/auth/calendar.readonly"]
    )

    service = build("calendar", "v3", credentials=creds)

    now = datetime.utcnow().isoformat() + "Z"
    end = (datetime.utcnow().replace(hour=23, minute=59, second=59)).isoformat() + "Z"

    events_result = service.events().list(
        calendarId="primary",
        timeMin=now,
        timeMax=end,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])
    if not events:
        return {"message": "No events for today."}

    event_data = []
    for event in events:
        event_data.append({
            "summary": event.get("summary", "No Title"),
            "start": event["start"].get("dateTime", event["start"].get("date")),
            "location": event.get("location", "No Location")
        })

    return {"events": event_data}

@router.get("/calendar/events")
def get_events(db: Session = Depends(get_db)):
    return db.query(CalendarEvent).order_by(CalendarEvent.start_time).all()
