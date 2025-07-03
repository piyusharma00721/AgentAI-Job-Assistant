# database/models.py
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from .db import Base
from sqlalchemy.sql import func

Base = declarative_base()

class UserToken(Base):
    __tablename__ = "user_credentials"

    email = Column(String, primary_key=True, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    access_token = Column(String)
    refresh_token = Column(String)
    token_expiry = Column(DateTime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
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