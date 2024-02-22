programa {
	/* O IMC – Índice de Massa Corporal é um critério da
	Organização Mundial de Saúde para dar uma indicação sobre
	a condição de peso de uma pessoa adulta.

	A fórmula é: IMC = Peso(kg) / altura(m) * altura(m)

	Elabore um algoritmo que leia
	o peso e a altura de um adulto
	e mostre sua condição de
	acordo com a tabela ao lado. */

	inclua biblioteca Matematica-->mat
	
	funcao inicio() {
		// Definindo variáveis
		cadeia nome
		real peso, altura, imc, imcArredondado

		// Solicitando informações
		escreva("Digite seu nome: ")
		leia(nome)

		escreva("Digite sua altura: ")
		leia(altura)

		escreva("Digite seu peso: ")
		leia(peso)
		limpa()

		// Calculo
		imc = peso / (altura * altura)
		
		imcArredondado = mat.arredondar(imc, 2)

		// Exibindo informações do usuário
		escreva("=== Exibindo Informações ===\n\n")
		escreva("Nome: ", nome ,"\n")
		escreva("Altura: ", altura ,"\n")
		escreva("Peso: ", peso ,"\n")
		escreva("IMC: ", imcArredondado ,"\n\n")

		// algoritmo
		se (imc <= 18.59) {
			escreva (nome, " de acordo com seu peso e sua altura, o seu imc (Índice de Massa Corporal) é ", imcArredondado , " e sua classificação é abaixo do peso.")
		}

		se (imc >= 18.6 e imc <= 24.99) {
			escreva (nome, " de acordo com seu peso e sua altura, o seu imc (Índice de Massa Corporal) é ", imcArredondado , " e sua classificação é peso ideal (Parabêns).")
		}

		se (imc >= 25 e imc <= 29.99) {
			escreva (nome, " de acordo com seu peso e sua altura, o seu imc (Índice de Massa Corporal) é ", imcArredondado , " e sua classificação é levemente acima do peso.")
		}

		se (imc >= 30 e imc <= 34.99) {
			escreva (nome, " de acordo com seu peso e sua altura, o seu imc (Índice de Massa Corporal) é ", imcArredondado , " e sua classificação é obesidade grau 1.")
		}

		se (imc >= 35 e imc <= 39.99) {
			escreva (nome, " de acordo com seu peso e sua altura, o seu imc (Índice de Massa Corporal) é ", imcArredondado , " e sua classificação é obesidade grau 2 (severa).")
		}

		se (imc >= 40) {
			escreva (nome, " de acordo com seu peso e sua altura, o seu imc (Índice de Massa Corporal) é ", imcArredondado , " e sua classificação é obesidade grau 3 (mórbida).")
		}

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1077; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */