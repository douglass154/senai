
const form = document.querySelector('#login_form')
const icon = document.querySelector('#mode_icon')
const buttonLogin = document.querySelector('#login_button')

icon.addEventListener('click', () => {
    form.classList.toggle('dark');

    icon.classList.toggle('bxs-moon');
    icon.classList.toggle('bxs-sun');
})