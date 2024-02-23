programa {
	
	funcao inicio() {
		real corVerde, corAzul, corAmarelo, corVermelho
		inteiro codigoCor

		corVerde = 10.00
		corAzul = 20.00
		corAmarelo = 30.00
		corVermelho = 40.00

		escreva("----------- Tabela de CD's -----------\n\n")
		escreva("Cores:\n\n")
		escreva("(1)Verde \n(2)Azul \n(3)Amarelo \n(4)Vermelho \n\n")

		escreva("Escolha uma das opções pela numeração: ")
		leia(codigoCor)

		escolha(codigoCor) {
			caso 1: escreva("\nEste CD custa R$ ", corVerde)
			pare
			caso 2: escreva("\nEste CD custa R$ ", corAzul)
			pare
			caso 3: escreva("\nEste CD custa R$ ", corAmarelo)
			pare
			caso 4: escreva("\nEste CD custa R$ ", corVermelho)
			pare
			caso contrario: escreva("\nEste código não existe, escolha um código válido!!")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 703; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */