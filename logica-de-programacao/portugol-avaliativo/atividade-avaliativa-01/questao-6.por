programa {
	
	funcao inicio() {
		real primeiraNota, segundaNota, media
		cadeia nome

		escreva("Digite seu nome: ")
		leia(nome)

		escreva("Sua primeira nota: ")
		leia(primeiraNota)

		escreva("Sua segunda nota: ")
		leia(segundaNota)

		media = (primeiraNota + segundaNota) / 2

		se (media >= 6) {
			escreva("Parabêns, ", nome , " você passou, sua media é maior do que a exigida \n\nMédia ", media)
		} senao se (media >=4 e media <= 5.9) {
			escreva(nome, " você está de recuperação pois não alcançou a média exigida \n\nMédia ", media)
		} senao se (media < 4) {
			escreva(nome, " você está de recuperação pois não alcançou a média exigida \n\nMédia ", media)
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 679; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */