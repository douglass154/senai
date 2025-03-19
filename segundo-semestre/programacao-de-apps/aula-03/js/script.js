
const buttons = document.querySelectorAll('button');
const img = document.querySelector('img')

const medias = [
   {index: 0, src: 'imgs/raiva.png'},
   {index: 1, src: 'imgs/alegria.png'},
   {index: 2, src: 'imgs/nojinho.png'},
   {index: 3, src: 'imgs/tristeza.png'},
]

buttons.forEach((button, index) => {
   button.addEventListener('click', () => {

      index === medias[index].index
         ? img.src = medias[index].src
         : null

   })
})