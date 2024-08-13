import os;
os.system('cls || clear');

soma: int = 0;

for i in range(5):
    numeros = int(input(f'Digite o {i + 1}º número: '));
    soma = soma + numeros;

print(f'A soma dos seus números é: {soma}');