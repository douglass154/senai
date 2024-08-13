import os;
os.system('cls || clear');

soma:float = 0;
contador:int = 1;

notas = float(input('Digite uma nota: '));
soma += notas;

while True:
    print('\nS- para inserir mais uma nota!');
    print('P- para ver quantas notas fora inseridas!');
    print('N- para calcular a média aritmética das notas informadas!\n');

    resposta = str(input('Deseja inserir mais 1 nota?: '));

    if(resposta == 'S' or resposta == 's'):
        notas = float(input('Digite uma nota: '));
        soma += notas;
        contador += 1;
    
    elif(resposta == 'P' or resposta == 'p'):
        print(f'Quantidade de notas inseridas: {contador}');
        break;
    
    elif(resposta == 'N' or resposta == 'n'):
        break;
        
media = soma / contador;

print(f'Média: {media:.2f}');