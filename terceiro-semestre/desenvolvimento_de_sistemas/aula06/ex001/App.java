package aula06.ex001;

import java.util.ArrayList;

public class App {
    public static void main(String[] args) {
        // Criando um ArrayList
        ArrayList<Integer> numeros = new ArrayList<>();

        // Adicionando elementos ao ArrayList
        numeros.add(10);
        numeros.add(20);
        numeros.add(30);

        // Exibindo os elementos do ArrayList
        System.out.println("Elementos do ArrayList de Inteiros:");
        for(Integer numero : numeros) {
            System.out.println(numero);
        }

        // Exibindo os elementos do ArrayList
        System.out.println("Elementos do ArrayList de inteiros: " + numeros);
        
        // Verificando o tamanho do ArrayList
        int tamanho = numeros.size();
        System.out.println("Tamanho do ArrayList: " + tamanho);

        // Verificando a existência de um elemento
        boolean existeElemento30 = numeros.contains(30);
        System.out.println("Existe o elemento 30? " + existeElemento30);

        // Removendo um elemento
        numeros.remove(Integer.valueOf(30)); // Removendo o valor 30
        System.out.println("Após a remoção do elemento 30:");
        for(Integer numero : numeros) {
            System.out.println(numero);
        }

    }

}
