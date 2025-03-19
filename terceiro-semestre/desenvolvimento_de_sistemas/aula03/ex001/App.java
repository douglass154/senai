import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int option;

        do {
            System.out.println("=== MENU DE EMBALAGENS ===");
            System.out.println("1 - Caixa de Papelão");
            System.out.println("2 - Sacola Plástica");
            System.out.println("3 - Embalagem de Vidro");
            System.out.println("4 - Sair");
            
            System.out.print("Escolha uma das opções acima pela numeração: ");
            option = sc.nextInt();

            switch (option) {
                case 1:
                    System.out.println("Caixa de Papelão: Ideal para transporte e armazenamento. \n");
                    break;
                case 2:
                    System.out.println("Sacola plástica: Leve e prática, mas pouco sustentável. \n");
                    break;
                case 3:
                    System.out.println("Embalagem de vidro: Resistente e reutilizável. \n");
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