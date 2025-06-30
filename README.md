
# 🧠 AgentAI Job Assistant  
**Empower your career search with autonomous AI agents.**  
An intelligent job assistant that organises, applies, schedules, and prepares — so you don’t have to.

---

## 📂 Repository Structure

This repo is modular and scalable, designed with clean separation of concerns for agents, APIs, databases, and orchestration:

```plaintext
AgentAI-Job-Assistant/
│
├── agents/                # Autonomous agent logic (e.g., Calendar, Email, Job Tracker)
│   └── calendar_agent/    # Currently active agent fetching daily events
│
├── api/                   # FastAPI backend
│   ├── main.py            # Entry point for FastAPI app
│   └── routes/            # Route handlers
│       ├── auth.py        # Google OAuth2 authentication
│       └── calendar.py    # Calendar event-fetching endpoints
│
├── config/                # Environment variables, API keys, and settings
│   └── settings.py
│
├── core/                  # Centralized orchestrator & schedulers (agent coordination)
│   └── orchestrator.py
│
├── database/              # PostgreSQL ORM models and DB utility
│   ├── db.py              # DB connection
│   ├── models.py          # SQLAlchemy user/token models
│   └── crud.py            # DB read/write logic
│
├── llm_engine/            # LLM utilities (future: JD parsing, resume matching, etc.)
├── vectorstore/           # FAISS or Pinecone integration for retrieval tasks
├── requirements.txt       # Dependencies
├── .env                   # Environment config (excluded from version control)
└── README.md              # This file
```

---

## 🚨 Problem Statement

In today’s hyper-competitive job market:

- Candidates juggle between applications, emails, and calendars.
- Missed interviews and disorganized follow-ups kill opportunities.
- Manual job tracking and resume tailoring are overwhelming and inefficient.

**What if your job hunt worked *for you*, not the other way around?**

---

## ✅ Our Solution

Introducing **AgentAI Job Assistant** — a fully autonomous, agent-powered backend system that helps you stay organized, professional, and always one step ahead.

### 💡 Key Features (in progress & upcoming):

| Feature                        | Status     | Description |
|-------------------------------|------------|-------------|
| 🔐 Google OAuth Login         | ✅ Done     | Secure login and calendar access |
| 📅 Calendar Agent             | ✅ Done     | Fetches your events daily |
| 🧠 LLM-Powered Job Agent      | 🛠 Building | Extracts job skills, matches resume with JD |
| 💌 Email Agent                | 🛠 Next     | Reads recruiter emails, drafts replies |
| 📊 ATS Tracker                | 🔜 Planned  | Tracks application statuses per platform |
| 🗓️ Interview Scheduler Agent | 🔜 Planned  | Auto-blocks time slots, sends reminders |
| 📥 Resume Analyzer            | 🔜 Planned  | Vectorizes resumes and JD for precise match |
| 🚀 Notifications              | 🛠 Soon     | Telegram/email reminders based on schedule |

---

## 🧠 Tech Stack

| Area             | Tech Used |
|------------------|-----------|
| Backend          | FastAPI, PostgreSQL, SQLAlchemy |
| OAuth & APIs     | Google OAuth2, Google Calendar API |
| Agents Framework | LangChain, CrewAI (planned) |
| LLMs             | OpenAI/Gemini APIs (for resume-JD analysis) |
| Frontend         | React (in progress) |
| Vector Store     | FAISS, Pinecone (planned) |
| Deployment       | Render, Railway, GitHub Actions (planned) |

---

## 🚀 Getting Started

### 🔧 Requirements

```bash
python>=3.9
PostgreSQL
```

### 📦 Installation

```bash
git clone https://github.com/piyusharma00721/AgentAI-Job-Assistant.git
cd AgentAI-Job-Assistant
pip install -r requirements.txt
```

### ⚙️ Setup

1. Create a `.env` file:

```ini
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/callback
DATABASE_URL=postgresql://username:password@localhost:5432/agentai
```

2. Run FastAPI:

```bash
uvicorn api.main:app --reload
```

3. Visit:  
   [http://localhost:8000/auth/google](http://localhost:8000/auth/google)

---

We’re actively building! Contributions are **welcome**:

- Build new agents (email, job tracker)
- Enhance LLM resume analysis
- UI/UX feedback for frontend
- Testing, logging, or deployment improvements

📬 Open an issue or PR to start contributing!

---

🎯 Tired of missing deadlines, managing job portals, and forgetting interviews?

💡 Let **AgentAI Job Assistant** streamline your job search while you focus on being your best self.

👉 **Star this repo** ⭐  
👉 **Fork it** 🍴  
👉 **Use it** 🚀  
👉 **Join the mission** to build your ultimate career co-pilot!  
> This is just the beginning — and **you can be a part of it.**
