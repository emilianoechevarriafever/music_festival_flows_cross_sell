/**
 * Desktop gallery layout for plan-view pages.
 * On screens >= 1024px, replaces the mobile carousel with a
 * Fever-style split gallery: large main media (left 60%) +
 * 2×2 thumbnail grid (right 40%) + Gallery button.
 *
 * Works for both static carousel (polar-sound pages) and pages
 * where the carousel is built dynamically (plan.html, etc.).
 */
(function () {
  if (window.innerWidth < 1024) return;

  function buildGallery() {
    var heroEl = document.querySelector('.detail-layout .hero');
    if (!heroEl || heroEl.dataset.galleryBuilt) return;

    /* ── Collect media from carousel slides ──────────────────── */
    var mediaItems = [];
    var carouselSlides = heroEl.querySelectorAll('.carousel-slide:not(.clone-slide)');

    carouselSlides.forEach(function (slide) {
      var vid = slide.querySelector('video');
      var img = slide.querySelector('img');
      if (vid) {
        var src = vid.getAttribute('src') || vid.src;
        var poster = vid.getAttribute('poster') || vid.poster || '';
        if (src) mediaItems.push({ type: 'video', src: src, poster: poster });
      } else if (img) {
        var src = img.getAttribute('src') || img.src;
        if (src) mediaItems.push({ type: 'image', src: src, alt: img.alt || '' });
      }
    });

    /* Fallback: non-carousel hero (e.g. accommodation hero-bg) */
    if (mediaItems.length === 0) {
      var vid = heroEl.querySelector('video.hero-bg, video');
      var img = heroEl.querySelector('img.hero-bg, img');
      if (vid) {
        var src = vid.getAttribute('src') || vid.src;
        mediaItems.push({ type: 'video', src: src, poster: vid.getAttribute('poster') || '' });
      }
      if (img) {
        var src = img.getAttribute('src') || img.src;
        mediaItems.push({ type: 'image', src: src, alt: img.alt || '' });
      }
    }

    if (mediaItems.length < 1) return;

    heroEl.dataset.galleryBuilt = '1';

    /* ── Build HTML ──────────────────────────────────────────── */
    var mainItem = mediaItems[0];
    var thumbItems = mediaItems.slice(1, 5);

    /* Pad thumbnails with first item's poster/src if fewer than 4 */
    while (thumbItems.length < 4) {
      var fallback = mediaItems[Math.min(thumbItems.length + 1, mediaItems.length - 1)];
      thumbItems.push(fallback || mainItem);
    }

    /* Main left media */
    var mainMediaHTML;
    if (mainItem.type === 'video') {
      mainMediaHTML = '<video src="' + mainItem.src + '"'
        + (mainItem.poster ? ' poster="' + mainItem.poster + '"' : '')
        + ' autoplay muted playsinline loop style="width:100%;height:100%;object-fit:cover;display:block;"></video>';
    } else {
      mainMediaHTML = '<img src="' + mainItem.src + '" alt="' + (mainItem.alt || '') + '" style="width:100%;height:100%;object-fit:cover;display:block;">';
    }

    /* Side buttons (like / share) — clone from hero if present */
    var sideBtnsEl = heroEl.querySelector('.side-buttons');
    var sideBtnsHTML = sideBtnsEl ? sideBtnsEl.outerHTML : '';

    /* Thumbnails */
    var thumbsHTML = thumbItems.map(function (item) {
      if (item.type === 'video') {
        return '<div class="hgd-thumb"><img src="' + (item.poster || item.src) + '" alt="" style="width:100%;height:100%;object-fit:cover;display:block;"></div>';
      }
      return '<div class="hgd-thumb"><img src="' + item.src + '" alt="' + (item.alt || '') + '" style="width:100%;height:100%;object-fit:cover;display:block;"></div>';
    }).join('');

    /* Gallery button icon (4-squares) */
    var galleryIconSVG = '<svg viewBox="0 0 16 16" fill="currentColor" width="16" height="16" aria-hidden="true"><rect x="0" y="0" width="6.5" height="6.5" rx="1"/><rect x="9.5" y="0" width="6.5" height="6.5" rx="1"/><rect x="0" y="9.5" width="6.5" height="6.5" rx="1"/><rect x="9.5" y="9.5" width="6.5" height="6.5" rx="1"/></svg>';

    var galleryHTML =
      '<div class="hero-gallery-desktop" role="region" aria-label="Event gallery">' +
        '<div class="hgd-main">' +
          mainMediaHTML +
          sideBtnsHTML +
        '</div>' +
        '<div class="hgd-grid">' +
          thumbsHTML +
          '<button type="button" class="hgd-gallery-btn gallery-btn">' +
            galleryIconSVG + ' Gallery' +
          '</button>' +
        '</div>' +
      '</div>';

    heroEl.insertAdjacentHTML('beforebegin', galleryHTML);
    heroEl.classList.add('hgd-hidden-carousel');

    var galleryDesktop = heroEl.previousElementSibling;

    /* ── Wire up clicks to open fullscreen gallery ───────────── */
    var originalGalleryBtn = heroEl.querySelector('.gallery-btn');

    function openGallery(idx) {
      if (originalGalleryBtn) {
        originalGalleryBtn.click();
        /* Navigate to the correct slide index after gallery opens */
        if (idx > 0) {
          setTimeout(function () {
            var fsNext = document.getElementById('fsGalleryNext');
            for (var i = 0; i < idx; i++) {
              if (fsNext) fsNext.click();
            }
          }, 80);
        }
      }
    }

    galleryDesktop.querySelector('.hgd-main').addEventListener('click', function () { openGallery(0); });
    galleryDesktop.querySelector('.hgd-gallery-btn').addEventListener('click', function (e) { e.stopPropagation(); openGallery(0); });

    galleryDesktop.querySelectorAll('.hgd-thumb').forEach(function (thumb, i) {
      thumb.addEventListener('click', function () { openGallery(i + 1); });
    });
  }

  /* Run now (for static carousels) and after a tick (for dynamic carousels) */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      buildGallery();
      setTimeout(buildGallery, 300);
    });
  } else {
    buildGallery();
    setTimeout(buildGallery, 300);
  }
})();
