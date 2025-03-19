
import time;
import os;

numeros = [];
contador = 1;

def pause(timer):
    time.sleep(timer);

def clearTerminal():
    os.system("cls || clear");

while True:
    num = int(input(f"Digite o {contador}º número: "));
    
    if(contador == 1):
        print("Para parar a execução do programa digite o número 0");
        pause(2);
        
    clearTerminal();
    
    if(num == 0):
        print("Saindo do programa...")
        pause(1.5);
        print("Programa Finalizado!");
        break;
    
    numeros.append(num);
    contador += 1;
    
soma = sum(numeros);

print(f"A soma de todos os números digitados é: {soma}");    