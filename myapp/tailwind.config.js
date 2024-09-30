/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html'],
  theme: {
    extend: {
      fontFamily: {
        asananew: ['"Asana New"', 'sans-serif'],
        charm: ['Charm', 'sans-serif'], // Charm font
        sarabun: ['Sarabun', 'sans-serif'], // Adding Sarabun font
        mitr: ['Mitr', 'sans-serif'],       // Adding Mitr font
        prompt: ['Prompt', 'sans-serif'],   // Adding Prompt font
      },
    },
  },
  plugins: [],
}
