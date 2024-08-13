import os;
os.system('cls || clear');

def tabuada(num):
    os.system('cls || clear');
    print(f'===== TABUADA DE {num} =====')
    for i in range(1, 11):
        print(' ' * 7 + f'{num} x {i} = {num * i}');

numero = int(input('Digite um número: '));
tabuada(numero);
    