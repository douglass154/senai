programa {
	// Elabore um algoritmo para ler o nome de um aluno, sua idade e quatro notas.

     // Calcular a média aritmética do aluno.

     // Mostrar: nome, idade, notas e média.
	funcao inicio() {
		// Definindo variáveis
		cadeia nome
		inteiro idade
		real primeiraNota, segundaNota, terceiraNota, quartaNota, media

		// Pedindo informações do usuário
		escreva("Qual o seu nome? : ")
		leia(nome)

		escreva("Quantos anos você tem? : ")
		leia(idade)

		escreva("Sua primeira nota: ")
		leia(primeiraNota)

		escreva("Sua segunda nota: ")
		leia(segundaNota)

		escreva("Sua terceira nota: ")
		leia(terceiraNota)

		escreva("Sua quarta nota: ")
		leia(quartaNota)
		limpa()

		// Calculo da média
		media = (primeiraNota + segundaNota + terceiraNota + quartaNota) / 4

		// Exibindo informações do usuário
		escreva("=== Exibindo informações do usuário ===")

		escreva("\n\nPrimeira nota: ", primeiraNota)
		escreva("\nSegunda nota: ", segundaNota)
		escreva("\nTerceira nota: ", terceiraNota)
		escreva("\nQuarta nota: ", quartaNota)

		escreva("\nMedia: ", media)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 651; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */