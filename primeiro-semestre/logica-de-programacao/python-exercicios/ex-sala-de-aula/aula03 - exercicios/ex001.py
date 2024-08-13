import os;

os.system("cls || clear")

firstNumber = int(input("Digite o primeiro número: "));
secondNumber = int(input("Digite outro número: "));

soma  = firstNumber + secondNumber;
media = soma / 2;
produto = firstNumber * secondNumber;

if firstNumber < secondNumber:
    menorValor = firstNumber;
    maiorValor = secondNumber;
else:
    maiorValor = firstNumber;
    menorValor = secondNumber;

print(f'Média: {media}');
print(f'Soma dos números: {soma}');
print(f'Produto: {produto}');
print(f'Menor valor: {menorValor}');
print(f'Maior valor: {maiorValor}');