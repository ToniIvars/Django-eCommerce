document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('search-button')
    const image = document.getElementById('search-image')

    button.onmouseover = () => {
        image.src = '/static/store/search-black.svg'
    }

    button.onmouseleave = () => {
        image.src = '/static/store/search.svg'
    }

    // Code for the filter buttons
    const price = document.getElementById('price')
    const price_reversed = document.getElementById('price_reversed')
    const query = document.getElementById('query_hidden').innerText

    const base_url = window.location.href.split('?')[0]

    price.onclick = () => {
        location.assign(`${base_url}?q=${query}&f=price`)
    }

    price_reversed.onclick = () => {
        location.assign(`${base_url}?q=${query}&f=price_reversed`)
    }
})