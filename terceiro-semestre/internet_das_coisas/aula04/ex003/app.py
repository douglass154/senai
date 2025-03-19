
import os;

numeros = [];

def clearTerminal():
    os.system("cls || clear");
    
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "));
    numeros.append(num);
    
largestNumber = max(numeros);
soma = sum(numeros);

clearTerminal();
    
print(f"números: {numeros}");
print(f"Maior número: {largestNumber}");
print(f"Soma dos números: {soma}");
    