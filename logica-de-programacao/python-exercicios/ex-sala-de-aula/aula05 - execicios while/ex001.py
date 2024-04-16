import os;
os.system('cls || clear');

nota = float(input('Digite uma nota: '));

while nota < 0 or nota > 10:
    nota = float(input('Digite uma nota: '));

print(f'Nota: {nota}');