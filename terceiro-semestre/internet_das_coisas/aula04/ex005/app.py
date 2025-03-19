
import os;

numeros = [];
contador = 0;

def clearTerminal():
    os.system("cls || clear");

for i in range(10): 
    num = int(input(f"Digite o {i + 1}º número: "));
    numeros.append(num);
    
    contador += 1
    
media = sum(numeros) / contador;

print(f"Média: {media}");