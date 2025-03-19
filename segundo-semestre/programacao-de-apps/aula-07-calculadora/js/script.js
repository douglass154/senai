const resultado = document.querySelector('.resultado span');
const btnCalcular = document.querySelector('.btn-calcular');

const calcularJuros = () => {
    const capital = document.querySelector('#capital').value;
    const juros = document.querySelector('#juros').value;
    const tempo = document.querySelector('#tempo').value;

    if (capital === '') return;
    if (juros === '') return;
    if (tempo === '') return;

    const montante = capital * (1 + (juros / 100)) ** tempo;
    resultado.parentElement.classList.add('active');
    resultado.textContent = `R$ ${montante.toFixed(2).replace('.', ',')}`;
}

btnCalcular.addEventListener('click', calcularJuros)
document.body.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') calcularJuros()
})