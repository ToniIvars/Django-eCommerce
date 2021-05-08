document.addEventListener('DOMContentLoaded', function () {
    // Code for the color changing of the search button
    const button = document.getElementById('search-button')
    const image = document.getElementById('search-image')

    button.onmouseover = () => {
        image.src = '/static/store/search-black.svg'
    }

    button.onmouseleave = () => {
        image.src = '/static/store/search.svg'
    }

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

    // Code for hiding the message
    const message_container = document.getElementById('message-container')

    document.getElementById('close-message').onclick = () => {
        message_container.classList.add('not-displayed')
        document.getElementById('container-when-message').classList.add('main-container')
    }
})