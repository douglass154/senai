package exercicios;

import java.util.Scanner;

public class Exercicio4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite a primeira palavra: ");
        String word = sc.next();

        System.out.print("Digite a segunda palavra: ");
        String secondWord = sc.next();

        System.out.println("Concatenação: " + word + " " + secondWord);

        sc.close();
    }
}
