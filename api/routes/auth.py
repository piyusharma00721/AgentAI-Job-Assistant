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
import os
from pydantic import BaseModel

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
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

class LoginRequest(BaseModel):
    email: str
# FastAPI route to check user existence
@router.post("/check-user")
def check_user(payload: LoginRequest, db: Session = Depends(get_db)):
    email = payload.email.lower()


    user = db.query(UserToken).filter_by(email=email).first()
    print(user)
    if user:
        token_valid = user.token_expiry and user.token_expiry > datetime.utcnow()
        return {
            "exists": True,
            "token_valid": token_valid,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
    return {"exists": False, "token_valid": False}


# FastAPI route to initiate Google OAuth flow
@router.get("/google")
def auth_google(first_name: str, last_name: str, email: str):
    flow = get_flow()
    # Custom state to carry name+email through OAuth redirect
    state = f"{first_name}|{last_name}|{email.lower()}"
    auth_url, _ = flow.authorization_url(
        access_type='offline',
        prompt='consent',
        state=state  # inject user info
    )
    return RedirectResponse(auth_url)


# FastAPI route to handle Google OAuth callback
@router.get("/callback")
def auth_callback(request: Request):
    code = request.query_params.get("code")
    state = request.query_params.get("state")  # 🧠 get custom user info
    print("💡 Received STATE:", state)  # 👈 add this

    # fallback
    first_name = last_name = ""
    email = ""

    if state:
        try:
            first_name, last_name, email = state.split("|")
        except ValueError:
            pass

    flow = get_flow()
    flow.fetch_token(authorization_response=str(request.url))
    creds = flow.credentials

    # override email from Google's token
    user_service = build("oauth2", "v2", credentials=creds)
    user_info = user_service.userinfo().get().execute()
    google_email = user_info.get("email")
    email = google_email or email  # prefer Google's

    db = SessionLocal()
    existing = db.query(UserToken).filter_by(email=email.lower()).first()

    if existing:
        setattr(existing, "access_token", creds.token)
        setattr(existing, "refresh_token", creds.refresh_token)
        setattr(existing, "token_expiry", creds.expiry)
        if first_name:
            setattr(existing, "first_name", first_name)
        if last_name:
            setattr(existing, "last_name", last_name)
    else:
        db.add(UserToken(
            email=email.lower(),
            first_name=first_name,
            last_name=last_name,
            access_token=creds.token,
            refresh_token=creds.refresh_token,
            token_expiry=creds.expiry
        ))
    db.commit()
    db.close()  

    return RedirectResponse(
    url=f"http://localhost:3000/home?email={email}&first_name={first_name}"
    )








# from fastapi import APIRouter, Request, Depends
# from fastapi.responses import RedirectResponse, JSONResponse
# from google_auth_oauthlib.flow import Flow
# from googleapiclient.discovery import build
# from config.settings import settings
# from database.db import SessionLocal
# from database.models import UserToken
# from datetime import datetime, timedelta
# from agents.calendar_agent.calendar_reader import get_upcoming_events
# from sqlalchemy.orm import Session

# router = APIRouter()

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# SCOPES = [
#     "https://www.googleapis.com/auth/calendar.readonly",
#     "https://www.googleapis.com/auth/userinfo.email",
#     "openid"
# ]


# def get_flow():
#     return Flow.from_client_config(
#         {
#             "web": {
#                 "client_id": settings.GOOGLE_CLIENT_ID,
#                 "client_secret": settings.GOOGLE_CLIENT_SECRET,
#                 "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#                 "token_uri": "https://oauth2.googleapis.com/token",
#                 "redirect_uris": [settings.GOOGLE_REDIRECT_URI]
#             }
#         },
#         scopes=SCOPES,
#         redirect_uri=settings.GOOGLE_REDIRECT_URI
#     )

# # FastAPI route to check authentication status
# @router.get("/check")
# def check_auth(request: Request):
#     # You can improve this with session/cookie validation
#     return {"authenticated": False}

# # FastAPI route to check user existence
# @router.post("/check-user")
# def check_user(data: dict, db: Session = Depends(get_db)):
#     email = data.get("email")
#     if not email:
#         return JSONResponse(status_code=400, content={"error": "Email required"})

#     user = db.query(UserToken).filter_by(email=email).first()
#     if user:
#         token_valid = user.token_expiry and user.token_expiry > datetime.utcnow()
#         return {
#             "exists": True,
#             "token_valid": token_valid
#         }
#     return {"exists": False, "token_valid": False}


# # FastAPI route to initiate Google OAuth flow
# @router.get("/google")
# def auth_google():
#     flow = get_flow()
#     auth_url, _ = flow.authorization_url(access_type='offline', prompt='consent')
#     return RedirectResponse(auth_url)


# # FastAPI route to handle Google OAuth callback
# @router.get("/callback")
# def auth_callback(request: Request):
#     code = request.query_params.get("code")
#     flow = get_flow()
#     flow.fetch_token(code=code)

#     creds = flow.credentials

#     # Get user email
#     user_service = build("oauth2", "v2", credentials=creds)
#     user_info = user_service.userinfo().get().execute()
#     email = user_info.get("email")

#     # Store or update tokens in DB
#     db = SessionLocal()
#     existing = db.query(UserToken).filter_by(email=email).first()
#     if existing:
#         setattr(existing, "access_token", creds.token)
#         setattr(existing, "refresh_token", creds.refresh_token)
#         setattr(existing, "token_expiry", creds.expiry)
#     else:
#         db.add(UserToken(
#             email=email,
#             access_token=creds.token,
#             refresh_token=creds.refresh_token,
#             token_expiry=creds.expiry
#         ))
#     db.commit()
#     db.close()

#     # Immediately extract upcoming calendar events (next 7 days)
#     from google.oauth2.credentials import Credentials as OAuth2Credentials
#     if not isinstance(creds, OAuth2Credentials):
#         raise TypeError("Credentials object is not of type google.oauth2.credentials.Credentials")
#     events = get_upcoming_events(creds)

#     return JSONResponse({
#         "message": f"🔐 Auth successful for {email}",
#         "events": events
#     })

