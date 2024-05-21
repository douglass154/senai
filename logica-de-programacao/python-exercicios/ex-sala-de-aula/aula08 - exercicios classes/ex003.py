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

pessoas.append(Pessoa(
    nome = input('Digite seu nome: '),
    idade = int(input('Digite sua idade: ')),
    peso = float(input('Digite seu peso: ')),
    altura = float(input('Digite sua altura: '))
));

with open(arquivo, 'w') as arquivoDePessoas:
    for pessoa in pessoas:
        arquivoDePessoas.write(f'Nome: {pessoa.nome}\nIdade: {pessoa.idade}\nPeso: {pessoa.peso:.2f}\nAltura: {pessoa.altura:.2f}');
        
print('\nDados salvos com sucesso!!');