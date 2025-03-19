public class Televisao implements Dispositivo {
    private boolean isOn = false;

    public void ligar() {
        this.isOn = true;
    }

    public void desligar() {
        this.isOn = false;
    }
    
    public void estaDesligada() {
        if(isOn) {
            System.out.println("Está ligada");
        } else {
            System.out.println("Está desligada");
        }
    }
}
