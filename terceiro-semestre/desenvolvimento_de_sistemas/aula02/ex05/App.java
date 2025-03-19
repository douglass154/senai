package ex05;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite sua primeira nota: ");
        double firstNote = sc.nextDouble();

        System.out.print("Digite sua segunda nota: ");
        double secondNote = sc.nextDouble();

        double media = (firstNote + secondNote) / 2;

        if(media >= 7) {
            System.out.println("Média " + media + ": Você foi aprovado!");
        } else {
            System.out.println("Média " + media + ": Você foi reprovado.");
        }

        sc.close();
    }
}
