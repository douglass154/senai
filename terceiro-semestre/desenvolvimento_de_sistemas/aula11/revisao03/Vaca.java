public class Vaca extends Animal {
    private String som;

    public Vaca(String som) {
        this.som = som;
    }

    @Override
    public void fazerSom() {
        System.out.println(som);
    }
}
