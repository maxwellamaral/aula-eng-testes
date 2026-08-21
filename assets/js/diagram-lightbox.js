/**
 * Diagram & Image Lightbox for Quarto (HTML pages and RevealJS Slides)
 * Provides Fullscreen modal with Zoom In/Out, Pan (drag) and ESC to exit.
 */

(function () {
  'use strict';

  // Inject HTML template for Lightbox modal
  function createLightboxModal() {
    if (document.getElementById('diagram-lightbox-modal')) return;

    const modal = document.createElement('div');
    modal.id = 'diagram-lightbox-modal';
    modal.className = 'diagram-lightbox-overlay';
    modal.innerHTML = `
      <div class="diagram-lightbox-toolbar">
        <button id="dl-zoom-in" title="Aumentar Zoom (+)" class="dl-btn" type="button">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
        </button>
        <button id="dl-zoom-out" title="Diminuir Zoom (-)" class="dl-btn" type="button">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
        </button>
        <button id="dl-reset" title="Restaurar Tamanho Padrão (0)" class="dl-btn" type="button">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><polyline points="3 3 3 8 8 8"></polyline></svg>
        </button>
        <span class="dl-separator"></span>
        <button id="dl-close" title="Fechar (ESC)" class="dl-btn dl-btn-close" type="button">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
      <div class="diagram-lightbox-viewport" id="dl-viewport">
        <div class="diagram-lightbox-content" id="dl-content"></div>
      </div>
      <div class="diagram-lightbox-hint">
        <span>Arraste para mover (Pan) &bull; Roda do mouse para Zoom &bull; <strong>ESC</strong> para fechar</span>
      </div>
    `;

    document.body.appendChild(modal);
    initLightboxEvents(modal);
  }

  let currentScale = 1;
  let translateX = 0;
  let translateY = 0;
  let isDragging = false;
  let startX = 0;
  let startY = 0;

  function updateTransform() {
    const content = document.getElementById('dl-content');
    if (content) {
      content.style.transform = `translate(${translateX}px, ${translateY}px) scale(${currentScale})`;
    }
  }

  function resetTransform() {
    currentScale = 1;
    translateX = 0;
    translateY = 0;
    updateTransform();
  }

  function openLightbox(diagramElement) {
    createLightboxModal();
    const modal = document.getElementById('diagram-lightbox-modal');
    const content = document.getElementById('dl-content');
    if (!modal || !content) return;

    content.innerHTML = '';

    // Find actual image or svg
    let target = diagramElement;
    if (diagramElement.tagName.toLowerCase() !== 'img' && diagramElement.tagName.toLowerCase() !== 'svg') {
      const found = diagramElement.querySelector('svg, img');
      if (found) target = found;
    }

    if (target.tagName.toLowerCase() === 'img') {
      const img = document.createElement('img');
      img.src = target.src;
      img.alt = target.alt || 'Imagem / Diagrama';
      img.draggable = false;
      content.appendChild(img);
    } else if (target.tagName.toLowerCase() === 'svg') {
      const clone = target.cloneNode(true);
      
      // Preserve or calculate viewBox
      if (!clone.getAttribute('viewBox')) {
        const bcr = target.getBoundingClientRect();
        const w = parseFloat(target.getAttribute('width')) || bcr.width || 800;
        const h = parseFloat(target.getAttribute('height')) || bcr.height || 600;
        if (w > 0 && h > 0) {
          clone.setAttribute('viewBox', `0 0 ${w} ${h}`);
        }
      }
      
      // Remove inline sizing styles so CSS controls lightbox presentation
      clone.removeAttribute('style');
      clone.removeAttribute('width');
      clone.removeAttribute('height');
      clone.classList.add('dl-injected-svg');
      
      content.appendChild(clone);
    } else {
      content.innerHTML = target.innerHTML;
    }

    resetTransform();
    modal.classList.add('active');
    document.body.classList.add('diagram-lightbox-open');
  }

  function closeLightbox() {
    const modal = document.getElementById('diagram-lightbox-modal');
    if (modal && modal.classList.contains('active')) {
      modal.classList.remove('active');
      document.body.classList.remove('diagram-lightbox-open');
      const content = document.getElementById('dl-content');
      if (content) content.innerHTML = '';
    }
  }

  function initLightboxEvents(modal) {
    const viewport = document.getElementById('dl-viewport');
    const btnIn = document.getElementById('dl-zoom-in');
    const btnOut = document.getElementById('dl-zoom-out');
    const btnReset = document.getElementById('dl-reset');
    const btnClose = document.getElementById('dl-close');

    // Close button
    btnClose?.addEventListener('click', (e) => {
      e.stopPropagation();
      closeLightbox();
    });

    // Zoom buttons
    btnIn?.addEventListener('click', (e) => {
      e.stopPropagation();
      currentScale = Math.min(currentScale * 1.3, 10);
      updateTransform();
    });

    btnOut?.addEventListener('click', (e) => {
      e.stopPropagation();
      currentScale = Math.max(currentScale / 1.3, 0.2);
      updateTransform();
    });

    btnReset?.addEventListener('click', (e) => {
      e.stopPropagation();
      resetTransform();
    });

    // Keyboard navigation (ESC to close, + / - to zoom, 0 to reset) - capture phase
    window.addEventListener('keydown', (e) => {
      if (!modal.classList.contains('active')) return;
      if (e.key === 'Escape') {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        closeLightbox();
      } else if (e.key === '+' || e.key === '=') {
        e.preventDefault();
        e.stopPropagation();
        currentScale = Math.min(currentScale * 1.25, 10);
        updateTransform();
      } else if (e.key === '-' || e.key === '_') {
        e.preventDefault();
        e.stopPropagation();
        currentScale = Math.max(currentScale / 1.25, 0.2);
        updateTransform();
      } else if (e.key === '0') {
        e.preventDefault();
        e.stopPropagation();
        resetTransform();
      }
    }, true);

    // Mouse wheel zoom
    viewport?.addEventListener('wheel', (e) => {
      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 1.15 : 0.85;
      currentScale = Math.max(0.2, Math.min(currentScale * zoomFactor, 10));
      updateTransform();
    }, { passive: false });

    // Drag / Pan events
    viewport?.addEventListener('mousedown', (e) => {
      if (e.target.closest('.diagram-lightbox-toolbar')) return;
      isDragging = true;
      startX = e.clientX - translateX;
      startY = e.clientY - translateY;
      viewport.style.cursor = 'grabbing';
    });

    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      translateX = e.clientX - startX;
      translateY = e.clientY - startY;
      updateTransform();
    });

    window.addEventListener('mouseup', () => {
      isDragging = false;
      if (viewport) viewport.style.cursor = 'grab';
    });

    // Touch support (mobile pan)
    let touchStartX = 0;
    let touchStartY = 0;
    viewport?.addEventListener('touchstart', (e) => {
      if (e.touches.length === 1) {
        isDragging = true;
        touchStartX = e.touches[0].clientX - translateX;
        touchStartY = e.touches[0].clientY - translateY;
      }
    }, { passive: true });

    viewport?.addEventListener('touchmove', (e) => {
      if (!isDragging || e.touches.length !== 1) return;
      translateX = e.touches[0].clientX - touchStartX;
      translateY = e.touches[0].clientY - touchStartY;
      updateTransform();
    }, { passive: true });

    viewport?.addEventListener('touchend', () => {
      isDragging = false;
    });

    // Click on backdrop to close
    modal.addEventListener('click', (e) => {
      if (e.target === modal || e.target === viewport) {
        closeLightbox();
      }
    });
  }

  // Scan and attach click triggers to diagrams and slide images
  function attachDiagramTriggers() {
    // 1. Mermaid diagrams
    const mermaidContainers = document.querySelectorAll('.mermaid, pre.mermaid, div.cell-output-display figure, .cell-output-display');
    mermaidContainers.forEach((container) => {
      if (container.dataset.lightboxAttached) return;

      const svg = container.querySelector('svg');
      if (svg) {
        setupTrigger(container, svg);
      } else {
        const observer = new MutationObserver(() => {
          const loadedSvg = container.querySelector('svg');
          if (loadedSvg && !container.dataset.lightboxAttached) {
            setupTrigger(container, loadedSvg);
            observer.disconnect();
          }
        });
        observer.observe(container, { childList: true, subtree: true });
      }
    });

    // 2. PlantUML / SVG images / Markdown images in content
    const contentImgs = document.querySelectorAll('main.content img, #quarto-document-content img, .plantuml img, figure img, img[src*=".svg"], img[src*="mediabag"]');
    contentImgs.forEach((img) => {
      if (img.dataset.lightboxAttached) return;
      setupTrigger(img.parentElement.tagName.toLowerCase() === 'figure' ? img.parentElement : img, img);
    });

    // 3. RevealJS Slide Images and SVG elements
    const slideImgs = document.querySelectorAll('.reveal .slides section img, .reveal .slides section svg, .reveal .slides figure');
    slideImgs.forEach((el) => {
      if (el.dataset.lightboxAttached) return;
      const target = (el.tagName.toLowerCase() === 'figure') ? (el.querySelector('img, svg') || el) : el;
      setupTrigger(el, target);
    });
  }

  function setupTrigger(wrapper, targetElement) {
    wrapper.dataset.lightboxAttached = 'true';
    wrapper.classList.add('diagram-lightbox-target');

    // Add visual hint overlay / badge if not present
    if (!wrapper.querySelector('.dl-expand-badge')) {
      const badge = document.createElement('button');
      badge.className = 'dl-expand-badge';
      badge.type = 'button';
      badge.title = 'Visualizar em tela cheia com zoom e pan';
      badge.innerHTML = `
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <polyline points="15 3 21 3 21 9"></polyline>
          <polyline points="9 21 3 21 3 15"></polyline>
          <line x1="21" y1="3" x2="14" y2="10"></line>
          <line x1="3" y1="21" x2="10" y2="14"></line>
        </svg>
        <span>Expandir</span>
      `;
      badge.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        openLightbox(targetElement);
      });
      wrapper.style.position = 'relative';
      wrapper.appendChild(badge);
    }

    wrapper.addEventListener('click', (e) => {
      if (e.target.closest('a, button:not(.dl-expand-badge), pre, code')) return;
      openLightbox(targetElement);
    });
  }

  // Initialize on DOMContentLoaded and polling for dynamic elements / RevealJS
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      attachDiagramTriggers();
      setTimeout(attachDiagramTriggers, 500);
      setTimeout(attachDiagramTriggers, 1500);
    });
  } else {
    attachDiagramTriggers();
    setTimeout(attachDiagramTriggers, 500);
    setTimeout(attachDiagramTriggers, 1500);
  }

  // Quarto tab change & Reveal slide change listener
  document.addEventListener('click', (e) => {
    if (e.target.closest('.nav-link, .nav-item, .navigate-left, .navigate-right, .navigate-up, .navigate-down')) {
      setTimeout(attachDiagramTriggers, 200);
      setTimeout(attachDiagramTriggers, 600);
    }
  });

  // Reveal slidechanged event if Reveal is present
  if (typeof window !== 'undefined') {
    window.addEventListener('load', () => {
      if (window.Reveal) {
        window.Reveal.on('slidechanged', () => {
          setTimeout(attachDiagramTriggers, 100);
        });
        window.Reveal.on('ready', () => {
          setTimeout(attachDiagramTriggers, 100);
        });
      }
    });
  }

  // Export to window
  window.DiagramLightbox = {
    open: openLightbox,
    close: closeLightbox,
    scan: attachDiagramTriggers
  };
})();
