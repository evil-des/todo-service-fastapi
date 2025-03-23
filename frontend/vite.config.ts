import { fileURLToPath, URL } from 'node:url';

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import vueDevTools from 'vite-plugin-vue-devtools';
import svgLoader from 'vite-svg-loader';

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    svgLoader({
      defaultImport: 'component',
    }),
  ],
  server: {
    port: 3000,
    hmr: {
      path: '/ws/hmr',
    },
    allowedHosts: ['.clubox.io', 'host.docker.internal', '.mirbots.ru'],
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      '@utils': fileURLToPath(new URL('./src/shared/utils', import.meta.url)),
      '@layouts': fileURLToPath(new URL('./src/app/layouts', import.meta.url)),
      '@css': fileURLToPath(new URL('./src/app/css', import.meta.url)),
      '@icons': fileURLToPath(
        new URL('./src/shared/assets/icons', import.meta.url)
      ),
    },
  },
});
