(() => {
  const y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
  document.querySelectorAll('a[target="_blank"]').forEach(a => a.setAttribute('rel','noopener noreferrer'));
})();
