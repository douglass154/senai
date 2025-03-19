
const midias = [
    {
        id: 0,
        nome: "Annabelle",
        src: "./imgs/annabelle.jpg",
        descricao: "Um jovem casal se prepara para o nascimento do seu primeiro bebê e compra uma boneca de presente para a futura filha. Quando sua casa é invadida por membros de uma seita e o casal é violentamente atacado, a boneca Anabelle torna-se o recipiente de uma entidade malévola."
    },
    {
        id: 1,
        nome: "Elementos",
        src: "./imgs/elementos.jfif",
        descricao: "Elementos é um filme de animação que se passa em uma sociedade extraordinária chamada Cidade Elemento, na qual os quatro elementos da natureza - ar, terra, fogo e ar - vivem em completa harmonia."
    },
    {
        id: 2,
        nome: "Jango Livre",
        src: "./imgs/jango-livre.jfif",
        descricao: "Situado num contexto pré-Guerra de Secessão do Deep South e Velho Oeste, o filme acompanha Django, um escravo liberto que caminha pelos Estados Unidos com um caçador de recompensas em uma missão para resgatar sua esposa de um fazendeiro cruel."
    },
    {
        id: 3,
        nome: "Lucifer",
        src: "./imgs/lucifer.jpg",
        descricao: "A série se desenvolve ao redor de Lucifer Morningstar, que está entediado e infeliz como o Senhor do Inferno. Ele renuncia seu trono e abandona seu reinado para tirar férias em Los Angeles, onde dá início a uma casa noturna com a ajuda de sua aliada demoníaca, Mazikeen Smith."
    }
]

const img = document.querySelector('img')
const descricao = document.querySelector('.descricao');
const buttons = document.querySelectorAll('button');

buttons.forEach((button, index) => {
    button.addEventListener('click', () => {
        if (index === midias[index].id) {
            img.src = midias[index].src;
            descricao.textContent = midias[index].descricao;
        }
    })
})