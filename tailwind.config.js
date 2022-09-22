/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.{html,jinja2}"],
  theme: {
    colors: {
      brand: "#162d50",
      dark: "#1C2541",
      mid: "#3A506B",
      light: "#FEFEFE",
      igtie: {
        '50': '#f3f5f6',
        '100': '#e8eaee',
        '200': '#c5cbd3',
        '300': '#a2abb9',
        '400': '#5c6c85',
        '500': '#162d50',
        '600': '#142948',
        '700': '#11223c',
        '800': '#0d1b30',
        '900': '#0b1627'
        },
      stone: {
        '50': '#f4f4f6',
        '100': '#e8e9ec',
        '200': '#c6c9d0',
        '300': '#a4a8b3',
        '400': '#60667a',
        '500': '#1C2541',
        '600': '#19213b',
        '700': '#151c31',
        '800': '#111627',
        '900': '#0e1220'
      },
    green: {
        '50': '#f7fcfc',
        '100': '#eff9f9',
        '200': '#d6efef',
        '300': '#bde6e5',
        '400': '#8cd3d2',
        '500': '#5BC0BE',
        '600': '#52adab',
        '700': '#44908f',
        '800': '#377372',
        '900': '#2d5e5d'
      }
    },
    extend: {
      fontFamily: {
        'kano': ['Kano', 'sans-serif'],
        'alcu': ['Alcubierre', 'sans-serif'],
        'muller': ['Muller', 'sans-serif'],
      },
      screens: {
        'md': '800px',
      },
    },
  },
  plugins: [],
}


