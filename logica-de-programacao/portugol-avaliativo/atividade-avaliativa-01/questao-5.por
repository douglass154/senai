programa {
	
	funcao inicio() {
		inteiro primeiroValor, segundoValor, resultado
		caracter codigo

		escreva("Digite um número: ")
		leia(primeiroValor)

		escreva("Digite um código de operação (+ - / *): ")
		leia(codigo)

		escreva("Digite outro valor: ")
		leia(segundoValor)
		

		escolha(codigo) {
			caso '+' : escreva("O resultado é: ", primeiroValor + segundoValor)
			pare
			caso '-': escreva("O resultado é: ", primeiroValor - segundoValor)
			pare
			caso '*': escreva("O resultado é: ",resultado = primeiroValor * segundoValor)
			pare
			caso '/': escreva("O resultado é: ", primeiroValor / segundoValor)
			pare
			caso contrario: escreva("Insira um código válido!!")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 308; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */