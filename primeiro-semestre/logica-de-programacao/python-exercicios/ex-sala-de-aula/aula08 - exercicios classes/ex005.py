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

def salvar_arquivos(aquivos):
    with open(arquivo, 'w') as arquivoDeLivros:
        for arquivo in aquivos:
            arquivoDeLivros.write(f'Nome do livro: {arquivo.nome}\nAutor: {arquivo.autor}\n');
            arquivoDeLivros.write(f'Categoria: {arquivo.categoria}\nPreço: {arquivo.preco:.2f}\n\n');

salvar_arquivos(livros)

print('Dados salvos com sucesso!');