import React from 'react';
import { useLocation } from 'react-router-dom';

const Home = () => {
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const firstName = params.get('first_name') || 'User';

  return (
    <div className="min-h-screen bg-gradient-to-br from-black via-purple-800 to-pink-300 text-white relative flex flex-col">
      
      {/* Brand Header */}
      <header className="text-center text-3xl font-bold mt-6">
        Agentic AI Job Assistant
      </header>

      {/* Separator line below brand name */}
      <div className="mx-auto mt-2 w-2/3 border-t border-white border-opacity-40"></div>

      {/* Top Right User Info */}
      <div className="absolute top-4 right-6 flex items-center space-x-2">
        <span className="text-sm sm:text-md">👋 Hello, {firstName}</span>
        <img
          src="https://i.pravatar.cc/40"
          alt="User"
          className="rounded-full w-8 h-8 border border-white"
        />
      </div>

      {/* Centered Boxes Section */}
      <div className="flex-grow flex justify-center items-center">
        <div className="flex flex-col sm:flex-row gap-8 mt-6">
          
          {/* Shared Box Styles */}
          {[
            {
              title: '📅 Calendar Check',
              description: 'View your upcoming interviews, deadlines, and meetings — all in one place.',
              button: 'View Events',
            },
            {
              title: '📧 Gmail Check',
              description: 'Instantly scan recruiter emails, job alerts, and responses from HR.',
              button: 'Read Mails',
            },
            {
              title: '🧠 Chat with AI Mentor',
              description: 'Get career guidance, interview prep, or ask anything — powered by AI.',
              button: 'Start Chat',
            },
          ].map((item, index) => (
            <div
              key={index}
              className="bg-white bg-opacity-15 backdrop-blur-xl p-6 rounded-2xl text-center shadow-[inset_0_4px_6px_rgba(255,255,255,0.3),inset_0_-4px_6px_rgba(255,255,255,0.3),inset_4px_0_6px_rgba(255,255,255,0.3),inset_-4px_0_6px_rgba(255,255,255,0.3)] border border-white border-opacity-20 w-72 h-72 flex flex-col justify-between"
            >
              <div>
                <h3 className="text-xl font-semibold mb-2">{item.title}</h3>
                <p className="text-sm">{item.description}</p>
              </div>
              <button className="mt-4 bg-white text-black bg-opacity-80 hover:bg-opacity-100 px-4 py-2 rounded-md">
                {item.button}
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Home;
