#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "portuguese");
	
	float valor, desconto, acrescimo, valorDescontado, valorAcrescido;
	
	printf("Digite um número qualquer: ");
	scanf("%f", &valor);
	
	desconto = valor * 0.10;
	acrescimo = valor * 0.10;
	
	valorDescontado = valor - desconto;
	valorAcrescido = valor + acrescimo;
	
	printf("O valor digitado com acrescimo de 10 porcento ficaria %.2f , e o valor com desconto ficaria %.2f", valorAcrescido, valorDescontado);
	
	return 0;
}
