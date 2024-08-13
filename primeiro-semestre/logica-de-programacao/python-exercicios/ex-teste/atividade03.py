"""
Utilizando vetores, crie um programa que leia o nome de um aluno, 4 notas e calcule a
média aritmética.

Verifique a situação do aluno considerando:
- Média igual ou maior que 7,0: Aprovado.
- Média entre 5,0 e 6,9: Recuperação.
- Média menor que 5,0: Reprovado.

Mostre os dados do aluno como: nome, suas 4 notas, média e situação conforme
solicitado acima.
"""

import os;

aluno = str(input('Digite seu nome: '));
notas = [];
soma = 0;
contador = 0;
i = 0;

for i in range(4):
    notasInput = float(input('Digite sua '+ str(i + 1)+ 'ª nota: '));
    notas.append(notasInput);

    soma = soma + notasInput;
    contador = contador + 1;


os.system('cls || clear');
media = soma / contador;

if media < 5:
    resultado = 'Reprovado';
elif media < 7:
    resultado = 'Recuperação';
else:
    resultado = 'Aprovado';


print('Nome do aluno:', aluno);

for i in range(4):
    print(str(i + 1)+ 'ª nota: ', str(notas[i]));

print('Situação do aluno', aluno,': ',resultado);