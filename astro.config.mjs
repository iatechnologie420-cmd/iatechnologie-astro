import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://iatechnologie.com',
  integrations: [
    tailwind(),
  ],
  build: {
    format: 'file',
  },
});
