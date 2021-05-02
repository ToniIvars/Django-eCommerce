document.addEventListener('DOMContentLoaded', function () {
    const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value

    function delete_from_cart(product_name) {

        fetch('/delete-from-cart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                product_to_delete: product_name
            })
        })
            .then(res => console.log(res.text()))
    }

    function change_quantity(what_to_do, product_name, quantity) {

        fetch('/change-quantity', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                product: product_name,
                change: what_to_do,
                quantity: quantity
            })
        })
            .then(res => res.json())
            .then(data => {
                const new_quantity = data['new_quantity']

                document.getElementById(`quantity-${product_name}`).innerHTML = new_quantity

                if (new_quantity <= 0) {
                    document.getElementById(product_name).classList.add('not-displayed')
                    delete_from_cart(product_name)
                }

                set_total()
            })
    }

    function set_total() {
        const prices = document.querySelectorAll('.price')
        const quantities = document.querySelectorAll("[id^='quantity']")
        const total_span = document.getElementById('total-span')

        let total = 0

        for (i=0; i < prices.length; i++) {
            total += prices[i].innerHTML.slice(0,-1) * quantities[i].innerHTML
        }

        total = Math.round(total * 100) / 100
        total_span.innerHTML = `${total}$`
    }

    document.querySelectorAll("[id^='remove']").forEach(btn => {
        const what_to_do = 'remove'
        const product_name = btn.id.split('-').pop()
        const quantity = document.getElementById(`quantity-${product_name}`).innerHTML

        btn.onclick = () => {
            change_quantity(what_to_do, product_name, quantity)
        }
    })

    document.querySelectorAll("[id^='add']").forEach(btn => {
        const what_to_do = 'add'
        const product_name = btn.id.split('-').pop()
        const quantity = document.getElementById(`quantity-${product_name}`).innerHTML

        btn.onclick = () => {
            change_quantity(what_to_do, product_name, quantity)
        }
    })

    set_total()
})