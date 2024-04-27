up.compiler('select', function (element) {
    new TomSelect(element);
});

/* it seems
"up.feedback.config.currentClasses.push('active');" from unpoly-bootstrap.js
removes active class from toggle btn , to fix this, we add it back
*/
up.compiler('#toggle-btn', function (element) {
    element.classList.add('active')
});
