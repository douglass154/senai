package ex002;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int option;

        do {
            System.out.println("=== MENU DE CANETAS ===");
            System.out.println("1 - Caneta Esferográfica");
            System.out.println("2 - Caneta em Gel");
            System.out.println("3 - Caneta de Tinteiro");
            System.out.println("4 - Sair");
            
            System.out.print("Escolha uma das opções acima pela numeração: ");
            option = sc.nextInt();

            switch (option) {
                case 1:
                    System.out.println("Caneta Esferográfica: Econômica e de longa duração. \n");
                    break;
                case 2:
                    System.out.println("Caneta Gel: Tinta mais pigmentada e escrita suave. \n");
                    break;
                case 3:
                    System.out.println("Caneta Tinteiro: Clássica e elegante, usada para caligrafia. \n");
                    break;
                case 4:
                    System.out.println("Saindo do programa. \n");
                    break;
                default:
                    System.out.println("Digite uma das opões pelo número \n");
                    break;
            }
        } while(option != 4);

        sc.close();
    }
}
