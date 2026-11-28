// Weekly letter signup (layouts/partials/newsletter.html).
// Submits the form to Kit in place and shows the success message. Served from this site,
// so content blockers that block Kit's own script don't break signups. If anything goes
// wrong, the form is submitted normally and Kit shows its own confirmation page.
document.querySelectorAll('form[data-weekly-form]').forEach(function (form) {
  form.addEventListener('submit', function (event) {
    if (!window.fetch || !window.FormData) return;
    event.preventDefault();
    var button = form.querySelector('button[type=submit]');
    var errors = form.querySelector('.weekly-errors');
    var fallback = function () { form.submit(); };
    button.disabled = true;
    button.setAttribute('data-active', '');
    fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (data) {
        if (data.status === 'success') {
          var done = document.createElement('p');
          done.className = 'weekly-success';
          done.setAttribute('role', 'status');
          done.textContent = form.getAttribute('data-success');
          var fields = form.querySelector('.weekly-field');
          fields.parentNode.replaceChild(done, fields);
          errors.hidden = true;
        } else if (data.status === 'quarantined' || !data.errors) {
          fallback(); // Kit wants an extra check, which its own page handles
        } else {
          var list = [].concat(data.errors.messages || data.errors);
          errors.textContent = list.join(' ');
          errors.hidden = false;
          button.disabled = false;
          button.removeAttribute('data-active');
        }
      })
      .catch(fallback);
  });
});
