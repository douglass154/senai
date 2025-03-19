import java.util.ArrayList;

public class App {
    public static void main(String[] args) {
        ArrayList<Animal> animal = new ArrayList<>();
        Cachorro cachorro = new Cachorro("Au au");

        animal.add(cachorro);
        animal.get(0).fazerSom();

    }
}
