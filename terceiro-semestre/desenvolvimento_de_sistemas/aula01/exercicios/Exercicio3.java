package exercicios;

import java.util.Scanner;

public class Exercicio3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Calculadora calc = new Calculadora();

        System.out.print("Digite o primeiro número para tirar a média: ");
        double n1 = sc.nextDouble();

        System.out.print("Digite o segundo: ");
        double n2 = sc.nextDouble();

        System.out.print("Digite o terceiro: ");
        double n3 = sc.nextDouble();

        calc.tirarMedia2(n1, n2, n3);

        sc.close();
    }
}
