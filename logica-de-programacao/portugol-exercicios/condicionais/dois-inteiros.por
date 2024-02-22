programa {
	// Elabore um algoritmo para receber dois inteiros como entrada do teclado e escreva na tela:

	// A média, a soma, o produto, o menor valor e o maior valor.

	// Usando uma linha para cada resultado.
	
	funcao inicio() {
		// Definindo variáveis
		inteiro primeiroNumero, segundoNumero
		inteiro soma, produto, menorValor, maiorValor, media

		// Solicitando Informações
		escreva("Escreva um número: ")
		leia(primeiroNumero)
		
		escreva("Escreva outro número: ")
		leia(segundoNumero)

		limpa()

		// Condicionais
		se (primeiroNumero > segundoNumero) {
			maiorValor = primeiroNumero
			menorValor = segundoNumero
		} senao {
			maiorValor = segundoNumero
			menorValor = primeiroNumero
		}

		// Calculo dos números
		soma = primeiroNumero + segundoNumero
		produto = primeiroNumero * segundoNumero
		media = (primeiroNumero + segundoNumero) / 2

		// Exibindo Informações
		escreva("\n=== Exibindo Informações ===")

		escreva("\n\nMédia: ", media)
		escreva("\nSoma: ", soma)
		escreva("\nProduto: ", produto)
		escreva("\nMaior valor: ", maiorValor)
		escreva("\nMenor valor: ", menorValor)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 714; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */