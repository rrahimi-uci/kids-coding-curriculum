// Tiny progressive-enhancement script: phone menu drawer, display toggles, copy buttons.
const root = document.documentElement;
const store = {
  get(k) { try { return localStorage.getItem(k); } catch { return null; } },
  set(k, v) { try { localStorage.setItem(k, v); } catch { /* private mode: ignore */ } },
  del(k) { try { localStorage.removeItem(k); } catch { /* ignore */ } },
};

// ---- phone and tablet: the sidebar becomes a drawer opened from the top bar
const menuBtn = document.querySelector('.menu-btn');
const sidebar = document.getElementById('sidebar');
const scrim = document.querySelector('.scrim');
const closeBtn = sidebar?.querySelector('.close-btn');
const drawerMode = () => matchMedia('(max-width: 63.99rem)').matches;
function setNav(open, { focus = true } = {}) {
  document.body.classList.toggle('nav-open', open);
  menuBtn?.setAttribute('aria-expanded', String(open));
  if (scrim) scrim.hidden = !open;
  if (open && focus) closeBtn?.focus();
  else if (!open && focus) menuBtn?.focus();
}
menuBtn?.addEventListener('click', () => setNav(true));
closeBtn?.addEventListener('click', () => setNav(false));
scrim?.addEventListener('click', () => setNav(false));
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && document.body.classList.contains('nav-open')) setNav(false);
});
// Keep keyboard focus inside the open drawer.
sidebar?.addEventListener('keydown', (e) => {
  if (e.key !== 'Tab' || !drawerMode() || !document.body.classList.contains('nav-open')) return;
  const items = [...sidebar.querySelectorAll('a[href], button, input, summary')].filter((el) => el.offsetParent !== null);
  const first = items[0], last = items[items.length - 1];
  if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
  else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
});
matchMedia('(max-width: 63.99rem)').addEventListener('change', () => setNav(false, { focus: false }));
// Bring the current page into view in a long sidebar.
// (Scroll only the menu, never the page.)
const sideNav = sidebar?.querySelector('.side-nav');
const currentItem = sideNav?.querySelector('[aria-current="page"]');
if (currentItem && !drawerMode()) {
  const box = sideNav.getBoundingClientRect(), it = currentItem.getBoundingClientRect();
  if (it.bottom > box.bottom - 16) sideNav.scrollTop += it.top - box.top - box.height / 2;
}

// "On this page" is folded in the HTML (it sits above the text on narrow screens); on wide screens it has its own
// column on the right, so open it there. Opening it only adds content to that column, so nothing else moves.
if (matchMedia('(min-width: 90rem)').matches) document.querySelectorAll('.lesson-side .toc details').forEach((d) => { d.open = true; });

// ---- theme + font toggles
const themeBtn = document.getElementById('theme-toggle');
const fontBtn = document.getElementById('font-toggle');
const dark = () => root.getAttribute('data-theme') === 'dark' ||
  (!root.getAttribute('data-theme') && matchMedia('(prefers-color-scheme: dark)').matches);
function syncToggles() {
  if (themeBtn) themeBtn.setAttribute('aria-pressed', String(dark()));
  if (fontBtn) fontBtn.setAttribute('aria-pressed', String(root.getAttribute('data-font') === 'dyslexia'));
}
themeBtn?.addEventListener('click', () => {
  const next = dark() ? 'light' : 'dark';
  root.setAttribute('data-theme', next); store.set('kc:theme', next); syncToggles();
});
fontBtn?.addEventListener('click', () => {
  const on = root.getAttribute('data-font') === 'dyslexia';
  if (on) { root.removeAttribute('data-font'); store.del('kc:font'); }
  else { root.setAttribute('data-font', 'dyslexia'); store.set('kc:font', 'dyslexia'); }
  syncToggles();
});
syncToggles();

// ---- copy buttons on code blocks
document.querySelectorAll('.lesson .code-block, .starter-code').forEach((block) => {
  const pre = block.querySelector('pre');
  if (!pre || block.classList.contains('code-outputcode')) return;
  const btn = document.createElement('button');
  btn.type = 'button'; btn.className = 'btn small secondary copy-btn';
  btn.innerHTML = 'Copy<span class="visually-hidden"> code</span>';
  btn.addEventListener('click', async () => {
    const text = pre.innerText;
    try { await navigator.clipboard.writeText(text); } catch {
      const ta = document.createElement('textarea'); ta.value = text; document.body.appendChild(ta); ta.select();
      document.execCommand('copy'); ta.remove();
    }
    btn.textContent = 'Copied!'; setTimeout(() => { btn.innerHTML = 'Copy<span class="visually-hidden"> code</span>'; }, 1800);
  });
  block.appendChild(btn);
});
