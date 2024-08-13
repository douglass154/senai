import os;
import time;

os.system('cls || clear');

numeros = [];

for i in range(5):
    inputNumeros = int(input(f'Digite o seu {i + 1}º número: '));
    
    if (inputNumeros >= 0):
        numeros.append(inputNumeros);
    else:
        inputNumeros = int(0);
        numeros.append(inputNumeros);

for i in range(len(numeros)):
    print(f'{i + 1}º Valor: {numeros[i]}');

    