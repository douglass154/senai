#include <stdio.h>

int main() {
	int n1, n2, soma, sub, mult, div;
	
	printf("Digite um numero: \n");
	scanf("%i",&n1);
	
	printf("Digite outro numero: \n");
	scanf("%i",&n2);
	
	soma = n1 + n2;
	sub = n1 - n2;
	mult = n1 * n2;
	div = n1 / n2;
	
	printf("=== Exibindo resultados === \n\n");
	
	printf("Soma: %i \n", soma);
	printf("Subtracao: %i \n", sub);
	printf("Multiplicacao: %i \n", mult);
	printf("Divisao: %i \n", div);
	
	return 0;
}
