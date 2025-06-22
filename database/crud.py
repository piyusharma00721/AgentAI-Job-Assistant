# database/crud.py

from sqlalchemy.orm import Session
from database.models import CalendarEvent

def store_event(db: Session, user_email: str, event_data: dict):
    existing = db.query(CalendarEvent).filter_by(event_id=event_data["event_id"]).first()
    if not existing:
        db_event = CalendarEvent(
            user_email=user_email,
            event_id=event_data["event_id"],
            summary=event_data["summary"],
            description=event_data["description"],
            location=event_data["location"],
            start_time=event_data["start"],
            end_time=event_data["end"],
            organizer_email=event_data["organizer_email"],
            meeting_link=event_data["meeting_link"],
            attachments=event_data["attachments"],
            attendees=event_data["attendees"]
        )
        db.add(db_event)
        db.commit()
