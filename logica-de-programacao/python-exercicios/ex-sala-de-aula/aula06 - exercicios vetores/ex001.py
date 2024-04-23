import os;
os.system('cls || clear');

soma: int = 0;
contador: int = 0;

notas = [];

for i in range(3):
    inputNotas = float(input(f'Digite a sua {i + 1}ª nota: '));
    notas.append(inputNotas);

media = sum(notas) / len(notas);

os.system('cls || clear');

for i in range(len(notas)):
    print(f'{i + 1}ª nota: {notas[i]}');

print(f'Média: {media:.1f}');