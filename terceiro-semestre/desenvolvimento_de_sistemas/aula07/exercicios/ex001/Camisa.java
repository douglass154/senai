package exercicios.ex001;

public class Camisa {
    private String cor;
    private int tamanho;
    private String tipo;

    public Camisa(String cor, int tamanho, String tipo) {
        this.cor = cor;
        this.tamanho = tamanho;
        this.tipo = tipo;
    }

    public String getColor() {
        return this.cor;
    }

    public int getSize() {
        return this.tamanho;
    }

    public String getType() {
        return this.tipo;
    }

    public void setColor(String cor) {
        this.cor = cor;
    }

    public void setSize(int tamanho) {
        this.tamanho = tamanho;
    }

    public void setType(String tipo) {
        this.tipo = tipo;
    }

}
