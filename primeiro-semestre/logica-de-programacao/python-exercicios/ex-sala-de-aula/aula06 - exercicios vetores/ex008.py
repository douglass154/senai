import os;
os.system('cls || clear');

qntPositivos = int(0);
qntNegativos = int(0)
pares = int(0);
impares = int(0);
contador = int(0);


numeros = int(input(f'Digite o 1º número: '));
contador += 1;

while numeros != 0:
    
    numeros = int(input(f'Digite o {contador + 1}º número: '));

    if numeros % 2 == 0:
        pares += 1;
    else:
        impares += 1;

    if numeros >= 0:
        qntPositivos += 1;
    else:
        qntNegativos += 1;

    contador += 1;

print(f'Quantidade de numeros pares: {pares}');
print(f'Quantidade de numeros impares: {impares}');
print(f'Quantidade de números positivos: {qntPositivos}');
print(f'Quantidade de números negativos: {qntNegativos}');
print(f'Quantidade de números inseridos: {contador}');