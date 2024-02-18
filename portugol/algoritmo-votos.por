programa {
	// Elabore um algoritmo usando operações lógicas para informar se
	// uma pessoa é obrigada a votar.

	// Considere que a regra é que menores de 18 e maiores que 65 não
	// são obrigados a votar.
	
	funcao inicio() {
		// Definindo variáveis
		cadeia nome 
		inteiro idade

		// Solicitando informações do usuário
		escreva("Seu nome: ")
		leia(nome)

		escreva("Idade: ")
		leia(idade)
		limpa()

		// Exibindo informações na tela
		escreva ("=== Exibindo informações ===")
		escreva ("\n\nNome: ", nome)
		escreva ("\nIdade: ", idade)
		
		// Algoritmo
		se (idade < 18) {
			escreva ("\n\n", nome ," você não está apto a votar ainda!!")
		}
		se (idade > 18 e idade < 65) {
			escreva ("\n\n", nome ," você tem idade suficiente para votar.")
		}
		se (idade >= 65) {
			escreva ("\n\n", nome ," você está apto a votar, mas esteja ciente de que não é obrigado.")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 571; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */