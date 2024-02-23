programa {
	funcao inicio() {
		caracter tipoDeCombustivel
		inteiro litros
		real precoGasolina, precoAlcool, precoTotal, precoTotalFinal, desconto

		precoTotal = 0

		escreva("\t\t\t----------- Tabela de descontos -----------\n\n")
		escreva("\t\tA-álcool \t\t\t\t\t\t\t G-gasolina \n\n")
		escreva("Até 25 litros, desconto de 2% por litro \t\t Até 25 litros, desconto de 3% por litro\n")
		escreva("Acima de 25 litros, desconto de 4% por litro \t\t Acima de 25 litros, desconto de 5% por litro\n\n")

		escreva("Qual o tipo de combustível (A) ou (G): ")
		leia(tipoDeCombustivel)

		escreva("Quantos litros? : ")
		leia(litros)
		

		precoGasolina = 6.59
		precoAlcool = 3.79


		escolha(tipoDeCombustivel) {
			caso 'A': precoTotal = litros * precoAlcool
			pare
			caso 'B': precoTotal = litros * precoGasolina
			pare
		}
		
		
		se (tipoDeCombustivel == 'A' e litros <= 25) {
			desconto = ((2 * precoAlcool * litros) / 100)
		} senao {
			desconto = ((4 * precoAlcool * litros) / 100)
		} 
		
		se (tipoDeCombustivel == 'G' e litros <= 25) {
			desconto = ((3 * precoGasolina * litros) / 100)
		} senao {
			desconto = ((5 * precoGasolina * litros) / 100)
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
 * @POSICAO-CURSOR = 166; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */