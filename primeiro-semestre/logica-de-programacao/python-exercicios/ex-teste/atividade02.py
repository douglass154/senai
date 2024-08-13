"""
Construa um algoritmo que calcule a média aritmética de vários
números inteiros positivos, inseridos pelo usuário.

O final da leitura acontecerá quando for lido um número negativo.

Mostre a média aritmética dos números informados pelo usuário.
"""

numeros = 0
contador = 1
soma = 0

while numeros >= 0:
    numeros = int(input('Digite o '+ str(contador)+ 'º número: '));
    
    if numeros >= 0:
        contador += 1;
        soma += numeros;
    else:
        print('Não é possível adicionar números negativos. Exibindo resultados!!');

media = soma / (contador - 1);

print("Média dos números digitados: "+ str(media));