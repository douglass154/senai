import os;
from dataclasses import dataclass;

os.system('cls || clear');

@dataclass
class Aluno:
    nome: str;
    idade: int;

QUANTIDADE_ALUNOS = 2;

alunos = [];

for i in range(QUANTIDADE_ALUNOS):
    nome = input('Digite seu nome: ');
    idade = int(input('Digite sua idade: '));
    
    alunos.append(Aluno(nome = nome, idade = idade));
    os.system('cls || clear');

arquivo = 'alunos.txt'

with open(arquivo, 'w') as arquivosDeAlunos:
    for aluno in alunos:
        arquivosDeAlunos.write(f'Nome: {aluno.nome}, Idade: {aluno.idade}\n');

print('Dados salvos com sucesso!');