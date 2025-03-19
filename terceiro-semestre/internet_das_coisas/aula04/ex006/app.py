import os;
import random;
import time

nomes = [];

def pause(timer):
    time.sleep(timer);

def clearTerminal():
    os.system("cls || clear");

for i in range(10):
    nome = input(f"Digite o {i + 1}º nome: ");
    nomes.append(nome);
    
nomeSorteado = random.choice(nomes);

clearTerminal();

print(f"O nome sorteado da vez foi...");
pause(1.5);

print(nomeSorteado);
