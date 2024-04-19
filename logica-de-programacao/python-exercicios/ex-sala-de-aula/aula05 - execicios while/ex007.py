import os;
os.system('cls || clear');

contador = int(1);
contadorPar = int(0);
soma = int(0);
somaPar = int(0);
somaImpar = int(0);


while True:
    numeros = int(input(f'Digite o {contador}º número: '));

    if (numeros > 0):

        if(numeros % 2 == 0):
            somaPar += 1;
            contadorPar += 1;
            mediaPar = somaPar / contadorPar;
        else:
            somaImpar += 1;

        contador += 1;
        soma += 1;
        media = soma / (contador - 1);
    elif (numeros == 0):
        print('Fim!!');
        break;
    else:
        print('Números negativos são inválidos!!');
        break;

print(f'Quantidade de números pares: {somaPar}');
print(f'Quantidade de números impares: {somaImpar}');
print(f'Média de valores pares: {mediaPar}');
print(f'Média geral: {media}');