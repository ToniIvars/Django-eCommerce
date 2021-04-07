document.addEventListener('DOMContentLoaded', function () {
    const inp = document.querySelector('#id_password')
    let count = 1

    inp.onmouseover = () => {
        if (inp.type === 'password' && count === 0) {
            inp.type = 'text'
            count += 1
        } else if (inp.type === 'text' && count === 0) {
            inp.type = 'password'
            count += 1
        }
    }

    inp.onmouseleave = () => {
        count = 0
    }

});