
import os;
import random;
import time;

nomes = [];

for i in range(10):
    if(i == 0):
        print("Digite 10 nomes.");
        time.sleep(1.5);
        print("Iremos dizer qual é o seu par ideal :)");
        time.sleep(1.5);
        
    nome = input(f"Digite o {i + 1}º nome: ");
    nomes.append(nome);
    
os.system("cls || clear");

print("O nome do seu par é...");
time.sleep(2);
print(random.choice(nomes));
        