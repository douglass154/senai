public class App {
    public static void main(String[] args) {
        Assistente assistente = new Assistente("Leonardo", 3200, "Estagiário");
        Gerente gerente = new Gerente("Arthur", 20200, "Gerente");

        System.out.println("Bônus de "+ assistente.getNome() +": "+ assistente.calcularBonus());
        System.out.println("Bônus de "+ gerente.getNome() +": "+ gerente.getBonus());
    }
}
