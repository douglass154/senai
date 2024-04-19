import os;
os.system('cls || clear');

soma = int(0);
contador = int(1);

numeros = int(input(f'Digite o {contador}º número: '));
contador += 1;
soma += numeros;

while numeros >= 0:
    numeros = int(input(f'Digite o {contador}º numero: '));
    
    if (numeros >= 0):
        contador += 1;
        soma += numeros;
    else:
        print("Números negativos são inválidos!!");

media = soma / (contador - 1);
print(f'Média: {media:.2f}');