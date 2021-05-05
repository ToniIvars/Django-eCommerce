document.addEventListener('DOMContentLoaded', function () {
    const order_id = document.getElementById('order-id').innerHTML
    const csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value

    const first_item = Array.from(document.querySelectorAll('button.dropdown-toggle')).slice(-1)
    const other_items = Array.from(document.querySelectorAll('button.dropdown-item'))

    const items = first_item.concat(other_items)

    function check_state(element) {
        if (element.innerHTML === 'Opened') {
            return 'red'
    
        } else if (element.innerHTML === 'In progress') {
            return 'yellow'
    
        } else if (element.innerHTML === 'Delivered') {
            return 'green'
        }
    }

    function change_state_backend(state) {

        fetch('/change-delivery-state', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                order_id: order_id,
                state: state
            })
        })
            .then(res => res.text())
            .then(data => console.log(data))
    }
    
    items.forEach((element, index) => {
        element.innerHTML = element.innerHTML.trim()
        
        if (index === 1) {
            if (items[0].innerHTML !== 'Opened') {
                element.innerHTML = 'Opened'
            }
        } else if (index === 2) {
            if (items[0].innerHTML !== 'Opened') {
                if (items[0].innerHTML === 'In progress') {
                    element.innerHTML = 'Delivered'
                } else {
                    element.innerHTML = 'In progress'
                }
            }
        }

        element.classList.add(check_state(element))
    });

    items.slice(1,3).forEach(element => {
        element.onclick = () => {
            let item1_text = items[0].innerHTML
            let item1_color = check_state(items[0])
            let element_color = check_state(element)

            items[0].innerHTML = element.innerHTML
            element.innerHTML = item1_text

            items[0].classList.replace(item1_color, check_state(items[0]))
            element.classList.replace(element_color, check_state(element))

            change_state_backend(items[0].innerHTML)
        }
    });
})