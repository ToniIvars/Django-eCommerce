document.addEventListener('DOMContentLoaded', function () {
    function change_quantity(what_to_do, product_name, quantity) {
        const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value

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
                console.log(new_quantity)

                if (new_quantity > 0) {
                    document.getElementById(`quantity-${product_name}`).innerHTML = new_quantity
                    
                } else {
                    document.getElementById(product_name).classList.add('not-displayed')
                }
            })
    }

    document.querySelectorAll("[id^='remove']").forEach(btn => {
        const what_to_do = 'remove'
        const product_name = btn.id.split('-').pop()
        const quantity = document.getElementById(`quantity-${product_name}`).innerHTML

        btn.onclick = () => {
            change_quantity(what_to_do, product_name, quantity)
        }
    })
})