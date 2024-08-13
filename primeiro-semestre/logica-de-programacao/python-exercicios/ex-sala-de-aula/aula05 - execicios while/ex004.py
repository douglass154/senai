import os;
os.system('cls || clear');

soma:float = 0;
contador:int = 1;

notas = float(input('Digite uma nota: '));
soma += notas;

while True:
    resposta = str(input('Deseja inserir mais 1 nota?: '));

    if(resposta == 'N' or resposta == 'n'):
        break;
    else:
        notas = float(input('Digite outra nota: '));
        soma += notas;
        contador += 1;

media = soma / contador;

print(f'Média: {media:.2f}');