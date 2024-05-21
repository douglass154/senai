import os;
os.system('cls || clear');

def pegarMedia(nota1, nota2):
    return (nota1 + nota2) / 2;

def resultado(media):
    if (media < 7):
       return 'Você está aprovado!!';
    return 'Você está reprovado';

nota1 = float(input('Digite a 1ª nota: '));
nota2 = float(input('Digite a 2ª nota: '));
media = pegarMedia(nota1, nota2);
resultado = resultado(media)

print(resultado);