/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './portfolioapp/templates/**/*.html',
     './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {
      fontFamily:{
        sans:["Playfair Display", 'serif'],
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
],
}

