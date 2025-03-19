public class Numeros {
    public static void main(String[] args) {
        double a = 3;
        double b = 2;
        
        double soma = a + b;
        double subtracao = a - b;
        double multiplicacao = a * b;
        double divisao = a / b;
        
        System.out.println(soma);
        System.out.println(subtracao);
        System.out.println(multiplicacao);
        System.out.printf("%.2f%n", divisao);
        System.out.printf("%.4f%n", divisao);
    }
}
