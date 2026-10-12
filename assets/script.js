(() => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.site-nav');
  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());
  if (!toggle || !nav) return;
  document.documentElement.classList.add('nav-ready');
  const close = () => {
    nav.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open navigation');
  };
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', close));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav.classList.contains('is-open')) {
      close();
      toggle.focus();
    }
  });
  document.addEventListener('click', event => { if (!nav.contains(event.target) && !toggle.contains(event.target)) close(); });
  window.matchMedia('(max-width: 800px)').addEventListener('change', close);
})();

(() => {
  const image = document.getElementById('lidar-animation');
  const button = document.getElementById('animation-toggle');
  if (!image || !button) return;
  const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const setPaused = paused => {
    const source = paused ? image.dataset.stillSource : image.dataset.animationSource;
    if (image.getAttribute('src') !== source) image.setAttribute('src', source);
    image.alt = paused
      ? 'Still frame of predicted plant organ segmentation from a 3D LiDAR point cloud'
      : 'Animated visualization of predicted plant organ segmentation from a 3D LiDAR point cloud';
    button.setAttribute('aria-pressed', String(paused));
    button.textContent = paused ? 'Play LiDAR animation' : 'Pause LiDAR animation';
  };
  button.hidden = false;
  setPaused(motionPreference.matches);
  button.addEventListener('click', () => setPaused(button.getAttribute('aria-pressed') !== 'true'));
  motionPreference.addEventListener('change', event => setPaused(event.matches));
})();
