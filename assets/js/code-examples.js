/** Abre os exemplos completos incluídos no deck, sem requisições de rede. */
(function () {
  'use strict';

  function init() {
    const dialog = document.getElementById('code-examples-dialog');
    if (!dialog) return;
    const select = document.getElementById('code-examples-select');
    const content = document.getElementById('code-examples-content');
    let trigger = null;
    let fontSize = 16;

    function showExample(id) {
      const template = document.getElementById(id);
      if (!template || template.tagName !== 'TEMPLATE') return false;
      content.replaceChildren(template.content.cloneNode(true));
      select.value = id;
      content.scrollTop = 0;
      content.scrollLeft = 0;
      return true;
    }

    document.addEventListener('click', (event) => {
      const link = event.target.closest('[data-code-example]');
      if (!link) return;
      // Impede também o preview-links do Reveal.js de abrir outro overlay.
      event.preventDefault();
      event.stopImmediatePropagation();
      if (!showExample(link.dataset.codeExample)) return;
      trigger = link;
      dialog.showModal();
      select.focus();
    }, true);

    select.addEventListener('change', () => showExample(select.value));
    dialog.addEventListener('click', (event) => {
      const action = event.target.closest('[data-code-action]')?.dataset.codeAction;
      if (action === 'close') dialog.close();
      if (action === 'expand') {
        const expanded = dialog.classList.toggle('expanded');
        const button = event.target.closest('button');
        button.setAttribute('aria-pressed', String(expanded));
        button.textContent = expanded ? 'Restaurar janela' : 'Expandir janela';
      }
      if (action === 'larger' || action === 'smaller') {
        fontSize = Math.max(12, Math.min(30, fontSize + (action === 'larger' ? 2 : -2)));
        content.style.fontSize = `${fontSize}px`;
      }
      if (event.target === dialog) {
        const rect = dialog.getBoundingClientRect();
        if (event.clientX < rect.left || event.clientX > rect.right ||
            event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
      }
    });
    dialog.addEventListener('close', () => trigger?.focus());

    // Não deixar atalhos do deck avançarem slides enquanto se lê o código.
    window.addEventListener('keydown', (event) => {
      if (!dialog.open) return;
      event.stopImmediatePropagation();
      if (event.key === 'Escape') {
        event.preventDefault();
        dialog.close();
      }
    }, true);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
