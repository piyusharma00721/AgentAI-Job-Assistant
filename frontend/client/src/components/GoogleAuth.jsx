// src/components/GoogleAuth.jsx
import React from 'react';

const GoogleAuth = () => {
  const handleLogin = () => {
    window.location.href = 'http://localhost:8000/auth/google'; // backend OAuth URL
  };

  return (
    <div className="auth-container">
      <h2>🔐 Welcome to Agentic AI Job Assistant</h2>
      <p>Please sign in with Google to continue</p>
      <button onClick={handleLogin}>Sign in with Google</button>
    </div>
  );
};

export default GoogleAuth;
