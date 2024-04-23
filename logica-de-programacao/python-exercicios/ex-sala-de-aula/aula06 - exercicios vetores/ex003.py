import os;
import time;

os.system('cls || clear');

numeros = [];

for i in range(5):
    inputNumeros = int(input(f'Digite o seu {i + 1}º número: '));
    numeros.append(inputNumeros);
    
maiorNumero = max(numeros);
menorNumero = min(numeros);

os.system("cls || clear");
print(f'Maior número: {maiorNumero}');
print(f'Menor número: {menorNumero}\n');

for i in range(len(numeros)):
    time.sleep(0.7);
    print(f'{i + 1}º número: {numeros[i]}');