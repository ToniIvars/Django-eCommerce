document.addEventListener('DOMContentLoaded', function () {
    const orders = document.querySelectorAll('.delivery-state')
    const states = document.querySelectorAll('.js-state')

    for (let i = 0; i < orders.length; i++) {
        if (states[i].innerHTML === 'Opened') {
            orders[i].classList.add('red')
        } else if (states[i].innerHTML === 'In progress') {
            orders[i].classList.add('yellow')
        } else {
            orders[i].classList.add('green')
        }
    }
})