from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse, JSONResponse
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from config.settings import settings
from database.db import SessionLocal
from database.models import UserToken
from datetime import datetime, timedelta
from agents.calendar_agent.calendar_reader import get_upcoming_events
from sqlalchemy.orm import Session

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/userinfo.email",
    "openid"
]


def get_flow():
    return Flow.from_client_config(
        {
            "web": {
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [settings.GOOGLE_REDIRECT_URI]
            }
        },
        scopes=SCOPES,
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )

# FastAPI route to check authentication status
@router.get("/check")
def check_auth(request: Request):
    # You can improve this with session/cookie validation
    return {"authenticated": False}

# FastAPI route to check user existence
@router.post("/check-user")
def check_user(data: dict, db: Session = Depends(get_db)):
    email = data.get("email")
    if not email:
        return JSONResponse(status_code=400, content={"error": "Email required"})

    user = db.query(UserToken).filter_by(email=email).first()
    if user:
        token_valid = user.token_expiry and user.token_expiry > datetime.utcnow()
        return {
            "exists": True,
            "token_valid": token_valid
        }
    return {"exists": False, "token_valid": False}


# FastAPI route to initiate Google OAuth flow
@router.get("/google")
def auth_google():
    flow = get_flow()
    auth_url, _ = flow.authorization_url(access_type='offline', prompt='consent')
    return RedirectResponse(auth_url)


# FastAPI route to handle Google OAuth callback
@router.get("/callback")
def auth_callback(request: Request):
    code = request.query_params.get("code")
    flow = get_flow()
    flow.fetch_token(code=code)

    creds = flow.credentials

    # Get user email
    user_service = build("oauth2", "v2", credentials=creds)
    user_info = user_service.userinfo().get().execute()
    email = user_info.get("email")

    # Store or update tokens in DB
    db = SessionLocal()
    existing = db.query(UserToken).filter_by(email=email).first()
    if existing:
        setattr(existing, "access_token", creds.token)
        setattr(existing, "refresh_token", creds.refresh_token)
        setattr(existing, "token_expiry", creds.expiry)
    else:
        db.add(UserToken(
            email=email,
            access_token=creds.token,
            refresh_token=creds.refresh_token,
            token_expiry=creds.expiry
        ))
    db.commit()
    db.close()

    # Immediately extract upcoming calendar events (next 7 days)
    from google.oauth2.credentials import Credentials as OAuth2Credentials
    if not isinstance(creds, OAuth2Credentials):
        raise TypeError("Credentials object is not of type google.oauth2.credentials.Credentials")
    events = get_upcoming_events(creds)

    return JSONResponse({
        "message": f"🔐 Auth successful for {email}",
        "events": events
    })

