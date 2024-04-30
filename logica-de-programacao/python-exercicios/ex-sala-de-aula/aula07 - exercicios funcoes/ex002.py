import os;

def logoSenai():
    os.system('cls || clear');
    print('=== SENAI ===');

def somar(n1, n2):
    return n1 + n2;

logoSenai();
primeiroNum = int(input('Digite o primeiro número: '));
segundoNum = int(input('Digite o segundo número: '));

soma = somar(primeiroNum, segundoNum);
media = soma / 2

print(f'A média dos seu números é {media:.2f}');