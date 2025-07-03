// frontend/client/src/pages/Auth.jsx

import React, { useState } from 'react';
import axios from 'axios';

const Auth = () => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (e) => {
  e.preventDefault();
  try {
    const response = await axios.post('http://localhost:8000/auth/check-user', {
      email: email.toLowerCase(),

    });

    console.log('Response:', response.data);

    if (response.data.exists) {
      // Save name for home page usage (optional - we can also fetch on /home)
      localStorage.setItem('user_email', email);
      window.location.href = '/home';
    } else {
      setError('User not found. Please register.');
    }
  } catch (err) {
    console.error('Error:', err.response?.data || err.message);
    if (err.response?.status === 404) {
      setError('User not found. Please register.');
    } else {
      setError(err.response?.data?.message || 'Error checking user. Please try again.');
    }
  }
};


  const handleRegister = async () => {
    try {
      window.location.href = 'http://localhost:8000/auth/google?first_name=' + encodeURIComponent(firstName) + '&last_name=' + encodeURIComponent(lastName) + '&email=' + encodeURIComponent(email);
    } catch (err) {
      setError('Registration failed. Please try again.');
    }
  };

  return (
      <div className="min-h-screen flex items-center justify-center p-4" style={{ background: 'linear-gradient(to bottom right, black 0%, black 8%,rgb(170, 0, 255) 60%,rgb(181, 120, 177) 100%)' }}>
      <div className="bg-white bg-opacity-15 backdrop-blur-xl p-8 rounded-3xl shadow-[inset_0_4px_6px_rgba(255,255,255,0.3),inset_0_-4px_6px_rgba(255,255,255,0.3),inset_4px_0_6px_rgba(255,255,255,0.3),inset_-4px_0_6px_rgba(255,255,255,0.3)] max-w-md w-full border border-gradient-to-br from-pink-300 to-transparent">
        <h2 className="text-2xl font-bold text-white mb-6 text-center">
          👋 Welcome to Agentic AI Job Assistant
        </h2>
        {error && (
          <div className="text-red-500 mb-4 bg-red-500 bg-opacity-20 p-2 rounded-md text-center">
            {error}
          </div>
        )}
        <form onSubmit={handleLogin}>
          <div className="mb-4 flex space-x-4">
            <div className="w-1/2">
              <label className="text-white mb-2 block"></label>
              <input
                type="text"
                placeholder="First Name"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                className="w-full p-2 rounded-md bg-white bg-opacity-10 text-white border border-white-300 focus:outline-none focus:border-pink-200"
                required
              />
            </div>
            <div className="w-1/2">
              <label className="text-white mb-2 block"></label>
              <input
                type="text"
                placeholder="Last Name"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                className="w-full p-2 rounded-md bg-white bg-opacity-10 text-white border border-white-300 focus:outline-none focus:border-pink-200"
                required
              />
            </div>
          </div>
          <div className="mb-4">
            <label className="text-white mb-2 block"></label>
            <input
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full p-2 rounded-md bg-white bg-opacity-10 text-white border border-white-300 focus:outline-none focus:border-pink-200"
              required
            />
          </div>
           <div className="flex space-x-4">
            <button
              type="submit"
              className="w-1/2 bg-white text-black bg-opacity-80 hover:bg-opacity-100 py-2 rounded-md"
            >
            🔒 Login
            </button>
            <button
              type="button"
              onClick={handleRegister}
              className="w-1/2 bg-white text-black bg-opacity-80 hover:bg-opacity-100 py-2 rounded-md"
            >
            🛅 Register
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Auth;










// import React, { useState } from "react";
// import axios from "axios";

// const Auth = () => {
//   const [email, setEmail] = useState("");

// const handleLogin = async () => {
//   if (!email) return alert("Please enter your email");

//   try {
//     const res = await axios.post("http://localhost:8000/auth/check-user", { email });
//     const { exists, token_valid } = res.data;

//     if (exists && token_valid) {
//       // Don't go to OAuth — directly load calendar
//       localStorage.setItem("user_email", email);
//       window.location.href = "/calendar";
//     } else {
//       // Go to OAuth only if new or expired
//       window.location.href = "http://localhost:8000/auth/google";
//     }
//   } catch (err) {
//     console.error("Login check failed", err);
//   }
// };


//   const handleRegister = () => {
//     window.location.href = "http://localhost:8000/auth/google";
//   };

//   return (
//     <div style={styles.container}>
//       <div className="shadow-inset p-4 bg-white rounded-lg" style={styles.glassCard}>
//         <h1 style={styles.title}>👋 Welcome to Agentic AI Job Assistant</h1>
//         <input
//           type="email"
//           placeholder="Enter your email"
//           value={email}
//           onChange={(e) => setEmail(e.target.value)}
//           style={styles.input}
//         />
//         <div style={styles.buttonGroup}>
//           <button onClick={handleLogin} style={styles.loginBtn}>🔐 Login</button>
//           <button onClick={handleRegister} style={styles.registerBtn}>🆕 Register</button>
//         </div>
//       </div>
//     </div>
//   );
// };

// const styles = {
//   container: {
//     height: "100vh",
//     background: "linear-gradient(135deg,rgb(63, 7, 230),rgb(230, 7, 111),rgb(234, 8, 46),rgb(233, 6, 6),rgb(207, 213, 10)",
//     display: "flex",
//     justifyContent: "center",
//     alignItems: "center",
//     fontFamily: "Arial, sans-serif"
//   },
//   glassCard: {
//     background: "rgba(255, 255, 255, 0.22)",
//     boxShadow: " rgba(255, 131, 131, 0.38)",
//     backdropFilter: "blur(12px)",
//     borderRadius: "16px",
//     padding: "40px",
//     width: "90%",
//     maxWidth: "400px",
//     textAlign: "center",
//     color: "#fff"
//   },
//   title: {
//     fontSize: "1.5rem",
//     marginBottom: "20px",
//     fontWeight: "bold"
//   },
//   input: {
//     color: "#ffffff",
//     background: "rgba(238, 210, 255, 0.49)",   

//     padding: "10px",
//     width: "95%",
//     borderRadius: "8px",
//     border: "none",
//     marginBottom: "20px",
//     fontSize: "1rem"
//   },
//   buttonGroup: {
//     display: "flex",
//     justifyContent: "space-between"
//   },
//   loginBtn: {
//     background: "rgba(255, 255, 255, 0.7)",
//     color: "#1f1f1f",
//     padding: "10px 20px",
//     border: "none",
//     borderRadius: "8px",
//     cursor: "pointer",
//     fontWeight: "bold"
//   },
//   registerBtn: {
//     background:"rgba(255, 255, 255, 0.7)",
//     color: "#1f1f1f",
//     padding: "10px 20px",
//     border: "None",
//     borderRadius: "8px",
//     cursor: "pointer",
//     fontWeight: "bold"
//   }
// };

// export default Auth;
