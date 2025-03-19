public class Gato extends Animal {
    private String som;

    public Gato(String som) {
        this.som = som;
    }

    @Override
    public void fazerSom() {
        System.out.println(som);
    }

}
