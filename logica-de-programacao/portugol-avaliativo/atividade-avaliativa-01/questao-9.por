programa
 {
	
	funcao inicio()
 {
		cadeia nome
		inteiro valorTotalDoEmprestimo, rendaMensalDoSolicitante, numeroPrestacoes
		real valorPrestacao

		escreva("Digite seu nome: ")
		leia(nome)

		escreva("Sua renda mensal: ")
		leia(rendaMensalDoSolicitante)

		escreva("Valor total do emprestimo solicitado: ")
		leia(valorTotalDoEmprestimo)

		escreva("Número de prestações: ")
		leia(numeroPrestacoes)

		valorPrestacao = valorTotalDoEmprestimo / numeroPrestacoes
		

		se (valorTotalDoEmprestimo <= 10 * rendaMensalDoSolicitante e valorPrestacao <= (30 * rendaMensalDoSolicitante) / 100 ) {
			escreva("Caro ", nome , " o senhor(a) está apto a receber o emprestimo")
		} senao {
			escreva("Caro ", nome , " o senhor(a) NÃO está apto a receber o emprestimo")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 729; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
