""" 
Crie um programa em C que leia 6 números inteiros em
um vetor e, utilizando um laço de repetição, informe:

- Os números inseridos pelo usuário;
- Quantos números são pares;
- Quantos números são ímpares. 
"""

import os;

numeros = [];
x = 0;
impares = 0;
pares = 0;

for x in range(6):
    numerosInput = int(input("Digite o "+ str(x + 1)+ "º número: "));
    numeros.append(numerosInput);

    if numerosInput % 2 == 0:
        pares = pares + 1;
    else:
        impares = impares + 1;

os.system('cls || clear');

for x in range(6):
    print('O '+ str(x + 1)+ 'º Número digitado foi: '+ str(numeros[x]));

print('Quantidade de números pares: '+ str(pares));
print('Quantidade de números impares: '+ str(impares));