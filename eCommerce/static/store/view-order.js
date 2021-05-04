document.addEventListener('DOMContentLoaded', function () {
    const state = document.getElementById('order-state')

    if (state.innerHTML === 'Opened') {
        state.classList.add('red')

    } else if (state.innerHTML === 'In progress') {
        state.classList.add('yellow')

    } else if (state.innerHTML === 'Delivered') {
        state.classList.add('green')
    }

})