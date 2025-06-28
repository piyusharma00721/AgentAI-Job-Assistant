# main.py
from agents.calendar_agent.calendar_reader import get_upcoming_events

if __name__ == "__main__":
    print("🔍 Checking today's calendar events...\n")
    events = get_upcoming_events()
    print(events)
