import os;
import time;

os.system('cls || clear');

class Usuario:
    def __init__(self, nome, dataDeNascimento, rg, cpf):
        self.nome = nome;
        self.dataDeNascimento = dataDeNascimento;
        self.rg = rg;
        self.cpf = cpf;

usuarios = [];
lerUsuarios = [];
arquivo = 'arquivos-txt/Funcionarios.txt';

for i in range(1):
    usuarios.append(Usuario(
        nome = input('Digite seu nome: '),
        dataDeNascimento = input('Digite sua data de nascimento: '),
        rg = input('Digite seu RG: '),
        cpf = input('Digite seu CPF: ')
    ));

    os.system('cls || clear');

def salvar_usuarios(usuarios):
    with open(arquivo, 'w') as arquivoUsuarios:
        for usuario in usuarios:
            arquivoUsuarios.write(f'Nome: {usuario.nome}\n');
            arquivoUsuarios.write(f'Data de nascimento: {usuario.dataDeNascimento}\n');
            arquivoUsuarios.write(f'RG: {usuario.rg}\n');
            arquivoUsuarios.write(f'CPF: {usuario.cpf}\n\n');

def ler_info_usuarios(arquivo):
    with open(arquivo, 'r') as arquivoUsuarios:
        registro = arquivoUsuarios.read()
        print(registro)

for usuario in lerUsuarios:
    print(f'nome: {usuario.nome}');
    print(f'Data de Nascimento: {usuario.dataDeNascimento}');
    print(f'RG: {usuario.rg}');
    print(f'CPF: {usuario.cpf}');

salvar_usuarios(usuarios);
ler_info_usuarios(arquivo);