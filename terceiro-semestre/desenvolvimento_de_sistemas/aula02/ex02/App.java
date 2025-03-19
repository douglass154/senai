package ex02;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite a sua nota: ");
        double nota = sc.nextDouble();

        if(nota >= 7) {
            System.out.println("Nota " + nota + ": Aprovado");
        } else {
            System.out.println("Nota " + nota + ": Reprovado");
        }

        sc.close();
    }
}
