

const btnResultado = document.querySelector('#btn-resultado');
const resultado = document.querySelector('#resultado');

btnResultado.addEventListener('click', () => {
    const n1 = Number(document.querySelector('#uni-1').value);
    const n2 = Number(document.querySelector('#uni-2').value);
    const n3 = Number(document.querySelector('#uni-3').value);
    
    let resultadoAprovacao;
    const media = (n1 + n2 + n3) / 3;

    if (media < 4) resultadoAprovacao = 'Reprovado';
    else if (media < 7) resultadoAprovacao = "Recuperação";
    else resultadoAprovacao = "Aprovado"

    resultado.innerHTML = `
        Sua média foi ${media.toFixed(1)} </br>
        Resultado: ${resultadoAprovacao};
    `
})