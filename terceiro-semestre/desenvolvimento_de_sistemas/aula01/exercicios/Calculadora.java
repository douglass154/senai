package exercicios;

public class Calculadora {
    public void somar(double n1, double n2) {
        double resultado = n1 + n2;
        System.out.println("A soma dos seus números é: " + resultado);
    };

    public void subtrair(double n1, double n2) {
        double resultado = n1 - n2;
        System.out.println("A subtração dos seus números é: " + resultado);
    };

    public void multiplicar(double n1, double n2) {
        double resultado = n1 * n2;
        System.out.println("A multiplicação dos seus números é: " + resultado);
    };

    public void dividir(double n1, double n2) {
        double resultado = n1 / n2;
        System.out.println("A divisão dos seus números é: " + resultado);
    };

    public void tirarMedia(double n1, double n2) {
        double resultado = (n1 + n2) / 2;
        System.out.printf("A média dos dois números é: %.2f%n", resultado);
    };

    public void tirarMedia2(double n1, double n2, double n3) {
        double resultado = (n1 + n2 + n3) / 3;
        System.out.printf("A média de todos os seus números é: %.2f%n", resultado);
    };

    public void calcularTrabalho(double forca, double distancia) {
        double trabalho = forca * distancia;
        System.out.println("O trabalho é igual a: " + trabalho);
    }

    public void calcularIMC(double peso, double altura) {
        double imc = peso / (altura * altura);
        System.out.printf("O calculo do seu imc é: %.2f%n", imc);
    }
}
