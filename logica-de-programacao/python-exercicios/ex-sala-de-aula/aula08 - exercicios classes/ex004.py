import os;
os.system('cls || clear');

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome;
        self.idade = idade;
        self.peso = peso;
        self.altura = altura;

pessoas = [];

arquivo = 'arquivos-txt/arquivo.txt';

# pessoas.append(Pessoa(
#     nome = input('Digite seu nome: '),
#     idade = int(input('Digite sua idade: ')),
#     peso = float(input('Digite seu peso: ')),
#     altura = float(input('Digite sua altura: '))
# ));

with open(arquivo, 'r') as arquivoDePessoas:
    for linha in arquivoDePessoas:
        nome, idade, peso, altura = linha.strip().split(',');
        pessoas.append(Pessoa(nome, idade, peso, altura))

for pessoa in pessoas:
    print(f'Nome: {pessoa.nome}');
    print(f'Idade: {pessoa.idade}');
    print(f'Peso: {pessoa.peso}');
    print(f'Altura: {pessoa.altura}');