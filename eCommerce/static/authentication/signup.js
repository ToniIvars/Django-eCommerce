document.addEventListener('DOMContentLoaded', function () {
    const inp = document.querySelector('#id_password')
    const inp2 = document.querySelector('#id_password2')
    let count = 1
    let count2 = 1

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

    inp2.onmouseover = () => {
        if (inp2.type === 'password' && count2 === 0) {
            inp2.type = 'text'
            count2 += 1
        } else if (inp2.type === 'text' && count2 === 0) {
            inp2.type = 'password'
            count2 += 1
        }
    }

    inp2.onmouseleave = () => {
        count2 = 0
    }

});