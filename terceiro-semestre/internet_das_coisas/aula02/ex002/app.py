
def calcularIMC(peso, altura):
    imc = float(peso / (altura ** 2));
    
    if(imc < 18.5):
        print(f"Você está abaixo do peso. IMC: {imc:.2f}");
    elif(imc < 24.9):
        print(f"Você está no peso ideal. IMC: {imc:.2f}");
    elif(imc < 29.9):
        print(f"Você está sobrepeso. IMC: {imc:.2f}");
    elif(imc < 34.9):
        print(f"Você está com Obesidade grau I. IMC: {imc:.2f}");
    elif(imc < 39.9):
        print(f"Você está com Obesidade grau II. IMC: {imc:.2f}");
    else:
        print(f"Você está com Obesidade grau III. IMC: {imc:.2f}");
        
peso = float(input("Digite o seu peso: "));
altura = float(input("Digite a sua altura: "));
        
calcularIMC(peso, altura);
calcularIMC(215.56, 1.78);