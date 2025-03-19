
import time;
import os;

numeros = [];
numerosNegativos = [];

contador = 0
numerosPositivos = 0;
somaPositivos = 0;

def pause(timer):
    time.sleep(timer);

def clearTerminal():
    os.system("cls || clear");

for i in range(10): 
    num = int(input(f"Digite o {i + 1}º número: "));
    numeros.append(num);
    clearTerminal();
    
    if(num < 0):
        numerosPositivos += 1;
        
print("Processando...");
pause(2.2);
clearTerminal();
        
for numero in numeros:
    if(numero < 0):
        numerosNegativos.append(numero);
    
    if(numero >= 0):
        somaPositivos += numero;
        
print(f"Números negativos: {numerosNegativos}");
print(f"Soma dos números positivos: {somaPositivos}");