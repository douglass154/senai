programa {
	
	funcao inicio() {
		inteiro quantidadeMorango, quantidadeMaca, precoMorango, precoMaca
		real desconto, valorTotal

		precoMorango = 0
		precoMaca = 0

		escreva("----------- Tabela de Frutas e Preços -----------\n\n")
		escreva("\t\t     Até 5 Kg \t\t\t  Acima de 5 Kg \n\n")
		escreva("Morango \t R$ 2,50 por Kg \t\t R$ 2,20 por Kg \n")
		escreva("Maçã \t\t R$ 1,80 por Kg \t\t R$ 1,50 por Kg \n\n")

		escreva("Quantos Kg de morango você deseja? : ")
		leia(quantidadeMorango)

		escreva("Quantos Kg de maçã você deseja? : ")
		leia(quantidadeMaca)
		

		se (quantidadeMorango <= 5) {
			precoMorango = 2.50 * quantidadeMorango
		} senao se (quantidadeMorango > 5) {
			precoMorango = 2.20 * quantidadeMorango
		}

		se (quantidadeMaca <= 5) {
			precoMaca = 1.80 * quantidadeMaca
		} senao se (quantidadeMaca > 5) {
			precoMaca = 1.50 * quantidadeMaca
		}

		valorTotal = precoMaca + precoMorango
		desconto = (10 * 100) / (valorTotal * 1)

		se (valorTotal >= 25) {
			escreva("O valor a pagar pelas frutas é de R$ ", desconto) 
		} senao se (valorTotal < 25) {
			escreva("O valor a pagar pelas frutas é de R$ ", valorTotal)
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1154; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */