import * as params from '@params';

const search = document.querySelector('[data-search-index]');
const input = document.getElementById('searchInput');
const results = document.getElementById('article-search-results');
const status = document.getElementById('search-status');
let searchIndex;
let revision = 0;

function loadSearch() {
    if (!searchIndex) {
        searchIndex = fetch(search.dataset.searchIndex)
            .then(response => {
                if (!response.ok) throw new Error('Search index unavailable');
                return response.json();
            })
            .then(index => index.map(item => ({
                ...item,
                slug: new URL(item.permalink, document.baseURI).pathname.split('/').filter(Boolean).pop()?.replaceAll('-', ' '),
            })))
            .then(index => new Fuse(index, {
                keys: params.fuseOpts.keys,
                threshold: params.fuseOpts.threshold,
                ignoreLocation: true,
            }))
            .catch(error => {
                searchIndex = undefined;
                throw error;
            });
    }
    return searchIndex;
}

function resultCard({ title, permalink, description, readingTime }) {
    const card = document.createElement('li');
    card.className = 'post-entry';

    const heading = document.createElement('h2');
    const link = document.createElement('a');
    link.href = permalink;
    link.textContent = title;
    heading.append(link);

    const copy = document.createElement('p');
    copy.textContent = description;
    card.append(heading, copy);

    if (readingTime) {
        const meta = document.createElement('p');
        meta.className = 'search-reading-time';
        meta.textContent = readingTime + ' min read';
        card.append(meta);
    }
    return card;
}

async function updateResults() {
    const request = ++revision;
    const query = input.value.trim();

    if (!query) {
        results.replaceChildren();
        status.textContent = '';
        return;
    }

    if (!searchIndex) status.textContent = 'Loading search…';

    try {
        const fuse = await loadSearch();
        if (request !== revision) return;

        const matches = fuse.search(query);
        results.replaceChildren(...matches.map(({ item }) => resultCard(item)));
        status.textContent = matches.length === 1 ? '1 result' :
            matches.length ? matches.length + ' results' : 'No results found.';
    } catch {
        if (request !== revision) return;
        results.replaceChildren();
        status.textContent = 'Search is unavailable. Try again in a moment.';
    }
}

input.addEventListener('input', updateResults);
input.addEventListener('search', updateResults);

search.addEventListener('keydown', event => {
    const active = document.activeElement;
    if (event.key === 'Escape') {
        event.preventDefault();
        input.value = '';
        updateResults();
        input.focus();
        return;
    }

    const card = active.closest('.post-entry');
    if (event.key === 'ArrowDown') {
        const next = active === input ? results.firstElementChild : card?.nextElementSibling;
        if (next) {
            event.preventDefault();
            next.querySelector('a').focus();
        }
    } else if (event.key === 'ArrowUp' && card) {
        event.preventDefault();
        (card.previousElementSibling?.querySelector('a') ?? input).focus();
    } else if (event.key === 'ArrowRight' && card) {
        active.click();
    }
});
