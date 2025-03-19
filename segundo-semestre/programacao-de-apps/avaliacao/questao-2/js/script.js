
const imc = document.querySelector('.imc span');
const informacoes = document.querySelector('.info-resultado');
const btnCalcular = document.querySelector('.btn-calcular');


btnCalcular.addEventListener('click', () => {
    const kg = document.querySelector('#kg').value;
    const metros = document.querySelector('#metros').value;
    
    calcularIMC(kg, metros);
})

const calcularIMC = (kg, metros) => {
    const calculoIMC = kg / metros**2;
    imc.textContent = calculoIMC.toFixed(2).replace('.', ',');

    if (calculoIMC < 18.5) {
        informacoes.textContent = "Você está muito magro!";
        return
    }
    if (calculoIMC < 25) {
        informacoes.textContent = "Você está no peso ideal!";
        return
    }
    if (calculoIMC < 30) {
        informacoes.textContent = "Você está acima do peso!";
        return
    }
    
    informacoes.textContent = "Você está com obesidade!"
};