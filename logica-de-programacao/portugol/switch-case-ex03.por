programa {

  funcao inicio() {
    // Definindo vari�ves
    inteiro diaSemana

    escreva("(1) Domingo \t\t\t\t(4) Quinta-feira \n(2) Segunda-feira \t(5) Sexta-feira \n(3) Ter�a-feira \t\t(6) S�bado \n(4) Quarta-feira \n\nDigite um n�mero de acordo com as op��es acima: ")
    leia(diaSemana)

    escolha(diaSemana) {
      caso 1: escreva("\nDomingo: Fim de Semana")
      pare
      caso 2: escreva("\nSegunda-Feira: Dia �til")
      pare
      caso 3: escreva("\nTer�a-feira: Dia �til")
      pare
      caso 4: escreva("\nQuarta-feira: Dia �til")
      pare
      caso 5: escreva("\nQuinta-feira: Dia �til")
      pare
      caso 6: escreva("\nSexta-feira: Dia �til")
      pare
      caso 7: escreva("\nS�bado: Fim de semana")
      pare
      caso contrario: escreva("Escolha um n�mero v�lido")
    }

  }
}
