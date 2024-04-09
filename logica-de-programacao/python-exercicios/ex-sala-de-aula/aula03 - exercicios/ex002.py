import os;

os.system('cls || clear');

loginRegistro = str(input('Registre seu login: '));
senhaRegistro = str(input('Registre sua senha: '));

os.system('cls || clear');

login = str(input('Digite seu e-mail: '));
senha = str(input('Digite sua senha: '));

if login == loginRegistro and senha == senhaRegistro:
    print('Bem-vindo!!');

while login != loginRegistro or senha != senhaRegistro:
    if login != loginRegistro or senha != senhaRegistro:
        os.system('cls || clear');
        print('Login ou senha inválidos');
    
        login = str(input('Digite seu e-mail: '));
        senha = str(input('Digite sua senha: '));
        
print('Bem-vindo!!');