programa {
	// Elabore um algoritmo usando operações lógicas para ler 3
	// números e escrever:

 	// • Os 3 números informados.
	// • O maior número;
	// • O menor número;
	
	funcao inicio() {
		// Declarando variáveis
		inteiro primeiroNumero, segundoNumero, terceiroNumero, maiorNumero, menorNumero
		cadeia nome

		maiorNumero = 0
		menorNumero = 0

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

		// Algoritmo primeiro número
		se (primeiroNumero > segundoNumero e primeiroNumero > terceiroNumero) {
			maiorNumero = primeiroNumero
		} senao se (primeiroNumero < segundoNumero e primeiroNumero < terceiroNumero) {
			menorNumero = primeiroNumero
		}

		// Algoritmo segundo número
		se (segundoNumero > primeiroNumero e segundoNumero > terceiroNumero) {
			maiorNumero = segundoNumero
		} senao se (segundoNumero < primeiroNumero e segundoNumero < terceiroNumero) {
			menorNumero = segundoNumero
		}

		// Algoritmo terceiro número
		se (terceiroNumero > primeiroNumero e terceiroNumero > segundoNumero) {
			maiorNumero = terceiroNumero
		} senao se (terceiroNumero < primeiroNumero e terceiroNumero < segundoNumero) {
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
 * @POSICAO-CURSOR = 1383; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */