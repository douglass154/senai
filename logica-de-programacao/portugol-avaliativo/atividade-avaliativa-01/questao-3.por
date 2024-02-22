programa {
	
	funcao inicio() {
		inteiro primeiroValor, segundoValor, resultado

		escreva("Digite um número: ")
		leia(primeiroValor)

		escreva("Digite m segundo número: ")
		leia(segundoValor)
		limpa()

		se (primeiroValor == segundoValor) {
			resultado = primeiroValor + segundoValor
		} senao {
			resultado = primeiroValor * segundoValor
		}
		

		escreva("----- Resultados -----\n\n")

		escreva("O resultado dos seus números é: ", resultado)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 457; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */