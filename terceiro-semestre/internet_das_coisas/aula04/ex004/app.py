import os;

nomes = [];

for i in range(5):
    nome = input(f"Digite o {i + 1}º nome: ");
    nomes.append(nome);
    
nomes.sort();

os.system("cls || clear");
print("Nomes em ordem alfabética:");

for nome in nomes:
    print(nome);