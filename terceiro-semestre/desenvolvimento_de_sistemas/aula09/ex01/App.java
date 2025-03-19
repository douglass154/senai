package ex01;

public class App {
    public static void main(String[] args) {
        Retangulo retangulo = new Retangulo(12, 25);
        Circulo circulo = new Circulo(12.5);

        double areaRetangulo = retangulo.calcularArea();
        double areaCirculo = circulo.calcularArea();

        System.out.println("Área do retângulo: "+ areaRetangulo);
        System.out.println("Área do círculo: "+ areaCirculo);
    }
}
