package exercicios.ex001;

import java.util.ArrayList;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Camisa> camisas = new ArrayList<>();
        
        while (true) {
            TshirtsTable();

            System.out.print("Digite o número da opção desejada: ");
            int option = sc.nextInt();

            switch (option) {
                case 1:
                    addNewTshirt(camisas);
                    break;
                case 2:
                    showAllTshirts(camisas);
                    break;
                case 3:
                    selectTypeOfUpdate(camisas);
                    break;
                case 4:
                    deleteTshirt(camisas);
                case 5:
                    System.out.println("Encerrando o programa...");
                    return;
                default:
                    System.out.println("Valor inválido");
                    continue;
            }
        
        }
        
    }

    public static void TshirtsTable() {
        System.out.println("");
        System.out.println("=== TABELA CAMISAS ===");
        System.out.println("");
        System.out.println("1. Adicionar nova Camisa");
        System.out.println("2. Ver camisas");
        System.out.println("3. Atualizar uma camisa");
        System.out.println("4. Excluir camisa");
        System.out.println("5. Encerrar programa");
        System.out.println("");
    }

    public static void addNewTshirt(ArrayList<Camisa> camisas) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite a cor da camisa: ");
        String color = sc.nextLine();

        System.out.print("Digite o tamanho da camisa: ");
        int size = sc.nextInt();
        sc.nextLine();
        
        System.out.print("Digite o tipo da camisa (exemplo - manga longa): ");
        String type = sc.nextLine();

        Camisa camisa = new Camisa(color, size, type);
        camisas.add(camisa);

        System.out.println("");
        System.out.println("Camisa adicionada com sucesso!");
    }
    
    public static void showAllTshirts(ArrayList<Camisa> camisas) {
        int count = 0;

        for (Camisa camisa : camisas) {
            System.out.println((count + 1) +"ª camisa: índice "+ count);
            System.out.println("Cor: "+ camisa.getColor());
            System.out.println("Tamanho: "+ camisa.getSize());
            System.out.println("Tipo: "+ camisa.getType());
            System.out.println("--------------------------------");

            count++;
        }
    }

    public static void selectTypeOfUpdate(ArrayList<Camisa> camisas) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o índice da camisa que deseja alterar: ");
        int indice = sc.nextInt();

        if(indice >= 0 && indice <= camisas.size()) {
            System.out.println("O que deseja alterar?");
            System.out.println("");
            System.out.println("1. Cor da camisa");
            System.out.println("2. Tamanho da camisa");
            System.out.println("3. Tipo da camisa");
            System.out.println("4. Alterar tudo");
            System.out.println("");
            System.out.print("Digite o número da opção que deseja atualizar: ");
            int option = sc.nextInt();

            updateTshirt(option, camisas, indice);
            return;
        }

        System.out.println("índice inválido:");
    }

    public static void updateTshirt(int option, ArrayList<Camisa> camisas, int indice) {
        Scanner sc = new Scanner(System.in);

        String newColor;
        int newSize;
        String newType;
        
        switch (option) {
            case 1:
                System.out.print("Digite a nova cor da camisa: ");
                newColor = sc.nextLine();
                camisas.get(indice).setColor(newColor);
                return;
            case 2:
                System.out.print("Digite o novo tamanho da camisa: ");
                newSize = sc.nextInt();
                camisas.get(indice).setSize(newSize);
                return;
            case 3:
                System.out.print("Digite o novo tipo da camisa: ");
                newType = sc.nextLine();
                camisas.get(indice).setType(newType);
            case 4:
                System.out.print("Digite a nova cor da camisa: ");
                newColor = sc.nextLine();
                
                System.out.print("Digite o novo tamanho da camisa: ");
                newSize = sc.nextInt();
                
                System.out.print("Digite o novo tipo da camisa: ");
                newType = sc.nextLine();

                camisas.get(indice).setColor(newColor);
                camisas.get(indice).setSize(newSize);
                camisas.get(indice).setType(newType);
                return;
            
            default:
                System.out.println("Não foi possível atualizar, valor inválido");
                break;
        }
    }

    public static void deleteTshirt(ArrayList<Camisa> camisas) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o índice da camisa que deseja alterar: ");
        int indice = sc.nextInt();

        if(indice >= 0 && indice <= camisas.size()) {
            camisas.remove(indice);
        }
    }

}
