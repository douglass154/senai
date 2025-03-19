public class Geladeira extends Eletrodomestico {
    private double capacidade;
    private boolean ligado;

    public Geladeira(String marca, double potencia, double capacidade) {
        super(marca, potencia);
        this.capacidade = capacidade;
        this.ligado = false;
    }

    public void ligar() {
        if(!ligado) {
            this.ligado = true;
            System.out.println("A geladeira está ligada");
        } else {
            this.ligado = false;
            System.out.println("Agora a geladeira está desligada");
        }
    }

}
