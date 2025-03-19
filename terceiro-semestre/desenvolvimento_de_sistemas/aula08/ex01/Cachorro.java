package ex01;

public class Cachorro extends Animal {
    private String cor;

    public Cachorro(String nome, int patas, String cor) {
        super(nome, patas);
        this.cor = cor;
    }

    @Override
    public void exibirSom() {
        System.out.println("Au au");
    }
}
