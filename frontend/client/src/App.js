// frontend/client/src/App.js

import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// Pages
import Auth from "./pages/Auth";
import Home from "./pages/Home";

// Optional: move these to pages if needed
import CalendarEvents from "./components/CalendarEvents";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Auth />} />
        <Route path="/home" element={<Home />} />
        <Route path="/calendar" element={<CalendarEvents />} />
      </Routes>
    </Router>
  );
}

export default App;
