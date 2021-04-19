document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('search-button')
    const image = document.getElementById('search-image')

    button.onmouseover = () => {
        image.src = '/static/store/search-black.svg'
    }

    button.onmouseleave = () => {
        image.src = '/static/store/search.svg'
    }
})