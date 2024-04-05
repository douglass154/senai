import os;

os.system('cls || clear');

idade = int(input('Digite sua idade: '));

if idade < 18 or idade >= 65:
    print('Não precisa votar!');
else:
    print('Obrigado a votar!');