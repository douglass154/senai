
numeros = [];

while True:
    num = int(input("Digite um número: "));
    
    if(num <= 0):
        print("Parando execução");
        break;
    
    numeros.append(num);
    
for numero in numeros:
    if(numero % 2 == 0):
        print(numero);