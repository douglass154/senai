import os;
import time;

os.system('cls || clear');

numeros = [];
i = 0;

for i in range(6):
    while True:
        inputNumeros = int(input(f'Digite o {i + 1}º número: '));

        if (inputNumeros >= 0):
            numeros.append(inputNumeros);
            break;
        else:
            print('Números negativos são inválidos!!');
            time.sleep(1.5);

for i in range(len(numeros)-1, -1, -1):
    print(f'Números inseridos mas em ordem inversa: {numeros[i]}');