const motion = window.matchMedia('(prefers-reduced-motion: no-preference)');

function play(target) {
    if (!target || !motion.matches) return;
    target.classList.remove('is-playing');
    // Read layout so a repeated interaction can restart the CSS animation.
    target.getBoundingClientRect();
    target.classList.add('is-playing');
}

const logo = document.querySelector('.site-logo');
const logoVisual = logo.querySelector('.logo-visual');
play(logoVisual);
for (const event of ['pointerenter', 'pointerdown', 'focus']) {
    logo.addEventListener(event, () => play(logoVisual));
}

const topics = document.querySelector('.home-topics');
topics?.addEventListener('change', event => play(event.target.nextElementSibling));
topics?.addEventListener('click', event => {
    const label = event.target.closest('label');
    if (label?.control?.checked) play(label);
});

const letter = document.querySelector('[data-home-letter]');
if (letter) {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = letter.className;
    button.setAttribute('aria-label', 'Open the letter');
    button.append(...letter.childNodes);
    letter.replaceWith(button);

    function syncMotion() {
        button.disabled = !motion.matches;
    }

    button.addEventListener('click', () => play(button));
    document.querySelector('.home-newsletter form').addEventListener('submit', () => play(button), true);
    motion.addEventListener('change', syncMotion);
    syncMotion();
}
