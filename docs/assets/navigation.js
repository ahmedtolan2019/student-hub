/* Progressive enhancement only: all navigation and downloads work without JS. */
(() => {
  const sections = [...document.querySelectorAll('.week-card[id]')];
  const links = [...document.querySelectorAll('.toc-link')];
  const header = document.querySelector('.site-header');
  if (!sections.length || !links.length || !header) return;
  let scheduled = false;
  function update() {
    scheduled = false;
    const marker = header.getBoundingClientRect().bottom + 80;
    let current = sections[0];
    for (const section of sections) {
      if (section.getBoundingClientRect().top <= marker) current = section;
    }
    // A short final week can reach the bottom before crossing the header marker.
    if (window.scrollY > 0 && window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) {
      current = sections[sections.length - 1];
    }
    for (const link of links) {
      if (link.hash === '#' + current.id) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    }
  }
  function schedule() {
    if (!scheduled) { scheduled = true; window.requestAnimationFrame(update); }
  }
  window.addEventListener('scroll', schedule, { passive: true });
  window.addEventListener('resize', schedule, { passive: true });
  window.addEventListener('hashchange', schedule);
  window.addEventListener('load', schedule);
  if (document.fonts) document.fonts.ready.then(schedule);
  update();
})();
