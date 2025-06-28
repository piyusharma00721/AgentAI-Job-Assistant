/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}"
  ],
  theme: {
    extend: {
      boxShadow: {
        'inset': 'inset 0 2px 5px rgba(251, 251, 251, 0.95)',
      }
    },
  },
  plugins: [],
}
