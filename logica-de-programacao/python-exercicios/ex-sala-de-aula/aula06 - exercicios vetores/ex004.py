import os;
import time;

os.system('cls || clear');

quantidadeDeNegativos: int = 0;
somaDosPositivos: int = 0;

numeros = [];

for i in range(10):
    inputNumeros = float(input(f'Digite o seu {i + 1}º número: '));
    numeros.append(inputNumeros);

    if (inputNumeros < 0):
        quantidadeDeNegativos += 1;
    if(inputNumeros >= 0):
        somaDosPositivos += inputNumeros;

os.system('cls || clear');

print(f'Soma dos números positivos: {somaDosPositivos:.2f}');
print(f'Quantidade de negativos: {quantidadeDeNegativos}');