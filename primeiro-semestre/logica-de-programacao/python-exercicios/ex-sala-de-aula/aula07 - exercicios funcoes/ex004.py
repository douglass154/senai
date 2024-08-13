import os;
os.system('cls || clear');

def calcular(codigo, num1, num2):
    if(codigo == '+'):
        return num1 + num2;
    if(codigo == '-'):
        return num1 - num2;
    if(codigo == '*'):
        return num1 * num2;
    if(codigo == '/'):
        return num1 / num2;

primeiroNum = int(input('Digite o primeiro número: '));
segundoNum = int(input('Digite o segundo número: '));
codigo = str(input('Coloque o operador desejado para a conta(+, -, *, /): '));
resultado = calcular(codigo, primeiroNum, segundoNum);

os.system('cls || clear');
print('Resultado da conta: ');
calcular(primeiroNum, segundoNum);