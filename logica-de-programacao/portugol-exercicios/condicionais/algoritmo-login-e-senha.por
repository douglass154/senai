programa {
	//Elabore um algoritmo para receber o login e senha de um usuário.

	// Caso o usuário e senha estejam corretos, mostre a mensagem “Bem-
	// vindo!”, caso contrário, mostre a mensagem “Login ou senha inválidos.”
 	
	funcao inicio() {
		// DEFININDO VARIÁVEIS
		cadeia nome, emailRegistro, senhaRegistro, emailLogin, senhaLogin

		// REGISTRANDO INFORMAÇÕES DO USUÁRIO
		escreva("Página de registro")
		
		escreva("\nNome: ")
		leia(nome)
		
		escreva("Email: ")
		leia(emailRegistro)

		escreva("Senha: ")
		leia(senhaRegistro)
		limpa()

		// CONFERINDO INFORMAÇÕES COM O USUÁRIO
		escreva("Página de login")

		escreva("\nDigite seu email: ")
		leia(emailLogin)
		
		escreva("\nDigite sua senha: ")
		leia(senhaLogin)
		
		// CONDIÇÕES
		se (emailLogin == emailRegistro e senhaLogin == senhaRegistro) {
			escreva("Bem-vindo! ", nome)
		} senao {
			escreva ("Login ou senha inválidos!")
		}
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 913; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */