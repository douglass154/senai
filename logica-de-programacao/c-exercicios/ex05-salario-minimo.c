#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "");
	
	float salario;
	float quantidadeSalarioMinino = 0;
	
	printf("Digite quanto voc� recebe de sal�rio: ");
	scanf("%f", &salario);
	
	quantidadeSalarioMinino = salario / 1412;
	
	printf("A quantidade de sal�rios m�nimos que voc� recebe por m�s � %.2f sal�rio(s) m�nimo(s)", quantidadeSalarioMinino);
	
	return 0;
}
