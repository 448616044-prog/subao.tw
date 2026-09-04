(function() {
  if (document.getElementById('lineFloatBtn')) return;

  var btn = document.createElement('a');
  btn.id = 'lineFloatBtn';
  btn.href = 'https://line.me/R/ti/p/@734dooky';
  btn.target = '_blank';
  btn.rel = 'noopener';
  btn.title = 'LINE 免費估價';
  btn.setAttribute('aria-label', 'LINE 免費估價');

  btn.innerHTML = '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">'
    + '<path d="M19.38 10.38c0-3.73-3.74-6.76-8.38-6.76S2.62 6.65 2.62 10.38c0 3.34 2.96 6.14 6.98 6.67.27.06.64.18.73.41.08.2.05.52.03.72 0 0-.1.6-.12.72-.04.24-.19.94.82.51 1.01-.43 5.45-3.21 7.43-5.5 1.37-1.5 1.89-2.8 1.89-4.53z" fill="#fff"/>'
    + '<path d="M15.11 12.52h.01c.32 0 .57-.26.57-.58a.57.57 0 00-.57-.58H8.89a.57.57 0 00-.57.58c0 .32.26.58.57.58h6.22zm-3.08 2.44h.01c.33 0 .57-.26.57-.58a.57.57 0 00-.57-.58H8.89a.57.57 0 00-.57.58c0 .32.26.58.57.58h3.14z" fill="#06C755"/>'
    + '</svg>';

  var style = document.createElement('style');
  style.textContent = [
    '#lineFloatBtn {',
    '  position: fixed; bottom: 24px; left: 16px; right: auto; z-index: 9999;',
    '  width: 48px; height: 48px; border-radius: 50%;',
    '  background: #06C755; box-shadow: 0 4px 16px rgba(6,199,85,0.4);',
    '  display: flex; align-items: center; justify-content: center;',
    '  cursor: pointer; transition: transform 0.2s, box-shadow 0.2s;',
    '  animation: lineFloatPulse 2s ease-in-out infinite;',
    '  text-decoration: none; -webkit-tap-highlight-color: transparent;',
    '}',
    '#lineFloatBtn:hover { transform: scale(1.1); box-shadow: 0 6px 24px rgba(6,199,85,0.55); }',
    '#lineFloatBtn:active { transform: scale(0.95); }',
    '@keyframes lineFloatPulse {',
    '  0%, 100% { box-shadow: 0 4px 16px rgba(6,199,85,0.4); }',
    '  50% { box-shadow: 0 4px 24px rgba(6,199,85,0.7); }',
    '}',
    '@media (min-width: 769px) {',
    '  #lineFloatBtn { left: auto; right: 32px; bottom: 32px; width: 60px; height: 60px; }',
    '}'
  ].join('\n');

  document.head.appendChild(style);
  document.body.appendChild(btn);
})();
