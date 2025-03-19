package exemplo2;

public class Veiculo {
    private String marca;
    private String modelo;
    private int ano;

    public Veiculo(String marca, String modelo, int ano) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
    }

    public String getBrand() {
        return this.marca;
    }

    public String getModel() {
        return this.modelo;
    }

    public int getYear() {
        return this.ano;
    }

    public void setBrand(String marca) {
        this.marca = marca;
    }

    public void setModel(String modelo) {
        this.modelo = modelo;
    }

    public void setYear(int ano) {
        this.ano = ano;
    }

    public void exibirInfo() {
        System.out.println("Marca: "+ getBrand());
        System.out.println("Modelo: "+ getModel());
        System.out.println("Ano: "+ getYear());
    }
}
