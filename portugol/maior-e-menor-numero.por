programa {
	// Elabore um algoritmo usando operações lógicas para ler 3
	// números e escrever:

 	// • Os 3 números informados.
	// • O maior número;
	// • O menor número;
	
	funcao inicio() {
		// Declarando variáveis
		inteiro primeiroNumero, segundoNumero, terceiroNumero, maiorNumero, menorNumero
		cadeia nome

		// Solicitando informações do usuário
		escreva ("Seu nome: ")
		leia(nome)
		
		escreva ("Digite um número: ")
		leia(primeiroNumero)

		escreva ("Digite outro número: ")
		leia(segundoNumero)

		escreva ("Digite o terceiro número: ")
		leia(terceiroNumero)
		limpa()

		maiorNumero = primeiroNumero
		menorNumero = primeiroNumero

		// Algoritmo
		se (segundoNumero > maiorNumero) {
			maiorNumero = segundoNumero
		} senao se (segundoNumero < maiorNumero) {
			menorNumero = segundoNumero
		}

		senao se (terceiroNumero > maiorNumero) {
			maiorNumero = terceiroNumero
		} senao se (terceiroNumero < maiorNumero) {
			menorNumero = terceiroNumero
		}
		

		// Exibindo informações
		escreva("=== Exibindo Informações ===\n\n")
		escreva("Nome: ", nome, "\n")
		escreva("Os números informados são: ", primeiroNumero, ", ", segundoNumero, " e ", terceiroNumero, "\n\n")
		escreva("Maior número foi: ", maiorNumero, "\n")
		escreva("Menor número foi: ", menorNumero)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 655; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */