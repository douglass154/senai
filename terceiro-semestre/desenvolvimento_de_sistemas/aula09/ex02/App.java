import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Animal> animais = new ArrayList<>();
        
        while (true) {
            System.out.println("\nMenu:");
            System.out.println("1 - Adicionar novo animal");
            System.out.println("2 - Fazer um animal emitir som");
            System.out.println("3 - Sair");
            System.out.print("Escolha uma opção: ");
            
            int opcao = scanner.nextInt();
            scanner.nextLine();
            
            switch (opcao) {
                case 1:
                    System.out.println("Qual animal deseja adicionar? (Cachorro/Gato)");
                    String tipo = scanner.nextLine().toLowerCase();
                    if (tipo.equals("cachorro")) {
                        animais.add(new Cachorro());
                        System.out.println("Cachorro adicionado!");
                    } else if (tipo.equals("gato")) {
                        animais.add(new Gato());
                        System.out.println("Gato adicionado!");
                    } else {
                        System.out.println("Tipo de animal desconhecido!");
                    }
                    break;
                
                case 2:
                    if (animais.isEmpty()) {
                        System.out.println("Nenhum animal cadastrado!");
                    } else {
                        System.out.println("Escolha um animal para ouvir o som:");
                        for (int i = 0; i < animais.size(); i++) {
                            System.out.println((i + 1) + " - " + animais.get(i).getNome());
                        }
                        System.out.print("Opção: ");
                        int escolha = scanner.nextInt();
                        scanner.nextLine();
                        
                        if (escolha > 0 && escolha <= animais.size()) {
                            animais.get(escolha - 1).fazerSom();
                        } else {
                            System.out.println("Opção inválida!");
                        }
                    }
                    break;
                
                case 3:
                    System.out.println("Saindo...");
                    scanner.close();
                    return;
                
                default:
                    System.out.println("Opção inválida!");
            }
        }
    }
}
