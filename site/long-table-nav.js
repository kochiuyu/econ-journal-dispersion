/* Keep the semantic table intact; the floating header is a pointer-only mirror. */
(() => {
  'use strict';
  const wrap = document.querySelector('.tbl-wrap');
  const table = wrap?.querySelector('table');
  const head = table?.tHead;
  const controls = document.querySelector('.controls');
  const pager = document.getElementById('pager');
  if (!head || !controls || !pager) return;

  document.body.classList.add('long-table-page');
  const pinned = document.createElement('div');
  pinned.className = 'pinned-heading';
  pinned.setAttribute('aria-hidden', 'true');
  pinned.hidden = true;
  const mirror = document.createElement('table');
  mirror.className = table.className;
  pinned.append(mirror);
  document.body.append(pinned);

  const makeReturn = className => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = className;
    button.textContent = 'Back to filters';
    button.setAttribute('aria-controls', 'filters');
    button.addEventListener('click', () => {
      pinned.hidden = true;
      const search = document.getElementById('q');
      if (search && !search.disabled) search.focus({ preventScroll: true });
      else {
        controls.tabIndex = -1;
        controls.focus({ preventScroll: true });
      }
      controls.scrollIntoView({ block: 'start', behavior: 'instant' });
      schedule();
    });
    return button;
  };
  pager.append(makeReturn('btn table-return'));
  const back = makeReturn('btn long-return');
  back.hidden = true;
  document.body.append(back);

  let pending = false;
  let dirty = true;
  const revealHead = () => {
    pinned.hidden = true;
    head.scrollIntoView({ block: 'start', behavior: 'instant' });
  };
  const rebuild = () => {
    const clone = head.cloneNode(true);
    clone.querySelectorAll('[id]').forEach(el => el.removeAttribute('id'));
    const originals = [...head.querySelectorAll('button')];
    clone.querySelectorAll('button').forEach((button, index) => {
      button.tabIndex = -1;
      button.addEventListener('mousedown', event => event.preventDefault());
      button.addEventListener('click', () => {
        originals[index].click();
        originals[index].focus({ preventScroll: true });
        revealHead();
      });
    });
    mirror.replaceChildren(clone);
    dirty = false;
  };
  function update() {
    pending = false;
    back.hidden = controls.getBoundingClientRect().bottom >= 0 && document.activeElement !== back;
    const rect = table.getBoundingClientRect();
    const header = head.getBoundingClientRect();
    if (!header.height || header.top >= -1 || rect.bottom <= 0) {
      pinned.hidden = true;
      return;
    }
    if (dirty) rebuild();
    const bounds = wrap.getBoundingClientRect();
    pinned.style.left = bounds.left + 'px';
    pinned.style.width = bounds.width + 'px';
    mirror.style.width = rect.width + 'px';
    const cells = [...head.querySelectorAll('th')];
    mirror.querySelectorAll('th').forEach((cell, index) => {
      const width = cells[index].getBoundingClientRect().width;
      cell.style.display = width ? 'table-cell' : 'none';
      cell.style.width = width + 'px';
    });
    pinned.hidden = false;
    pinned.style.top = Math.min(0, rect.bottom - pinned.offsetHeight) + 'px';
    pinned.scrollLeft = wrap.scrollLeft;
  }
  function schedule() {
    if (!pending) { pending = true; requestAnimationFrame(update); }
  }
  window.addEventListener('scroll', schedule, { passive: true });
  window.addEventListener('resize', schedule, { passive: true });
  wrap.addEventListener('scroll', schedule, { passive: true });
  pinned.addEventListener('scroll', () => {
    if (Math.abs(wrap.scrollLeft - pinned.scrollLeft) > 1) wrap.scrollLeft = pinned.scrollLeft;
  }, { passive: true });
  back.addEventListener('blur', schedule);
  const resize = new ResizeObserver(schedule);
  [table, wrap, ...head.querySelectorAll('th')].forEach(el => resize.observe(el));
  new MutationObserver(() => { dirty = true; schedule(); }).observe(head, {
    subtree: true, childList: true, attributes: true,
    attributeFilter: ['aria-sort', 'aria-label', 'hidden']
  });
  document.addEventListener('focusin', event => {
    if (head.contains(event.target)) { revealHead(); return; }
    requestAnimationFrame(() => {
      if (pinned.contains(event.target) || !event.target.getBoundingClientRect) return;
      const target = event.target.getBoundingClientRect();
      const top = pinned.hidden ? 0 : pinned.getBoundingClientRect().bottom;
      if (target.top >= 0 && target.top < top) window.scrollBy(0, target.top - top - 8);
      const button = back.getBoundingClientRect();
      if (!back.hidden && event.target !== back && target.bottom > button.top && target.top < button.bottom && target.right > button.left && target.left < button.right) {
        window.scrollBy(0, target.bottom - button.top + 8);
      }
    });
  });
  schedule();
})();
