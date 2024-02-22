programa {
	// Elabore um algoritmo para resolver a seguinte questão:

	// As maçãs custam R$ 1,30 cada se forem compradas menos de uma
 	// dúzia, e R$ 1,00 se forem compradas pelo menos 12.

 	// Escreva um programa que leia o número de maçãs compradas,
	// calcule e escreva o custo total da compra.

	inclua biblioteca Matematica-->mat
	
	funcao inicio() {
		// Definindo variáveis
		inteiro numeroDeMacas
		real primeiroPreco, segundoPreco, arredondaPrimeiroPreco, arredondaSegundoPreco

		escreva("Quantas maçãs você quer: ")
		leia(numeroDeMacas)

		primeiroPreco = 1.31 * numeroDeMacas
		segundoPreco = 1.01 * numeroDeMacas
		
		arredondaPrimeiroPreco = mat.arredondar(primeiroPreco, 2)
		arredondaSegundoPreco = mat.arredondar(segundoPreco, 2)

		// Algoritmo
		se (numeroDeMacas >= 12) {
			escreva ("Vai lhe custar R$", arredondaSegundoPreco)
		} senao {
			escreva ("Vai lhe custar R$", arredondaPrimeiroPreco)
		}
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 857; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */