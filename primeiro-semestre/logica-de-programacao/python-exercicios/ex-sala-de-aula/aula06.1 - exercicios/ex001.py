import os
os.system('cls || clear')

codigos = []
nomesPratos = []


def mostrarPratosEscolhidos(opcao):
    if (opcao == 1):
        print("1- Pão com ovo | R$25.00")
        nomesPratos.append('Pão com ovo')
        codigos.append(1)
        preco = 25.00
        
    elif (opcao == 2):
        print('2- Lasanha  | R$45.00')
        nomesPratos.append('Lasanha')
        codigos.append(2)
        preco = 45.00
        
    elif (opcao == 3):
        print('3- Feijão com arroz  | R$35.00')
        nomesPratos.append('Feijão com arroz')
        codigos.append(3)
        preco = 35.00
        
    elif (opcao == 4):
        print('4- Macarronada  | R$38.00')
        nomesPratos.append('Macarronada')
        codigos.append(4)
        preco = 38.00
        
    elif (opcao == 5):
        print('5- Salada  | R$15.00')
        nomesPratos.append('Salada')
        codigos.append(5)
        preco = 15.00
        
    elif (opcao == 6):
        print('6- Sushi  | R$20.00')
        nomesPratos.append('Sushi')
        codigos.append(6)
        preco = 20.00
        
    elif (opcao == 7):
        print('7- Strogonoff  | R$18.00')
        nomesPratos.append('Strogonoff')
        codigos.append(7)
        preco = 18.00
        
    elif (opcao == 0):
        print('Saindo...')
    
    
def precosDosPratos(opcao):
    if (opcao == 1):
        preco = 25.00
        
    if (opcao == 2):
        preco = 45.00
        
    if (opcao == 3):
        preco = 35.00
        
    if (opcao == 4):
        preco = 38.00
        
    if (opcao == 5):
        preco = 15.00
        
    if (opcao == 6):
        preco = 20.00
        
    if (opcao == 7):
        preco = 18.00
        
    return preco;


def calculaPreco(opcao):
    preco = [];
    preco.append(precosDosPratos(opcao));
        
    return sum(preco);
    

def escolhaPrato():
    print('Código |     Pratos       |    Preço   |')
    print('-=' * 30)
    print('   1   |   Pão com ovo    |   R$25.00  |')
    print('   2   |     Lasanha      |   R$45.00  |')
    print('   3   | Feijão com arroz |   R$35.00  |')
    print('   4   |   Macarronada    |   R$38.00  |')
    print('   5   |     Salada       |   R$15.00  |')
    print('   6   |     Sushi        |   R$20.00  |')
    print('   7   |   Strogonoff     |   R$18.00  |')
    print('   0   |    Para sair     |    Grátis  |')
    print()
    opcao = int(input('Digite o código do prato: '))
    mostrarPratosEscolhidos(opcao)
    return opcao
    

opcao = escolhaPrato()
primeiroPreco = precosDosPratos(opcao);

def calcularPrecoTotalFinal(precoTotal, descontoOuAcrescimo, opcaoDePagamento):
    if opcaoDePagamento == 1:
        precoTotalFinalLocal = precoTotal - descontoOuAcrescimo
        return precoTotalFinalLocal #Desconto
    
    else: 
        precoTotalFinalLocal = precoTotal + descontoOuAcrescimo
        return precoTotalFinalLocal #Acrescimo

    
while opcao != 0:
    print()
    desejaMaisUmPrato = str(input('Deseja fazer mais um pedido?: ')).upper()
    
    if (desejaMaisUmPrato == 'S'):
        os.system('cls || clear')
        opcao = escolhaPrato()
        segundoPreco = calculaPreco(opcao);
        precoTotal = primeiroPreco + segundoPreco;
        descontoOuAcrescimo = 10 * precoTotal / 100
        
    else:
        os.system('cls || clear');
        print('Código  |  Forma de pagamento  |   Taxas/descontos')
        print('-=' * 40)
        print('  1     |       A Vista        |   desconto de 10%')
        print('  2     |   Cartão de crédito  |   acrescimo de 10%')
        print()
        
        opcaoDePagamento = int(input('Qual será seu método de pagamento(1 ou 2)?: '))
        precoTotalFinal = calcularPrecoTotalFinal(precoTotal, descontoOuAcrescimo, opcaoDePagamento)
        os.system('cls || clear')
    
        for i in range(len(nomesPratos)):
            print(f'Código do {i + 1}º prato: {codigos[i]} || Prato: {nomesPratos[i]}')
        print('-=' * 30)
        
        if opcaoDePagamento == 1:
            print('Opção de pagamento: A vista')
            print(f'Valor do desconto: {descontoOuAcrescimo}')
        else:
            print('Opção de pagamento: Cartão de crédito')
            print(f'Valor do acrescimo: {descontoOuAcrescimo}')
        
        print(f'Subtotal: {precoTotal}')
        print(f'Valor total final: {precoTotalFinal}')
        break
    
