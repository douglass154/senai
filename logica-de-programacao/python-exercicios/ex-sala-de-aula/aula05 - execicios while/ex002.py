import os;
os.system('cls || clear');

soma: float = 0;

i = int(0);
for i in range(2):
    nota = float(input(f'Digite a {i + 1}ª nota: '));

    while nota < 0 or nota > 10:
        nota = float(input(f'Digite a {i + 1}ª nota: '));

    if nota >= 0 or nota <= 10:
        soma += nota;
    
    i = i + 1;
    media = soma / i;

print(f'Média: {media}');

