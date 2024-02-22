programa {
	// 3. Elabore um algoritmo para ler o nome de um aluno, sua idade
	// (em anos) e as três notas. Calcular a média do aluno.

	// Caso a média do aluno seja menor que 7, o aluno está reprovado.

   	// Mostrar: nome, idade, média e se está aprovado ou reprovado. 
	
	funcao inicio() {
		// Declarando variáveis
		cadeia nome
		inteiro idade
		real primeiraNota, segundaNota, terceiraNota, soma, media

		// Solicitando informações
		escreva("Digite seu nome: ")
		leia(nome)

		escreva("Digite sua idade: ")
		leia(idade)
		
		escreva("Digite sua primeira nota: ")
		leia(primeiraNota)
		
		escreva("Digite sua segunda nota: ")
		leia(segundaNota)
		
		escreva("Digite sua terceira nota: ")
		leia(terceiraNota)

		limpa()

		//Calculo das médias
		soma = primeiraNota + segundaNota + terceiraNota
		media = soma / 3

		// Exibindo informações do usuário
		escreva("\n=== Exibindo informações do usuário ===")
		
		escreva("\n\nNome: ", nome)
		escreva("\nIdade: ", idade)
		escreva("\nMédia: ", media)

		se (media >=7) {
			escreva ("\n\nParabêns, você foi aprovado com média ", media)
		} senao {
			escreva ("\n\nVocê não bateu a meta exigida de 7 pontos e foi reprovado.\n Média: ", media)
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 944; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */