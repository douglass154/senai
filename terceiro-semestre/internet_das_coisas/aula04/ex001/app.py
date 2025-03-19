
numeros = [];

for i in range(3):
    num = int(input(f"Digite o {i + 1}º número: "));
    numeros.append(num);
    
biggestNumber = max(numeros);

print(f"O maior número é o {biggestNumber}");