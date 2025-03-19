import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Double[] numeros = new Double[10];
        int option;
        
        while (true) {
            System.out.println("");
            System.out.println("=== MENU ===");
            System.out.println("1. Adicionar um novo número");
            System.out.println("2. Exibir números");
            System.out.println("3. Remover um número");
            System.out.println("4. Finalizar programa");
            System.out.print("Escolha uma das opções (1-4): ");
            
        
            option = sc.nextInt();
            
            System.out.println("");

            switch (option) {
                case 1:
                    addNumber(numeros);
                    break;
                case 2:
                    showNumbers(numeros);
                    break;
                case 3:
                    deleteNumber(numeros);
                    break;
                case 4:
                    System.out.println("Saindo do programa...");
                    sc.close();
                    return;
                default:
                    System.out.println("Digite um valor válido.");
                    continue;
            }
        }
    }

    public static void addNumber(Double[] numeros) {
        Scanner sc = new Scanner(System.in);
        
        boolean added = false;

        for(int i = 0; i < numeros.length; i++) {
            if(numeros[i] == null) {
                System.out.print("Qual número deseja adicionar: ");
                numeros[i] = sc.nextDouble();

                System.out.println("Número adicionado com sucesso!");

                added = true;
                break;
            }
        }

        if(!added) {
            System.out.println("Não é possível adicionar mais números. A lista está cheia.");
        }
    }

    public static void showNumbers(Double[] numeros) {
        if(numeros[0] == null) {
            System.out.println("Não há números cadastrados!");
            return;
        };

        int contador = 1;
        
        System.out.println("Números na lista e seus índices:");
        for(Double numero : numeros) {
            if(numero == null) return;

            System.out.println(contador + "º número: " + numero + " - índice " + (contador - 1));
            contador++;
        }
    }

    public static void deleteNumber(Double[] numeros) {
        if(numeros[0] == null) {
            System.out.println("Não há números cadastrados!");
            return;
        };

        Scanner sc = new Scanner(System.in);

        System.out.print("Qual número da lista deseja excluir pelo índice (0 - 9): ");
        int index = sc.nextInt();

        if(index < 0 || index >= numeros.length || numeros[index] == null) {
            System.out.println("Indíce inválido ou posição vazia!");
            return;
        }

        for(int i = index; i < numeros.length - 1; i++) {
            numeros[i] = numeros[i + 1];
        }

        numeros[numeros.length - 1] = null;

        System.out.println("Número removido com sucesso!");
    }
}