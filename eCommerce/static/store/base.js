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
})