package ex003;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int option;

        do {
            System.out.println("=== MENU DE MOCHILAS ===");
            System.out.println("1 - Mochila Escolar");
            System.out.println("2 - Mochila de Viagens");
            System.out.println("3 - Mochila Esportiva");
            System.out.println("4 - Sair");
            
            System.out.print("Escolha uma das opções acima pela numeração: ");
            option = sc.nextInt();

            switch (option) {
                case 1:
                    System.out.println("Mochila Escolar: Compacta e ideal para estudantes. \n");
                    break;
                case 2:
                    System.out.println("Mochila de Viagem: Espaçosa, ideal para longas jornadas. \n");
                    break;
                case 3:
                    System.out.println("Mochila Esportiva: Leve, resistente e ergonômica. \n");
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
