package ex02;

public class ArCondicionado {
    private int codigo;
    private String marca;
    private String btu;
    private boolean isBreak = false;
    private String tipoDoDefeito = "";

    public ArCondicionado(int codigo, String marca, String btu, boolean isBreak, String tipoDoDefeito) {
        this.codigo = codigo;
        this.marca = marca;
        this.btu = btu;
        this.isBreak = isBreak;
        this.tipoDoDefeito = tipoDoDefeito;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getBtu() {
        return btu;
    }

    public void setBtu(String btu) {
        this.btu = btu;
    }

    public boolean isBreak() {
        return isBreak;
    }

    public void setBreak(boolean isBreak) {
        this.isBreak = isBreak;
    }

    public String getTipoDoDefeito() {
        return tipoDoDefeito;
    }

    public void setTipoDoDefeito(String tipoDoDefeito) {
        this.tipoDoDefeito = tipoDoDefeito;
    }

}
