// Minimal static server for the built site; mounts dist/ under SITE_BASE (default "/").
import { createServer } from 'node:http';
import fs from 'node:fs';
import path from 'node:path';

const types = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.mjs': 'text/javascript', '.svg': 'image/svg+xml',
  '.webp': 'image/webp', '.woff2': 'font/woff2', '.pdf': 'application/pdf', '.json': 'application/json', '.zip': 'application/zip', '.py': 'text/plain',
  '.txt': 'text/plain', '.pf_meta': 'application/octet-stream', '.pf_index': 'application/octet-stream', '.pf_fragment': 'application/octet-stream', '.pagefind': 'application/octet-stream', '.wasm': 'application/wasm' };

export function serve(dist, port = 0, base = process.env.SITE_BASE || '/') {
  base = base.endsWith('/') ? base : base + '/';
  const server = createServer((req, res) => {
    let p = decodeURIComponent(req.url.split('?')[0]);
    if (!p.startsWith(base)) { res.writeHead(404); return res.end('outside base'); }
    p = '/' + p.slice(base.length);
    if (p.endsWith('/')) p += 'index.html';
    let f = path.join(dist, p);
    if (!fs.existsSync(f) && fs.existsSync(f + '/index.html')) { res.writeHead(301, { location: req.url + '/' }); return res.end(); }
    if (!fs.existsSync(f)) { res.writeHead(404, { 'content-type': 'text/html' }); return res.end(fs.existsSync(path.join(dist, '404.html')) ? fs.readFileSync(path.join(dist, '404.html')) : 'not found'); }
    res.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream', 'cache-control': 'max-age=3600' });
    fs.createReadStream(f).pipe(res);
  });
  return new Promise((resolve) => server.listen(port, '127.0.0.1', () => resolve({ server, url: `http://127.0.0.1:${server.address().port}${base}`, port: server.address().port })));
}

export function pagesIn(dist) {
  const out = [];
  const walk = (d) => { for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const f = path.join(d, e.name);
    if (e.isDirectory()) { if (e.name !== 'pagefind' && e.name !== '_astro' && e.name !== 'downloads' && e.name !== 'generated') walk(f); }
    // Pages that only forward the browser to a moved page (meta refresh) are left out: the target is checked.
    else if ((e.name === 'index.html' || e.name === '404.html') && !/http-equiv="refresh"/.test(fs.readFileSync(f, 'utf8')))
      out.push('/' + path.relative(dist, f).replace(/index\.html$/, '').replace(/\\/g, '/'));
  } };
  walk(dist);
  return out.sort();
}
