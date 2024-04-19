import os;
os.system('cls || clear');

salario = float(0);
contadorSalario = int(0);
somaSalario = float(0);
maiorIdade = int(0);
menorIdade = int(99999);
quantidadeMulheres = int(0);

<<<<<<< HEAD
print('Opções ||       Descrição');
print('  1    || Adicionar informações');
print('  2    ||   Exibir resultados');
print('  3    ||         Sair');
opcao = str(input('Escolha a opção desejada: '));

while opcao != '3':
    os.system('cls || clear');
    
    def escolhaOpcao(opcao):
        if(opcao == '1'):
=======
print('Opções ||    Descrição');
print('  1    ||    Adicionar');
print('  2    || Exibir resultados');
print('  3    ||      Sair');

while True:
    opcao = int(input('Escolha a opção desejada: '));
    
    def escolhaOpcao(opcao):
        if(opcao == 1):
>>>>>>> refs/remotes/origin/main
            idade = int(input('Digite sua idade: '));
            sexo = str(input('Digite seu sexo(M/F): '));
            salario = float(input('Digite seu salário: '));
            contadorSalario += 1;
            somaSalario += salario;
            
            if(idade > maiorIdade):
                maiorIdade = idade;
            if(idade < menorIdade):
                menorIdade = idade;
            if((sexo == 'F' or sexo == 'f') and salario >= 5000):
                quantidadeMulheres += 1;
        
<<<<<<< HEAD
        if(opcao == '2'):
            mediaSalario = somaSalario / contadorSalario;
            print(f'Média salárial: {mediaSalario}');
            print(f'Menor idade: {menorIdade}');
            print(f'Maior idade: {maiorIdade}');
            print(f'Quantidade de mulheres que recebem mais de R$5000: {quantidadeMulheres}');    

        if(opcao == '3'):
            print('Fim!!');
    
    escolhaOpcao(opcao);
    print('Opções ||       Descrição');
    print('  1    || Adicionar informações');
    print('  2    ||   Exibir resultados');
    print('  3    ||         Sair');
    opcao = str(input('Escolha a opção desejada: '));
=======
        if(opcao == 2):
            mediaSalario = somaSalario / contadorSalario;
            print(f'Média salárial: {mediaSalario}');
>>>>>>> refs/remotes/origin/main
