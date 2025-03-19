package exercicios;
import java.util.Scanner;

public class Exercicio {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Calculadora calc = new Calculadora();

        System.out.print("Digite o primeiro número: ");
        double n1 = sc.nextDouble();

        System.out.print("Digite o segundo número: ");
        double n2 = sc.nextDouble();

        calc.somar(n1, n2);
        calc.subtrair(n1, n2);
        calc.multiplicar(n1, n2);
        calc.dividir(n1, n2);

        sc.close();
    }
}
