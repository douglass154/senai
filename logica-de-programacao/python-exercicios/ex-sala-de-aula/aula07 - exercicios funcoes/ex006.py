import os;
os.system('cls || clear');

def transformCM(metro):
    return metro * 100;

metro = float(input('Digite um valor em metros: '));
centimetros = transformCM(metro);

os.system('cls || clear');
print(f'Valor em centímetros: {centimetros:.2f}');