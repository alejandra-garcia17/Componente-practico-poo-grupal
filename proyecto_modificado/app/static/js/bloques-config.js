/* =====================================================
   BLOQUES-CONFIG.JS — Configuración central de bloques
   =====================================================
   Para agregar un bloque nuevo:
   1. Agrégalo al nivel que corresponde (EASY, MID o HARD).
   2. Agrégalo a ALL_BLOCKS en el orden correcto.
   Nada más. Todo lo demás es automático.
   ===================================================== */

(function () {

    // ── CONFIGURACIÓN DE NIVELES ──────────────────────
    const EASY_BLOCKS = [1, 2, 3, 4, 5, 6, 7];
    const MID_BLOCKS  = [8, 9, 10, 11, 12, 13, 14];
    const HARD_BLOCKS = [15, 16, 17, 18, 19,20];

    // Orden de navegación (anterior / siguiente)
    const ALL_BLOCKS  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19];

    // Claves de localStorage
    const KEY_EASY = 'poo_completed_easy';
    const KEY_MID  = 'poo_completed_mid';
    const KEY_HARD = 'poo_completed_hard';

    // ── LEER BLOQUE ACTUAL ────────────────────────────
    const pathMatch    = window.location.pathname.match(/\/bloque(\d+)/);
    const currentBlock = pathMatch ? parseInt(pathMatch[1]) : 0;

    // ── LEER COMPLETADOS ─────────────────────────────
    const completedEasy = JSON.parse(localStorage.getItem(KEY_EASY) || '[]');
    const completedMid  = JSON.parse(localStorage.getItem(KEY_MID)  || '[]');
    const completedHard = JSON.parse(localStorage.getItem(KEY_HARD) || '[]');

    const allEasyDone = EASY_BLOCKS.every(b => completedEasy.includes(b));
    const allMidDone  = MID_BLOCKS.every(b => completedMid.includes(b));

    // ── HELPERS ───────────────────────────────────────
    function isLevelBlocked(n) {
        if (!n) return false;
        if (MID_BLOCKS.includes(n)  && !allEasyDone) return true;
        if (HARD_BLOCKS.includes(n) && !allMidDone)  return true;
        return false;
    }

    function arrowLeft() {
        return `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>`;
    }
    function arrowRight() {
        return `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>`;
    }
    function homeIcon() {
        return `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12L12 3l9 9"/><path d="M9 21V12h6v9"/></svg>`;
    }
    function checkIcon() {
        return `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>`;
    }

    // ── BLOQUEAR SIDEBAR ──────────────────────────────
    document.querySelectorAll('.sidebar a').forEach(a => {
        const href = a.getAttribute('href') || '';
        const m    = href.match(/\/bloque(\d+)/);
        if (!m) return;
        const n = parseInt(m[1]);

        if (isLevelBlocked(n)) {
            a.setAttribute('data-locked', 'true');
            a.removeAttribute('href');
        }

        // Marcar completados en sidebar con un tick
        const isDone = (EASY_BLOCKS.includes(n) && completedEasy.includes(n)) ||
                       (MID_BLOCKS.includes(n)  && completedMid.includes(n))  ||
                       (HARD_BLOCKS.includes(n) && completedHard.includes(n));
        if (isDone) a.setAttribute('data-done', 'true');
    });

    // ── BANNER DE BLOQUE BLOQUEADO (acceso directo URL) ──
    const blocked = isLevelBlocked(currentBlock);
    if (blocked) {
        let nivel, pending, keyNeeded;
        if (MID_BLOCKS.includes(currentBlock)) {
            nivel      = 'Intermedio';
            pending    = EASY_BLOCKS.filter(b => !completedEasy.includes(b));
            keyNeeded  = 'Básico';
        } else {
            nivel      = 'Avanzado';
            pending    = MID_BLOCKS.filter(b => !completedMid.includes(b));
            keyNeeded  = 'Intermedio';
        }

        const banner = document.createElement('div');
        banner.className   = 'bloque-locked-banner';
        banner.style.display = 'block';
        banner.innerHTML = `
            <span class="lock-icon">🔒</span>
            <h3>Nivel ${nivel} bloqueado</h3>
            <p>Debes completar todos los bloques de <strong>Nivel ${keyNeeded}</strong> antes de continuar.<br>
               Te faltan: ${pending.map(b => 'Bloque ' + b).join(', ')}</p>
            <a href="/bloque${pending[0]}">Ir al Bloque ${pending[0]}</a>
        `;
        const main = document.querySelector('.contenido');
        if (main) main.prepend(banner);
        return; // no renderizar nav en bloque bloqueado
    }

    // ── BOTÓN "MARCAR COMO COMPLETADO" ───────────────
    if (currentBlock !== 0) {
        const isEasy = EASY_BLOCKS.includes(currentBlock);
        const isMid  = MID_BLOCKS.includes(currentBlock);
        const isHard = HARD_BLOCKS.includes(currentBlock);

        const alreadyDone = (isEasy && completedEasy.includes(currentBlock)) ||
                            (isMid  && completedMid.includes(currentBlock))  ||
                            (isHard && completedHard.includes(currentBlock));

        const btnComplete = document.createElement('button');
        btnComplete.className = alreadyDone ? 'btn-complete btn-complete-done' : 'btn-complete';
        btnComplete.innerHTML = alreadyDone
            ? `${checkIcon()} Bloque completado`
            : `${checkIcon()} Marcar como completado`;

        btnComplete.addEventListener('click', function () {
            if (isEasy) {
                if (!completedEasy.includes(currentBlock)) {
                    completedEasy.push(currentBlock);
                    localStorage.setItem(KEY_EASY, JSON.stringify(completedEasy));
                }
            } else if (isMid) {
                if (!completedMid.includes(currentBlock)) {
                    completedMid.push(currentBlock);
                    localStorage.setItem(KEY_MID, JSON.stringify(completedMid));
                }
            } else if (isHard) {
                if (!completedHard.includes(currentBlock)) {
                    completedHard.push(currentBlock);
                    localStorage.setItem(KEY_HARD, JSON.stringify(completedHard));
                }
            }
            btnComplete.className = 'btn-complete btn-complete-done';
            btnComplete.innerHTML = `${checkIcon()} Bloque completado`;

            // Refrescar sidebar sin recargar página
            document.querySelectorAll('.sidebar a').forEach(a => {
                const href = a.getAttribute('href') || '';
                const m = href.match(/\/bloque(\d+)/);
                if (m && parseInt(m[1]) === currentBlock) {
                    a.setAttribute('data-done', 'true');
                }
            });
        });

        const bloque = document.querySelector('.bloque');
        if (bloque) bloque.appendChild(btnComplete);
    }

    // ── BOTONES DE NAVEGACIÓN ─────────────────────────
    const idx = ALL_BLOCKS.indexOf(currentBlock);
    if (idx === -1) return;

    const prevNum = idx > 0 ? ALL_BLOCKS[idx - 1] : null;
    const nextNum = idx < ALL_BLOCKS.length - 1 ? ALL_BLOCKS[idx + 1] : null;

    const nav = document.createElement('div');
    nav.className = 'bloque-nav';

    // Botón anterior
    if (prevNum) {
        const locked = isLevelBlocked(prevNum);
        nav.innerHTML += `
            <a class="btn-nav btn-nav-prev${locked ? '" data-locked="true' : ''}"
               href="${locked ? '#' : '/bloque' + prevNum}">
                ${arrowLeft()} Bloque ${prevNum}
            </a>`;
    } else {
        nav.innerHTML += `<a class="btn-nav btn-nav-prev" href="/">${homeIcon()} Inicio</a>`;
    }

    // Indicador de progreso
    nav.innerHTML += `<span class="nav-progress">Bloque ${currentBlock} / ${ALL_BLOCKS.length}</span>`;

    // Botón siguiente
    if (nextNum) {
        const locked = isLevelBlocked(nextNum);
        nav.innerHTML += `
            <a class="btn-nav btn-nav-next${locked ? '" data-locked="true' : ''}"
               href="${locked ? '#' : '/bloque' + nextNum}">
                Bloque ${nextNum} ${arrowRight()}
            </a>`;
    } else {
        nav.innerHTML += `<a class="btn-nav btn-nav-next" href="/">Inicio ${homeIcon()}</a>`;
    }

    const bloque = document.querySelector('.bloque');
    if (bloque) bloque.appendChild(nav);

})();
