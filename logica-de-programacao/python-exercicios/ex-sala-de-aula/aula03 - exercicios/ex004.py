import os;

os.system('cls || clear');

numeros = [];
soma = int(0);

pares = int(0);
impares = int(0);

for i in range(5):
    inputNumeros = int(input(f'Digite o {i + 1}º primeiro: '));
    numeros.append(inputNumeros);
    soma += numeros[i];

    if numeros[i] % 2 == 0:
        pares += 1
    else:
        impares += 1;

print(f'Soma dos números: {soma}');
print(f'Quantidade de pares: {pares}');
print(f'Quantidade de impares: {impares}');