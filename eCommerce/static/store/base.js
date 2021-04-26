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

    // Code for the filter buttons
    function able_button(button) {
        button.disabled = false
        button.classList.remove('button-disabled')
    }
    
    function disable_button(button) {
        button.disabled = true
        button.classList.add('button-disabled')
    }

    const button_price_ascendant = document.getElementById('price_ascendant')
    const button_price_descendant = document.getElementById('price_descendant')

    const div_results_ascendant = document.getElementById('results_ascendant')
    const div_results_descendant = document.getElementById('results_descendant')

    disable_button(button_price_ascendant)

    button_price_descendant.onclick = () => {
        div_results_ascendant.style.display = 'none'
        div_results_descendant.style.display = 'block'

        disable_button(button_price_descendant)
        able_button(button_price_ascendant)
    }

    button_price_ascendant.onclick = () => {
        div_results_descendant.style.display = 'none'
        div_results_ascendant.style.display = 'block'

        able_button(button_price_descendant)
        disable_button(button_price_ascendant)
    }
})