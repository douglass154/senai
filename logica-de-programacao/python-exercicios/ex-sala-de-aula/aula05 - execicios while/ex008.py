import os;
os.system('cls || clear');

salario = float(0);
contadorSalario = int(0);
somaSalario = float(0);
maiorIdade = int(0);
menorIdade = int(99999);
quantidadeMulheres = int(0);

print('Opções ||    Descrição');
print('  1    ||    Adicionar');
print('  2    || Exibir resultados');
print('  3    ||      Sair');

while True:
    opcao = int(input('Escolha a opção desejada: '));
    
    def escolhaOpcao(opcao):
        if(opcao == 1):
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
        
        if(opcao == 2):
            mediaSalario = somaSalario / contadorSalario;
            print(f'Média salárial: {mediaSalario}');