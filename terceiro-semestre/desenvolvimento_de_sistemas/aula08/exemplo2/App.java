package exemplo2;

public class App {
    public static void main(String[] args) {
        Carro carro = new Carro("Lamborghini","Huracan", 2022, 2);
        Moto moto = new Moto("Honda", "150", 2022, 600);
        Aviao aviao = new Aviao("Boing", "Boing 4078", 2023);
        Veiculo veiculo = new Veiculo("Carrao", "Carrao brabo", 2077);

        veiculo.exibirInfo();
        System.out.println();

        aviao.exibirInfo();

        System.out.println();
        carro.exibirInfo();

        System.out.println();
        moto.exibirInfo();
    }
}
