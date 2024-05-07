import os

class Reserva:
    def __init__(self, numero_aviao, nome_passageiro):
        self.numero_aviao = numero_aviao
        self.nome_passageiro = nome_passageiro

# Inicialização dos vetores
avioes = [None] * 4
assentos_disponiveis = [0] * 4
reservas = []

def limpar_tela():
    os.system("cls || clear")


def registrar_avioes():
    limpar_tela()
    
    print("Informe o número de cada avião:")
    for i in range(4):
        avioes[i] = input(f"Avião {i+1}: ")

def registrar_assentos_disponiveis():
    limpar_tela()
    print("Informe a quantidade de assentos disponíveis para cada avião:")
    for i in range(4):
        assentos_disponiveis[i] = int(input(f"Assentos disponíveis para o avião {avioes[i]}: "))

def realizar_reserva():
    limpar_tela()
    
    if len(reservas) >= 10:
        print("Limite de reservas atingido!")
        return
    
    numero_aviao = input("Informe o número do avião: ")
    if numero_aviao not in avioes:
        print("Este avião não existe!")
        return
    
    indice_aviao = avioes.index(numero_aviao)
    if assentos_disponiveis[indice_aviao] == 0:
        print("Não há assentos disponíveis para este avião!")
        return
    
    nome_passageiro = input("Informe o nome do passageiro: ")
    reservas.append(Reserva(numero_aviao, nome_passageiro))
    assentos_disponiveis[indice_aviao] -= 1
    print("Reserva realizada com sucesso!")
    
    
def realizar_consulta_aviao():
    limpar_tela()
    
    numero_escolhido_aviao = input("Digite o número do avião desejado: ")
    if numero_escolhido_aviao not in avioes:
        print("Este avião não existe!")
        return;
    
    reservas_aviao = []
    for reserve in reservas:
        if reserve.numero_aviao == numero_escolhido_aviao:
            reservas_aviao.append(reserve)
            
    if not reservas_aviao:
        print("Não há reservas realizadas para este avião!")
    else:
        for reserve in reservas_aviao:
            print(f"Passageiro(a): {reserve.nome_passageiro}");
            
def realizar_consulta_passageiro():
    limpar_tela()
    
    nome_passageiro = input("Digite o nome do passageiro: ")
    
    reservas_passageiro = []
    for passageiro in reservas:
        if passageiro.nome_passageiro == nome_passageiro:
            reservas_passageiro.append(passageiro)
            
    if not reservas_passageiro:
        print("Não há reservas realizadas para este passageiro!")
    else:
        for passageiro in reservas_passageiro:
            print(f"{passageiro.nome_passageiro} está no avião {passageiro.numero_aviao}")
    
def menu():
    print("\nMenu:")
    print("1. Registrar número de cada avião")
    print("2. Registrar quantitativo de assentos disponíveis em cada avião")
    print("3. Reservar passagem aérea")
    print("4. Realizar consulta por avião")
    print("5. Realizar consulta por passageiro")
    print("6. Encerrar")

# Programa principal
while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        registrar_avioes()
    elif opcao == 2:
        registrar_assentos_disponiveis()
    elif opcao == 3:
        realizar_reserva()
    elif opcao == 4:
        realizar_consulta_aviao()
    elif opcao == 5:
        realizar_consulta_passageiro()
    elif opcao == 6:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
