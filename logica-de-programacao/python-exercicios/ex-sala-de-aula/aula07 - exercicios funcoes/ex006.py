import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")
    
def calcularIMC(peso, altura):
    return peso / (altura ** 2)
    
def reusltadosIMC(imc):
    if (imc < 18.5):
        return 'Abaixo do peso';
    if (imc < 25):
        return 'Peso normal';
    if (imc < 30):
        return 'Sobrepeso';
    if (imc < 35):
        return 'Obesidade grau 1';
    if (imc < 40):
        return 'Obesidade grau 2';
    return 'Obesidade grau 3 (mórbida)';
    

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []
imcs = []
resultados = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    sobrenome = str(input("Digite seu sobrenome: "))
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    imcs.append(calcularIMC(peso, altura))
    
for i in range(len(nomes)):
    resultados.append(reusltadosIMC(imcs[i]));

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print(f"Nome completo: {nomes[i]} {sobrenomes[i]}")
    print(f"Idade: {idades[i]}")
    print(f"Altura: {alturas[i]:.2f} metros")
    print(f"Peso: {pesos[i]:.2f} quilogramas")
    print(f"IMC: {imcs[i]:.2f}");
    print(f"Resultado: {resultados[i]}");
    print()
    print('-=' * 10);
    print()