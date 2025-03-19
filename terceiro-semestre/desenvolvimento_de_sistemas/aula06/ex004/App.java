package aula06.ex004;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Cadastro> contatos = new ArrayList<>();
        
        while (true) {
            int opcao = opcoesCadastro();
            
            if(opcao == 4) {
                System.out.println("Saindo do programa...");
                break;
            }
    
            switch (opcao) {
                case 1:
                    cadastrar(contatos);
                    break;
                case 2:
                    listarContatos(contatos);
                    break;
                case 3:
                    removerContato(contatos);
                    break;
                default:
                    System.out.println("Valor inválido");
                    break;
            }
        }

        sc.close();
    }

    public static int opcoesCadastro() {
        Scanner sc = new Scanner(System.in);

        System.out.println("");
        System.out.println("=== Opções ===");
        System.out.println("1. Cadastro");
        System.out.println("2. Listar");
        System.out.println("3. Excluir");
        System.out.println("4. Sair");
        
        System.out.print("Escolha uma das opções: ");
        int opcao = sc.nextInt();

        System.out.println("");

        return opcao;
    }

    public static void cadastrar(ArrayList<Cadastro> contatos) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o nome: ");
        String nome = sc.nextLine();

        System.out.print("Digite o telefone: ");
        String phone = sc.nextLine();

        Cadastro user = new Cadastro(nome, phone);
        contatos.add(user);
    }

    public static void listarContatos(ArrayList<Cadastro> contatos) {
        int count = 1;
        
        for(Cadastro contato : contatos) {
            System.out.println(count +"º contato:");
            System.out.println("Nome: "+ contato.getName());
            System.out.println("Telefone: "+ contato.getPhone());
            System.out.println("");

            count++;
        }
    }

    public static void removerContato(ArrayList<Cadastro> contatos) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Digite o nome do contato que deseja excluir: ");
        String nome = sc.nextLine();

        Iterator<Cadastro> iterator = contatos.iterator();

        while(iterator.hasNext()) {
            Cadastro contato = iterator.next();

            if(contato.getName().equals(nome)) {
                iterator.remove();
                System.out.println("Contato removido com sucesso!");
                return;
            }
        }

        System.out.println("Contato não econtrado.");
    }
}
