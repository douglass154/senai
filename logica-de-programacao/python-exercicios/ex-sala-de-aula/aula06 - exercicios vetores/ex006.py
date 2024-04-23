import os;
import time;

os.system('cls || clear');

numeros = [];
i = 0;

for i in range(6):
    while True:
        inputNumeros = int(input(f'Digite o {i + 1}º número: '));

        if (inputNumeros >= 0 and inputNumeros % 2 == 0):
            numeros.append(inputNumeros);
            break;
        else:
            print('Números negativos ou impares são inválidos!!');
            time.sleep(1);

print('-=' * 40);
# for i in range(len(numeros)-1, -1, -1):
for valor in reversed(numeros):
    print(f'Números inseridos mas em ordem inversa: {valor}');