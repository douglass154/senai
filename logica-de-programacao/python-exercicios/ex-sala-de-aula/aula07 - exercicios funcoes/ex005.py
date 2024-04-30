import os;
os.system("cls || clear");

def parImpar(num):
    if (num % 2 == 0):
        print(f'{num} é Par');
    else:
        print(f'{num} é Ímpar');

numero = int(input('Digite um número: '));
parImpar(numero);