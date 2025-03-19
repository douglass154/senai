package ex004;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int operator;
        double n1 = 0;
        double n2 = 0;

        do {
            System.out.println("=== ESCOLHA A OPERAÇÃO ===");
            System.out.println("1 - SOMA");
            System.out.println("2 - SUBTRAÇÃO");
            System.out.println("3 - MULTIPLICAÇÃO");
            System.out.println("4 - DIVISÃO");
            System.out.println("5 - Sair");
            
            System.out.print("Escolha uma das opções acima pela numeração: ");
            operator = sc.nextInt();

            
            if(operator <= 4) {
                System.out.println("Agora escolha 2 números para fazer o calculo!");

                System.out.print("1º número: ");
                n1 = sc.nextDouble();
    
                System.out.print("2º número: ");
                n2 = sc.nextDouble();
            }

            switch (operator) {
                case 1:
                    System.out.println(n1 + " + " + n2 + " é igual a " + (n1 + n2));
                    break;
                case 2:
                    System.out.println(n1 + " - " + n2 + " é igual a " + (n1 - n2));
                    break;
                case 3:
                    System.out.println(n1 + " * " + n2 + " é igual a " + (n1 * n2));
                    break;
                case 4:
                    System.out.println(n1 + " / " + n2 + " é igual a " + (n1 / n2));
                    break;
                case 5:
                    System.out.println("Saindo do Programa");
                    break;
                default:
                    System.out.println("Digite uma das opções validas! \n");
                    break;
            }
        } while(operator != 5);

        sc.close();
    }
}
