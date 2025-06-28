import React, { useEffect, useState } from "react";

const CalendarEvents = () => {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);

  const email = "sharmapiyush1106@gmail.com"; // 🔄 Replace with dynamic email in future

useEffect(() => {
  fetch(`http://localhost:8000/calendar/events?email=${email}`)
    .then((res) => res.json())
    .then((data) => {
      console.log("Fetched data from API:", data); // 🐛 Debug
      if (Array.isArray(data)) {
        setEvents(data);
      } else {
        console.error("Expected array but got:", data);
        setEvents([]);
      }
      setLoading(false);
    })
    .catch((err) => {
      console.error("Error fetching events:", err);
      setLoading(false);
    });
}, []);
;

  if (loading) return <p>⏳ Loading your events...</p>;
  if (events.length === 0) return <p>📭 No events found</p>;

  return (
    <div>
      <h2>📅 Upcoming Events</h2>
      <ul>
        {events.map((event, index) => (
          <li key={index} style={{ marginBottom: "1rem" }}>
            <strong>{event.summary}</strong> <br />
            🕒 {event.start} → {event.end} <br />
            📍 {event.location || "N/A"} <br />
            👥 Attendees:{" "}
            {event.attendees?.length
              ? event.attendees.map((a) => a.email).join(", ")
              : "None"}
            <br />
            🔗 Meeting Link:{" "}
            {event.meeting_link ? (
              <a href={event.meeting_link}>Join</a>
            ) : (
              "N/A"
            )}
            <br />
            📎 Description: {event.description || "No description"}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CalendarEvents;
