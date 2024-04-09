import os;
os.system("cls || clear");

idade = int(input('Digite sua idade: '));

if idade < 18 or idade >= 65:
    print('Não é obrigado a votar!');
else:
    print('obrigado a votar');