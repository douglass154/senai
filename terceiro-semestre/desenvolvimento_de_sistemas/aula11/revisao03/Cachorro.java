public class Cachorro extends Animal {
    private String som;

    public Cachorro(String som) {
        this.som = som;
    }

    @Override
    public void fazerSom() {
        System.out.println(som);
    }
}
