/** @type {import('tailwindcss').Config} */
const colors = require("tailwindcss/colors")


module.exports = {
  content: ["./zeus/**/*.{html,js}"],
  theme: {
    colors:colors,
    extend: {},
  },
  plugins: [],
};
