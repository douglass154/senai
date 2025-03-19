import random;
import time;
import os;
    
tentativas = 0;

numeroSorteado = random.randint(1, 100);

while True:        
    if(tentativas == 0):
        print("Jogo de adivinhações");
        time.sleep(1.5);
        print("Tente adivinhar qual o número escolhido pelo sistema!");
        time.sleep(1.5);
        print("Boa sorte e que comecem os jogos!!");
        time.sleep(1.5);
        os.system("cls || clear");
    
    tentativas += 1;
    num = int(input(f"Digite o {tentativas}º número: "));
    
    if(num < numeroSorteado):
        print("O número que você digitou é menor que o escolhido, tente novamente :)");
        time.sleep(2);
        os.system("cls || clear");
    elif(num > numeroSorteado):
        print("O número que você digitou é maior que o escolhido, tente novamente :)");
        time.sleep(2);
        os.system("cls || clear");
    else:
        print("Parabêns você acertou o número em cheio :)");
        time.sleep(2);
        print(f"Número de tentativas: {tentativas}");
        time.sleep(2);
        resposta = input("Deseja fazer mais um jogo? (Sim : Não): ");
        
        if(resposta.lower() == "sim"):
            print("Perfeito, vamos continuar :)");
            os.system("cls || clear");
            tentativas = 0;
            time.sleep(1);
            
            numeroSorteado = random.randint(1, 100);
            continue;
        if(resposta.lower() == "não" or resposta.lower() == "nao"):
            print("Obrigado por jogar!");
            time.sleep(2);
            os.system("cls || clear");
            break;