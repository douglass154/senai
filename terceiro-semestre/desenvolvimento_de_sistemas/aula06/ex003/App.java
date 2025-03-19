package aula06.ex003;

import java.util.ArrayList;

public class App {
    public static void main(String[] args) {
        
        ArrayList<String> nomes = new ArrayList<>();
        nomes.add("Douglas");
        nomes.add("Icaro");
        nomes.add("Augusto");

        // Listando todos os objetos da lista
        System.out.println("Primeiros nomes: "+ nomes);

        // Acessando o elemento pelo índice
        System.out.println(nomes.get(0));

        // Iterando sobre os elementos
        for(String nome : nomes) {
            System.out.println(nome);
        }

    }
}
