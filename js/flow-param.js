/**
 * Auto-detect the current flow and propagate ?flow=XX to all URLs.
 * - Reads flow from URL param or infers from directory path
 * - Updates the URL bar via history.replaceState (no reload)
 * - Adds ?flow=XX to all <a> links on the page
 * - Exposes window.flowHref(url) helper for JS navigations
 */
(function() {
  var params = new URLSearchParams(window.location.search);
  var flow = params.get('flow');

  if (!flow) {
    var path = window.location.pathname;
    if (/\/a2\//.test(path)) flow = 'a2';
    else if (/\/b1\//.test(path)) flow = 'b1';
    else if (/\/b2\//.test(path)) flow = 'b2';
    else if (/\/c1\//.test(path)) flow = 'c1';
    else if (/\/c2\//.test(path)) flow = 'c2';
    else if (/\/d1\//.test(path)) flow = 'd1';
    else if (/\/d2\//.test(path)) flow = 'd2';
    else if (/\/e1\//.test(path)) flow = 'e1';
    else if (/\/e2\//.test(path)) flow = 'e2';
    else if (/\/option-c\//.test(path)) flow = 'option-c';
    else if (/\/option-e\//.test(path)) flow = 'option-e';
    else if (/\/option-f\//.test(path)) flow = 'option-f';
  }

  if (!flow) return;

  window.__currentFlow = flow;

  if (!params.has('flow')) {
    try {
      var url = new URL(window.location.href);
      url.searchParams.set('flow', flow);
      history.replaceState(null, '', url.pathname + url.search + url.hash);
    } catch (e) {}
  }

  function appendFlow(href) {
    if (!href || href.charAt(0) === '#' || href.indexOf('javascript:') === 0 ||
        href.indexOf('mailto:') === 0 || href.indexOf('http') === 0 ||
        href.indexOf('flow=') !== -1) return href;
    var hash = '';
    var hashIdx = href.indexOf('#');
    if (hashIdx >= 0) { hash = href.substring(hashIdx); href = href.substring(0, hashIdx); }
    var sep = href.indexOf('?') >= 0 ? '&' : '?';
    return href + sep + 'flow=' + flow + hash;
  }

  window.flowHref = appendFlow;

  function processLinks() {
    var links = document.querySelectorAll('a[href]');
    for (var i = 0; i < links.length; i++) {
      var a = links[i];
      var href = a.getAttribute('href');
      if (!href || href.charAt(0) === '#' || href.indexOf('javascript:') === 0 ||
          href.indexOf('mailto:') === 0 || href.indexOf('http') === 0 ||
          href.indexOf('flow=') !== -1) continue;
      a.setAttribute('href', appendFlow(href));
    }
  }

  // "With cart" flows — inject cart icon on pages that don't have one
  var withCartFlows = { a2:1, b2:1, d2:1, e2:1, c2:1 };

  function injectCartIcon() {
    if (!withCartFlows[flow]) return;
    if (document.getElementById('nav-cart-link')) return;

    var navIcons = document.querySelector('.nav-icons');
    if (!navIcons) return;
    var menuBtn = navIcons.querySelector('[aria-label="Menu"], [aria-label="Open menu"]');
    if (!menuBtn) menuBtn = navIcons.lastElementChild;
    if (!menuBtn) return;

    // Derive base path prefix from this script's own src attribute
    var prefix = '';
    var fpScript = document.querySelector('script[src*="flow-param.js"]');
    if (fpScript) {
      var fpSrc = fpScript.getAttribute('src');
      var jsIdx = fpSrc.indexOf('js/flow-param.js');
      if (jsIdx > 0) prefix = fpSrc.substring(0, jsIdx);
    }

    var cartHref;
    if (flow === 'a2') cartHref = prefix + 'a2/cart.html';
    else if (flow === 'b2') cartHref = prefix + 'b2/cart.html';
    else cartHref = prefix + 'cart.html';

    var a = document.createElement('a');
    a.className = 'nav-icon-btn';
    a.id = 'nav-cart-link';
    a.href = appendFlow(cartHref);
    a.setAttribute('aria-label', 'Cart');
    a.innerHTML = '<svg viewBox="0 0 576 512" fill="currentColor"><path d="M24 0C10.7 0 0 10.7 0 24S10.7 48 24 48l45.5 0c3.8 0 7.1 2.7 7.9 6.5l51.6 271c6.5 34 36.2 58.5 70.7 58.5L488 384c13.3 0 24-10.7 24-24s-10.7-24-24-24l-288.3 0c-11.5 0-21.4-8.2-23.6-19.5L170.7 288l288.5 0c32.6 0 61.1-21.8 69.5-53.3l41-152.3C576.6 57 557.4 32 531.1 32l-411 0C111 12.8 91.6 0 69.5 0L24 0zM131.1 80l389.6 0L482.4 222.2c-2.8 10.5-12.3 17.8-23.2 17.8l-297.6 0L131.1 80zM176 512a48 48 0 1 0 0-96 48 48 0 1 0 0 96zm336-48a48 48 0 1 0 -96 0 48 48 0 1 0 96 0z"/></svg>';

    menuBtn.parentNode.insertBefore(a, menuBtn);
  }

  function init() {
    processLinks();
    injectCartIcon();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  var pending = null;
  var obs = new MutationObserver(function() {
    if (pending) return;
    pending = setTimeout(function() { pending = null; processLinks(); }, 50);
  });
  var target = document.body || document.documentElement;
  if (target) obs.observe(target, { childList: true, subtree: true });
  else document.addEventListener('DOMContentLoaded', function() {
    obs.observe(document.body, { childList: true, subtree: true });
  });
})();
