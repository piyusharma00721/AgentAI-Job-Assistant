from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import auth, calendar

app = FastAPI(title="Agentic AI Job Assistant")

# Optional: CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["OAuth"])
app.include_router(calendar.router, prefix="/calendar", tags=["Calendar"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # if using Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)