package ex03;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String userPassword = "alfa";

        System.out.print("Digite a sua senha: ");
        String password = sc.next();

        if(password.contains(userPassword)) {
            System.out.println("Senha correta!");
        } else {
            System.out.println("Senha incorreta!");
        }

        sc.close();
    }
}
