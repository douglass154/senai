programa {
	
	funcao inicio() {
		cadeia nomeProduto
		inteiro quantidade
		real precoUnitario, precoTotal, desconto, precoDescontado

		desconto = 0

		escreva("Nome do produto desejado: ")
		leia(nomeProduto)

		escreva("Quantos produtos você deseja: ")
		leia(quantidade)

		precoUnitario = 7.50
		precoTotal = precoUnitario * quantidade

		se (quantidade <= 5) {
			desconto = precoTotal / (2*100)
		} senao se (quantidade > 5 e quantidade <= 10) {
			desconto = precoTotal / (3*100) 
		} senao se (quantidade > 10) {
			desconto = precoTotal / (5*100)
		}

		escreva("O valor a pagar é de R$ ", precoTotal - desconto)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 406; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */