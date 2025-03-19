import java.util.Scanner;

public class Entrada2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        double n1 = sc.nextDouble();

        System.out.print("Digite o segundo número: ");
        double n2 = sc.nextDouble();

        double soma = n1 + n2;
        double subtracao = n1 - n2;
        double multiplicacao = n1 * n2;
        double divisao = n1 / n2;
        
        System.out.println("A soma dos seus número é: " + soma);
        System.out.println("A subtração dos seus número é: " + subtracao);
        System.out.println("A multiplicação dos seus número é: " + multiplicacao);
        System.out.printf("A divisão dos seus número é: %.1f%n", divisao);

        sc.close();
    }
}
