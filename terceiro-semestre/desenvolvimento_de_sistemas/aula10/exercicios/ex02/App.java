import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Digite um número: ");
            String num = sc.nextLine();

            int resultado = Integer.parseInt(num);
            System.out.println("O número que você digitou é: "+ resultado);
        } catch (Exception e) {
            System.out.println("O valor que você digitou é inválido!");
        };
    }
}