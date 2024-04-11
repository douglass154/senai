import os;

os.system('cls || clear');

numero = int(input('Digite um número: '));

print('=== TABUADA DE MULTIPLICAÇÃO ===\n');
for i in range(10):
    print(f'{numero} x {i + 1} = {numero * (int(i) + 1)}');