import os;
from random import randint;

os.system('cls || clear');

pares: int = 0;
impares:int = 0;
positivos:int = 0;
negativos:int = 0;
mediaPar:float = 0;
somaPar: int = 0;
mediaImpar:float = 0;
somaImpar: int = 0;
mediaGeral:int = 0;
menorNum:int = 99999;
maiorNum: int = 0;

numeros = [];

def verificaParImpar(num):
    impares:int = 0;
    pares: int = 0;

    if num % 2 == 0:
        pares += 1;
        somaPar += num;
        return 
    else:
        impares += 1;
        somaImpar += num;

def verificaPositivoENegativo(num):
    if num >= 0:
        positivos += 1;
    else:
        negativos += 1;

def maiorEMenorNum(num):
    if num < menorNum:
        menorNum = num;
    if num > maiorNum:
        maiorNum = num;

for i in range(1, 6):
    inputNum = int(input(f'Digite o {i}º número: '));
    numeros.append(inputNum);

    verificaParImpar(inputNum);
    verificaPositivoENegativo(inputNum);
    maiorEMenorNum(inputNum);

mediaPar = pares / somaPar;
mediaImpar = impares / somaImpar;
mediaGeral = sum(numeros) / len(numeros);

print(f'Quantidade de pares: {pares}');
print(f'Quantidade de impares: {impares}');
print(f'Quantidade de números positivos: {positivos}');
print(f'Quantidade de números negativos: {negativos}');
print(f'Média pares: {mediaPar}');
print(f'Média impares: {mediaImpar}');
print(f'Média geral: {mediaGeral}');
