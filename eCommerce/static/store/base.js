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

    const url = window.location.href
    const base_url = url.split('?')[0]

    price.onclick = () => {
        location.assign(`${base_url}?q=${query}&f=price`)
    }
    price_reversed.onclick = () => {
        location.assign(`${base_url}?q=${query}&f=price_reversed`)
    }

    if (url.includes('price_reversed')) {
        price_reversed.disabled = true
        price_reversed.classList.add('button-disabled')

    } else if (url.includes('price')) {
        price.disabled = true
        price.classList.add('button-disabled')
    }
})