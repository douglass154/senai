#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");
	
	int n1, ant, suces;
	
	printf("Digite um n�mero: ");
	scanf("%i", &n1);
	
	ant = n1 - 1;
	suces = n1 + 1;
	
	printf("O n�mero antecessor do n�mero que voc� digitou � %i \n", ant);
	printf("E o n�mero sucessor do n�mero que voc� digitou � %i \n", suces);
	
	return 0;
}
