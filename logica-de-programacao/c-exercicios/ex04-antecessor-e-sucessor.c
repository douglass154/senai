#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");
	
	int n1, ant, suces;
	
	printf("Digite um número: ");
	scanf("%i", &n1);
	
	ant = n1 - 1;
	suces = n1 + 1;
	
	printf("O número antecessor do número que você digitou é %i \n", ant);
	printf("E o número sucessor do número que você digitou é %i \n", suces);
	
	return 0;
}
