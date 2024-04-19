import os;
os.system('cls || clear');

notas = [];

for i in range(3):
    inputNotas = float(input(f'Digite a sua {i + 1}ª nota: '));
    notas.append(inputNotas);

media = sum(notas) / len(notas);

if (media < 5):
    resultado = 'Reprovado!!';
elif (media < 7):
    resultado = 'Recuperação!!';
else:
    resultado = 'Aprovado!!';

os.system('cls || clear');

for valor in range(len(notas)):
    print(f'{valor + 1}ª Nota: {notas[valor]}');

print(f'Média: {media:.1f}');
print(f'Resultado: {resultado}');