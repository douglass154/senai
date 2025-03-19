package aula06.ex002;

import java.util.ArrayList;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        // Criando um Scanner para entrada de dados do usuario
        Scanner sc = new Scanner(System.in);

        // Criando um ArrayList
        ArrayList<String> lista = new ArrayList<>();

        // Solicitando ao usuário que insira uma string
        System.out.print("Insira uma string: ");
        String entrada = sc.nextLine();

        // Adicionandno a string à lista
        lista.add(entrada);

        // Exibindo a lista
        System.out.println("Elementos da lista:");
        for (String dado : lista) {
            System.out.println(dado);
        }

        sc.close();
        
    }
}
