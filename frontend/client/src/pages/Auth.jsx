// frontend/client/src/pages/Auth.jsx

import React, { useState } from "react";
import axios from "axios";

const Auth = () => {
  const [email, setEmail] = useState("");

const handleLogin = async () => {
  if (!email) return alert("Please enter your email");

  try {
    const res = await axios.post("http://localhost:8000/auth/check-user", { email });
    const { exists, token_valid } = res.data;

    if (exists && token_valid) {
      // Don't go to OAuth — directly load calendar
      localStorage.setItem("user_email", email);
      window.location.href = "/calendar";
    } else {
      // Go to OAuth only if new or expired
      window.location.href = "http://localhost:8000/auth/google";
    }
  } catch (err) {
    console.error("Login check failed", err);
  }
};


  const handleRegister = () => {
    window.location.href = "http://localhost:8000/auth/google";
  };

  return (
    <div style={styles.container}>
      <div style={styles.glassCard}>
        <h1 style={styles.title}>👋 Welcome to Agentic AI Job Assistant</h1>
        <input
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          style={styles.input}
        />
        <div style={styles.buttonGroup}>
          <button onClick={handleLogin} style={styles.loginBtn}>🔐 Login</button>
          <button onClick={handleRegister} style={styles.registerBtn}>🆕 Register</button>
        </div>
      </div>
    </div>
  );
};

const styles = {
  container: {
    height: "100vh",
    background: "linear-gradient(135deg,rgb(63, 7, 230),rgb(230, 7, 111),rgb(234, 8, 46),rgb(233, 6, 6),rgb(207, 213, 10)",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    fontFamily: "Arial, sans-serif"
  },
  glassCard: {
    background: "rgba(255, 255, 255, 0.22)",
    boxShadow: " rgba(255, 131, 131, 0.38)",
    backdropFilter: "blur(12px)",
    borderRadius: "16px",
    padding: "40px",
    width: "90%",
    maxWidth: "400px",
    textAlign: "center",
    color: "#fff"
  },
  title: {
    fontSize: "1.5rem",
    marginBottom: "20px",
    fontWeight: "bold"
  },
  input: {
    color: "#ffffff",
    background: "rgba(238, 210, 255, 0.49)",   
    color: "#ffffff",
    padding: "10px",
    width: "95%",
    borderRadius: "8px",
    border: "none",
    marginBottom: "20px",
    fontSize: "1rem"
  },
  buttonGroup: {
    display: "flex",
    justifyContent: "space-between"
  },
  loginBtn: {
    background: "rgba(255, 255, 255, 0.7)",
    color: "#1f1f1f",
    padding: "10px 20px",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
    fontWeight: "bold"
  },
  registerBtn: {
    background:"rgba(255, 255, 255, 0.7)",
    color: "#1f1f1f",
    padding: "10px 20px",
    border: "None",
    borderRadius: "8px",
    cursor: "pointer",
    fontWeight: "bold"
  }
};

export default Auth;
