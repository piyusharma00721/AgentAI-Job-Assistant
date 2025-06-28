# database/models.py
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from .db import Base

Base = declarative_base()

class UserToken(Base):
    __tablename__ = "user_credentials"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    access_token = Column(String, nullable=False)
    refresh_token = Column(String, nullable=True)
    token_expiry = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)


class CalendarEvent(Base):
    __tablename__ = "calendar_events"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, index=True)
    event_id = Column(String, unique=True, index=True)
    summary = Column(String)
    description = Column(Text)
    location = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    organizer_email = Column(String)
    meeting_link = Column(String)
    attachments = Column(Text)
    attendees = Column(Text) 