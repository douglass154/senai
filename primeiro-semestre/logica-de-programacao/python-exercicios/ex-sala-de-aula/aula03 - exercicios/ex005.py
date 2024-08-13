import os;
os.system('cls || clear');

nomeProduto = str(input('Digite o nome do produto: '));
quantidadeDeProdutos = int(input('Digite quantos produtos você deseja: '));
precoProdutoUnitario = float(127.90);

desconto = 0;
totalPreco: float = quantidadeDeProdutos * precoProdutoUnitario;

if quantidadeDeProdutos <= 5:
    desconto = totalPreco - (2 / 100);
elif quantidadeDeProdutos > 5 and quantidadeDeProdutos <= 10:
    desconto = totalPreco - (3 / 100);
else:
    desconto = totalPreco - (5 / 100);

totalParaPagar = totalPreco - desconto;

print(f'Preço total: {totalPreco}');
print(f'Desconto: {desconto:.2f}');
print(f'Preço descontado: {totalParaPagar:.2f}'); 