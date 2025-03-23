/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,vue}'],
  theme: {
    extend: {
      spacing: {
        'safe-top':
          'calc(var(--tg-safe-area-inset-top) + var(--tg-content-safe-area-inset-top))',
        'safe-bottom':
          'calc(var(--tg-safe-area-inset-bottom) + var(--tg-content-safe-area-inset-bottom))',
      },
      maxWidth: {
        'web-app': '28rem',
        'sticker': '13.75rem',
      },
      minWidth: {
        'sticker': '10.9rem',
      },
      width: {
        'sticker': '13.75rem',
        'sticker-sm': '10.9rem',
      },
      height: {
        'sticker': '13.75rem',
        'sticker-sm': '10.9rem',
      }
    },
  },
  plugins: [require('tailwindcss-primeui'), require('tailwindcss-animated')],
};
