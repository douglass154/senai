import os;
os.system('cls || clear');

class Livros:
    def __init__(self, nome, autor, categoria, preco):
        self.nome = nome;
        self.autor = autor;
        self.categoria = categoria;
        self.preco = preco;

arquivo = 'arquivos-txt/catalogo_livros.txt';

livros = [];

for i in range(3):
    livros.append(Livros(
        nome = input('Nome do livro: '),
        autor = input('Nome do autor: '),
        categoria = input('Categoria do livro: '),
        preco = float(input('Preço: '))
    ));
    os.system('cls || clear');

with open(arquivo, 'w') as arquivoDeLivros:
    for livro in livros:
        arquivoDeLivros.write(f'Nome do livro: {livro.nome}\nAutor: {livro.autor}\n');
        arquivoDeLivros.write(f'Categoria: {livro.categoria}\nPreço: {livro.preco:.2f}\n\n');

print('Dados salvos com sucesso!');