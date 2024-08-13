#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");
	
	float salario;
	float quantidadeSalarioMinino = 0;
	
	printf("Digite quanto você recebe de salário: ");
	scanf("%f", &salario);
	
	quantidadeSalarioMinino = salario / 1412;
	
	printf("A quantidade de salários mínimos que você recebe por mês é %.2f salário(s) mínimo(s)", quantidadeSalarioMinino);
	
	return 0;
}
