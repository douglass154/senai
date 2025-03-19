
nomes = [];

while True:
    nome = input("Digite um nome: ");
    
    if(nome.lower() == "exit"):
        print("Parando execução!");
        break;
    
    nomes.append(nome);
    
for nome in nomes:
    nomeConverted = nome.upper();
    
    if(nomeConverted[0] == "A"):
        print(nome);
        