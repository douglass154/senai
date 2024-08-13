import os;

def logoSenai():
    os.system('cls || clear');
    print('=== SENAI ===');

def somar(n1, n2):
    return n1 + n2;


logoSenai();
primeiroNumero = int(input('Digite o 1º número: '));
segundoNumero = int(input('Digite o 2º número: '));
resultado = somar(primeiroNumero, segundoNumero);

logoSenai();
print(f'A soma dos seus números é: {resultado}');