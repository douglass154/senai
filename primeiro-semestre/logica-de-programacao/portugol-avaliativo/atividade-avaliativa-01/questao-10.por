programa {
	funcao inicio() {
		caracter tipoDeCombustivel
		inteiro litros
		real precoGasolina, precoAlcool, precoTotal, precoTotalFinal, desconto
		precoGasolina = 6.59
		precoAlcool = 3.79
		precoTotal = 0
		precoTotalFinal = 0
		desconto = 0
		
		

		escreva("\t\t\t----------- Tabela de descontos -----------\n\n")
		escreva("\t\tA-álcool \t\t\t\t\t\t\t G-gasolina \n\n")
		escreva("Até 25 litros, desconto de 2% por litro \t\t Até 25 litros, desconto de 3% por litro\n")
		escreva("Acima de 25 litros, desconto de 4% por litro \t\t Acima de 25 litros, desconto de 5% por litro\n\n")

		escreva("Qual o tipo de combustível (A) ou (G): ")
		leia(tipoDeCombustivel)

		escreva("Quantos litros? : ")
		leia(litros)
		

		


		se (litros <= 25) {
			precoTotal = litros * precoAlcool
			desconto = precoTotal * 0.02
		} senao se (litros > 25) {
			precoTotal = litros * precoAlcool
			desconto = precoTotal * 0.04
		}

		se (litros <= 25) {
			precoTotal = litros * precoGasolina
			desconto = precoTotal * 0.03
		} senao se (litros > 25) {
			precoTotal = litros * precoGasolina
			desconto = precoTotal * 0.05
		}

		precoTotalFinal = precoTotal - desconto 

		escreva("O valor total deu R$ ", precoTotalFinal)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 246; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */