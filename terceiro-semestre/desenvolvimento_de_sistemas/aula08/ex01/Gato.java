package ex01;

public class Gato extends Animal {
    private String cor;

    public Gato(String nome, String cor, int patas) {
        super(nome, patas);
        this.cor = cor;
    }

    @Override
    public void exibirSom() {
        System.out.println("Miau");
    }
}
