package ex01;

public class App {
    public static void main(String[] args) {
        Cachorro cachorro = new Cachorro("Brutus", 4, "preto");
        Gato gato = new Gato("Neve", "branco", 4);

        cachorro.exibirSom();
        gato.exibirSom();
    }
}
