import { defineConfig } from 'astro/config';

// SITE_URL / SITE_BASE are set by the GitHub Actions workflow for the project page
// (https://<user>.github.io/<repo>/). Locally the site is served from "/".
const site = process.env.SITE_URL || 'http://localhost:4321';
const base = process.env.SITE_BASE || '/';

export default defineConfig({
  site,
  base,
  trailingSlash: 'always',
  build: { format: 'directory', inlineStylesheets: 'auto' },
  compressHTML: true,
  devToolbar: { enabled: false },
});
