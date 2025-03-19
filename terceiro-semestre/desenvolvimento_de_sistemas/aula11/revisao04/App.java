public class App {
    public static void main(String[] args) {
        Geladeira geladeira = new Geladeira("Eletrolux", 15000, 15);
        Microondas microondas = new Microondas("Max", 8000, 20);

        geladeira.ligar();
        microondas.ligar();
    }
}
