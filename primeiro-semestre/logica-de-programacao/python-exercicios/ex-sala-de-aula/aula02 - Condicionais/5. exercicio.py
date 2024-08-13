import os;

os.system('cls || clear');

soma = int(0);
i = int(0);

nome = str(input('Digite seu nome: '));
idade = int(input('Digite sua idade: '));
notas = [];

for i in range(4):
    notasInput = float(input(f'Digite a {i+1}ª nota: '));
    notas.append(notasInput);
    soma += notasInput;

media = soma / 4;

os.system('cls || clear');

print(f'Nome: {nome}');
print(f'Idade: {idade}');

for i in range(4):
    print(f'{i + 1}ª Nota: {notas[i]}');

print(f'Media: {media}');