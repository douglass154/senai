package exemplo2;

public class Carro extends Veiculo {
    private int qtdPortas;

    public Carro(String marca, String modelo, int ano, int qtdPortas) {
        super(marca, modelo, ano);
        this.qtdPortas = qtdPortas;
    }

    public int getQtdPortas() {
        return this.qtdPortas;
    }

    public void setQtdPortas(int qtdPortas) {
        this.qtdPortas = qtdPortas;
    }

    @Override
    public void exibirInfo() {
        System.out.println("Marca: "+ getBrand());
        System.out.println("Modelo: "+ getModel());
        System.out.println("Ano: "+ getYear());
        System.out.println("Quantidade de Portas: "+ getQtdPortas());
    }
}
