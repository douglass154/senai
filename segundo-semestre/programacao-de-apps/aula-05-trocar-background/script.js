const firstBtn = document.querySelector('#img-1');
const secondBtn = document.querySelector('#img-2');
const thirdBtn = document.querySelector('#img-3');

firstBtn.addEventListener('click', () => {
    document.querySelector('body').style.background = 'URL("imgs/imagem-1.jpg")';
})

secondBtn.addEventListener('click', () => {
    document.querySelector('body').style.background = 'URL("imgs/imagem-2.jpg")';
})

thirdBtn.addEventListener('click', () => {
    document.querySelector('body').style.background = 'URL("imgs/imagem-3.jpg")';
})