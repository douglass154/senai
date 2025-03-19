package exercicios.ex01;

public class Array {
    public static void main(String[] args) {
        int[] Array = {10, 20, 30, 40};
        int indice = 2;

        try {
            System.out.println("Elemento do índice "+ indice +": "+ Array[indice]);
        } catch (ArrayIndexOutOfBoundsException err) {
            System.out.println("Elemento não existe no índice selecionado!");
        } finally {
            System.out.println("Finalizando...");
        }
    }
}
