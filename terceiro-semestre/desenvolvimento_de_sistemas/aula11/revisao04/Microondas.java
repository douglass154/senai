public class Microondas extends Eletrodomestico {
    private int tempoMaximo;
    private boolean ligado;

    public Microondas(String marca, double potencia, int tempoMaximo) {
        super(marca, potencia);
        this.tempoMaximo = tempoMaximo;
        this.ligado = false;
    }

    public void ligar() {
        if(!ligado) {
            this.ligado = true;
            System.out.println("O microondas está ligado");
        } else {
            this.ligado = false;
            System.out.println("Agora o microondas está desligado");
        }
    }
}
