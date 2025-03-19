public class Numero {
    public static void main(String[] args) {
        try {
            int numero = 10 / 0;
        } catch(ArithmeticException err) {
            System.out.println("Erro: impossível dividir um número por zero");
        } finally {
            System.out.println("Finalizando...");
        }
    }
}