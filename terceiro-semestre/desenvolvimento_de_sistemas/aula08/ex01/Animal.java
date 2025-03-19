package ex01;

public class Animal {
    private String nome;
    private int patas;

    public Animal(String nome, int patas) {
        this.nome = nome;
        this.patas = patas;
    }

    public void exibirSom() {
        System.out.println("Eu sou um animal.");
    }
}
