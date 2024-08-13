import os;

os.system('cls || clear');

notas = []
soma = 0
i = 0

for i in range(4):
    notasInput = float(input(f'Digite a {i+1} nota: '));
    notas.append(notasInput);

