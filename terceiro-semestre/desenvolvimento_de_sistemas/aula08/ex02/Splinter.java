package ex02;

public class Splinter extends ArCondicionado {
    private String tipos;
    private int tamanho;

    public Splinter(int codigo, String marca, String btu, boolean isBreak, String tipoDoDefeito, String tipos, int tamanho) {
        super(codigo, marca, btu, isBreak, tipoDoDefeito);
        this.tipos = tipos;
        this.tamanho = tamanho;
    }

    public String getTipos() {
        return tipos;
    }

    public void setTipos(String tipos) {
        this.tipos = tipos;
    }

    public int getTamanho() {
        return tamanho;
    }

    public void setTamanho(int tamanho) {
        this.tamanho = tamanho;
    }

}
