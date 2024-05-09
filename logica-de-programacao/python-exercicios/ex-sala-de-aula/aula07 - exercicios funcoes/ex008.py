import os;

def desconto_vale_transporte(opcaoVale, salario):
    if opcaoVale.lower() == 's':
        return salario * (6 / 100);
    return 0;

def desconto_vale_refeicao(valor):
    return valor * (20 / 100);
    
def desconto_plano_saude():
    return 150;
    
def desconto_inss(salario):
    if salario <= 1100:
        return salario * (7.5 / 100);
    if salario <= 2203.48:
        return salario * (9 / 100);
    if salario <= 3305.22:
        return salario * (12 / 100);
    if salario <= 6433.57:
        return salario * (14 / 100);
        
    return 854.36;
    
def desconto_irrf(salario):
    if salario <= 2259.20:
        return 0;
    if salario <= 2826.65:
        return (salario * (7.5 / 100)) + 189.59;
    if salario <= 3751.05:
        return (salario * (15 / 100)) + 189.59;
    if salario <= 4664.68:
        return (salario * (22.5 / 100)) + 189.59;
        
    return (salario * (27.5 / 100)) + 189.59;
    
def calcularSalarioLiquido(salario, valeTrans, valeRef, planoSaude, inss, irff):
    salarioLiquido = salario - (valeTrans + valeRef + planoSaude + inss + irff);
    return salarioLiquido;
    
matricula = input('Digite sua mátricula: ');
senha = input('Digite sua senha: ');
os.system('cls || clear');

salario = float(input('\nDigite seu salário: R$'));
opcaoValeTransporte = input('Deseja receber vale transporte(s/n)? : ');
valorValeRefeicao = float(input('Valor do vale refeição fornecido pela empresa: R$'));

descontoValeTransporte = desconto_vale_transporte(opcaoValeTransporte, salario);
descontoValeRefeicao = desconto_vale_refeicao(valorValeRefeicao);
descontoPlanoDeSaude = desconto_plano_saude();
descontoINSS = desconto_inss(salario);
descontoIRFF = desconto_irrf(salario);

salarioLiquido = calcularSalarioLiquido(salario, descontoValeTransporte, descontoValeRefeicao, descontoPlanoDeSaude, descontoINSS, descontoIRFF);

print(f'\nDesconto do vale transporte: {descontoValeTransporte:.2f}');
print(f'Desconto do vale refeição: {descontoValeRefeicao:.2f}');
print(f'Desconto do plano de saúde: {descontoPlanoDeSaude}');
print(f'Desconto do INSS: {descontoINSS:.2f}');
print(f'Desconto do IRFF: {descontoIRFF:.2f}');

print(f'\nSeu salário é: {salarioLiquido:.2f}');