package ex06;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite um número: ");
        int num = sc.nextInt();

        if(num % 2 != 0) {
            System.out.println("O número " + num + " é impar");
        } else {
            System.out.println("O número " + num + " é par");
        }

        sc.close();
    }
}
