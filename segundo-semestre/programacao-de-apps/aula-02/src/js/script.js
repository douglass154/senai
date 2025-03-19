
const lampada = document.querySelector('#lamp');

const acender = document.querySelector('.acender');
const apagar = document.querySelector('.apagar');

const acenderLamp = () => {
    lampada.src = 'src/imgs/acesa.gif';
    acender.style.display = 'none';
    apagar.style.display = 'block';
}

const apagarLamp = () => {
    lampada.src = 'src/imgs/apagada.gif';
    apagar.style.display = 'none';
    acender.style.display = 'block';
}

const breakLamp = () => {
    lampada.src = 'src/imgs/quebrada.jpg';
    apagar.style.display = 'none';
    acender.style.display = 'none';
}

acender.addEventListener('click', acenderLamp);
apagar.addEventListener('click', apagarLamp);
lampada.addEventListener('dblclick', breakLamp);