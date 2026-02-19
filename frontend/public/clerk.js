// Clerk JS loader for direct integration
(function() {
  if (window.Clerk) return;
  var script = document.createElement('script');
  script.src = 'https://cdn.clerk.dev/clerk.js';
  script.async = true;
  script.crossOrigin = 'anonymous';
  document.head.appendChild(script);
})();
