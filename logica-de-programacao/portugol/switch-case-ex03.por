programa {

  funcao inicio() {
    // Definindo variáves
    inteiro diaSemana

    escreva("(1) Domingo \t\t\t\t(4) Quinta-feira \n(2) Segunda-feira \t(5) Sexta-feira \n(3) Terça-feira \t\t(6) Sábado \n(4) Quarta-feira \n\nDigite um número de acordo com as opções acima: ")
    leia(diaSemana)

    escolha(diaSemana) {
      caso 1: escreva("\nDomingo: Fim de Semana")
      pare
      caso 2: escreva("\nSegunda-Feira: Dia útil")
      pare
      caso 3: escreva("\nTerça-feira: Dia útil")
      pare
      caso 4: escreva("\nQuarta-feira: Dia útil")
      pare
      caso 5: escreva("\nQuinta-feira: Dia útil")
      pare
      caso 6: escreva("\nSexta-feira: Dia útil")
      pare
      caso 7: escreva("\nSábado: Fim de semana")
      pare
      caso contrario: escreva("Escolha um número válido")
    }

  }
}
