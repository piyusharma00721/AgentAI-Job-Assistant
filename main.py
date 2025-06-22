# main.py
from agents.calendar_agent.calendar_reader import get_todays_events

if __name__ == "__main__":
    print("🔍 Checking today's calendar events...\n")
    events = get_todays_events()
    print(events)
