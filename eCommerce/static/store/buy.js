document.addEventListener('DOMContentLoaded', function () {
    const bank_card_option = document.getElementById('id_paying_ways_0')
    const paypal_option = document.getElementById('id_paying_ways_1')
    const bitcoin_option = document.getElementById('id_paying_ways_2')
    const paying_data = document.getElementById('id_paying_data')

    bank_card_option.onclick = () => {
        paying_data.placeholder = 'Bank card number'
    }

    paypal_option.onclick = () => {
        paying_data.placeholder = 'PayPal number'
    }

    bitcoin_option.onclick = () => {
        paying_data.placeholder = 'Bitcoin number'
    }

    bank_card_option.checked = true
    paying_data.placeholder = 'Bank card number'
})