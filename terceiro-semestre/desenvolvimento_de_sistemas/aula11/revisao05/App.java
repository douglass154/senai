import java.util.ArrayList;
import java.util.Scanner;

public class App {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        ArrayList<Livro> livros = new ArrayList<>();
        int option;

        do {
            menu();
            System.out.print("Digite a opção que deseja para prosseguir: ");
            option = sc.nextInt();
            sc.nextLine();
            
            switch(option) {
                case 1:
                    addNewBook(livros);
                    break;
                case 2:
                    showAllBooks(livros);
                    break;
                case 3:
                    editBookByIndex(livros);
                    break;
                case 4:
                    removeBookByIndex(livros);
                    break;
                case 5:
                    System.out.println("Encerrando o programa...");
                    break;
            }

        } while(option != 5);

    }

    public static void menu() {
        System.out.println();
        System.out.println("1. Adicionar um novo livro");
        System.out.println("2. Exibir todos os livros disponíveis");
        System.out.println("3. Alterar algum livro");
        System.out.println("4. Remover um livro");
        System.out.println("5. Encerrar programa");
        System.out.println();
    }

    public static void addNewBook(ArrayList<Livro> livros) {
        System.out.print("Título do livro: ");
        String nome = sc.nextLine();

        System.out.print("Nome do autor: ");
        String autor = sc.nextLine();

        System.out.print("Ano de publicação: ");
        int anoPublicacao = sc.nextInt();
        sc.nextLine();

        System.out.print("Preço: ");
        double preco = sc.nextDouble();
        sc.nextLine();

        if(preco < 0) {
            System.out.println("Não é possível adiconar um preço menor que 0");
            return;
        }

        Livro livro = new Livro(nome, autor, anoPublicacao, preco);
        livros.add(livro);

        System.out.println("Livro " + livro.getTitulo() + " adicionado com sucesso!");
    }

    public static void showAllBooks(ArrayList<Livro> livros) {
        livros.forEach(livro -> {
            livro.exibirInformacoes();
            System.out.println("");
        });
    }

    public static void editBookByIndex(ArrayList<Livro> livros) {
        String nome;
        String autor;
        int anoPublicacao;
        double preco;

        System.out.print("Digite o índice do livro que deseja alterar (1 pra cima): ");
        int index = sc.nextInt();

        if(index < 1 || index > livros.size()) {
            System.out.println("índice inválido ou inexistente, digite de 1 pra cima (1 é o primeiro livro)");
            return;
        }

        System.out.println();
        System.out.println("O que deseja editar?");
        System.out.println("1. Título");
        System.out.println("2. Autor");
        System.out.println("3. Ano de publicação");
        System.out.println("4. Preço");
        System.out.println("5. Todos");
        System.out.print("Digite sua opção aqui: ");
        int option = sc.nextInt();
        sc.nextLine();

        System.out.println();

        switch (option) {
            case 1:
                System.out.print("Digite o novo título: ");
                nome = sc.nextLine();
                livros.get(index - 1).setTitulo(nome);
                System.out.println("Título atualizado com sucesso!");
                return;
            case 2:
                System.out.print("Digite o novo autor: ");
                autor = sc.nextLine();
                livros.get(index - 1).setAutor(autor);
                System.out.println("Autor atualizado com sucesso!");
                return;
            case 3:
                System.out.print("Ano de publicação: ");
                anoPublicacao = sc.nextInt();
                livros.get(index - 1).setAnoPublicacao(anoPublicacao);
                System.out.println("Ano de publicação atualizado com sucesso!");
                return;
            case 4:
                System.out.print("Preço: ");
                preco = sc.nextDouble();
                livros.get(index - 1).setPreco(preco);
                System.out.println("Preço atualizado com sucesso!");
                return;
            case 5:
                System.out.print("Digite o novo título: ");
                nome = sc.nextLine();

                System.out.print("Digite o novo autor: ");
                autor = sc.nextLine();

                System.out.print("Ano de publicação: ");
                anoPublicacao = sc.nextInt();
                sc.nextLine();

                System.out.print("Preço: ");
                preco = sc.nextDouble();
                sc.nextLine();

                livros.get(index - 1).setTitulo(nome);
                livros.get(index - 1).setAutor(autor);
                livros.get(index - 1).setAnoPublicacao(anoPublicacao);
                livros.get(index - 1).setPreco(preco);
                System.out.println("Livro atualizado com sucesso!");

                return;
            default:
                System.out.println("Valor ínvalido");
                return;
        }
    }

    public static void removeBookByIndex(ArrayList<Livro> livros) {
        System.out.print("Digite o índice do livro que deseja excluir (1 pra cima): ");
        int index = sc.nextInt();
        sc.nextLine();

        if(index < 1 || index > livros.size()) {
            System.out.println("Valor inválido ou inexistente, digite de 1 pra cima (1 é o primeiro livro)");
            return;
        }

        livros.remove(index - 1);
        System.out.println("Livro removido com sucesso!");
    }
}
