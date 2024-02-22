programa {
	
	funcao inicio() {
		cadeia nome, sexo, estadoCivil
		inteiro tempoCasada
		

		escreva("Digite seu nome: ")
		leia(nome)
		
		escreva("Seu sexo (M) para Masculino e (F) para Feminino: ")
		leia(sexo)
		
		escreva("Qual o seu estado cívil casada(o) ou solteira(o): ")
		leia(estadoCivil)
		

		se (sexo == "F" e estadoCivil == "casada") {
			escreva("Digite quanto tempo você tem de casada (anos): ")
		}
		leia(tempoCasada)
		

		escreva("\n\n----- Exibindo informações do usuário -----\n\n")
		
		escreva("Nome: ", nome ,"\n")
		escreva("Sexo: ", sexo ,"\n")
		escreva("Estado Cívil: ", estadoCivil ,"\n")
		escreva("Tempo casada: ", tempoCasada ," anos")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 309; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */