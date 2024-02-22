programa {
	// 1. Elabore um algoritmo para ler um valor e escrever a mensagem:
     // É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário
     // escrever “NÃO É MAIOR QUE 10!
     
	funcao inicio() {
		inteiro valor

		escreva("digite um valor: ")
		leia(valor)
		limpa()

		se (valor > 10) {
			escreva (valor, " É MAIOR QUE 10!")
		} senao se (valor == 10) {
			escreva (valor, " É IGUAL A 10!")
		} senao {
			escreva (valor, " É MENOR QUE 10!")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 473; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */