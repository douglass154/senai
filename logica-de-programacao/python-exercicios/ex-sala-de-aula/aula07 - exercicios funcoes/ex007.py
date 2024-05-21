import os;
os.system('cls || clear');

def alterarPreco(preco):
    if (preco < 100):
        return preco + (preco * (10 / 100));
    return preco - (preco * (20 / 100));
        
preco = float(input(f'Digite o preço do produto: '));
precoAlterado = alterarPreco(preco);

print(f'Preço inserido: R${preco}');
print(f'Preço modificado: R${precoAlterado}');
