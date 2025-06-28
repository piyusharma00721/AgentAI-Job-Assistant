// frontend/client/src/components/GoogleAuthButton.js
import React from "react";

const GoogleAuthButton = () => {
  const handleLogin = () => {
    window.location.href = "http://localhost:8000/auth/google"; // FastAPI OAuth route
  };

  return (
    <div style={styles.container}>
      <h2>Welcome to Agentic AI Job Assistant</h2>
      <button style={styles.button} onClick={handleLogin}>
        Sign in with Google
      </button>
    </div>
  );
};

const styles = {
  container: {
    display: "flex",
    height: "100vh",
    alignItems: "center",
    justifyContent: "center",
    flexDirection: "column",
    backgroundColor: "#f4f4f4",
    fontFamily: "Arial, sans-serif",
  },
  button: {
    padding: "10px 20px",
    fontSize: "16px",
    borderRadius: "5px",
    backgroundColor: "#4285F4",
    color: "#fff",
    border: "none",
    cursor: "pointer",
  },
};

export default GoogleAuthButton;
