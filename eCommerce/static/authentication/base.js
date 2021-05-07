document.addEventListener('DOMContentLoaded', function () {
    // Code for the favicon
    lightSchemeIcon = document.getElementById('white-theme-favicon');
    darkSchemeIcon = document.getElementById('dark-theme-favicon');

    matcher = window.matchMedia('(prefers-color-scheme: dark)');
    matcher.addListener(onUpdate);
    onUpdate();

    function onUpdate() {
        if (matcher.matches) {
            lightSchemeIcon.remove();
            document.head.append(darkSchemeIcon);
        } else {
            document.head.append(lightSchemeIcon);
            darkSchemeIcon.remove();
        }
    }

})