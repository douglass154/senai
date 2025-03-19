package ex02;

public class Portatil extends ArCondicionado {
    private int voltagem;
    private String cor;

    public Portatil(int codigo, String marca, String btu, boolean isBreak, String tipoDoDefeito, int voltagem, String cor) {
        super(codigo, marca, btu, isBreak, tipoDoDefeito);
        this.voltagem = voltagem;
        this.cor = cor;
    }

    public int getVoltagem() {
        return voltagem;
    }

    public void setVoltagem(int voltagem) {
        this.voltagem = voltagem;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

}
