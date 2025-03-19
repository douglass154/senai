import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o valor do seu salário: ");
        double salario = sc.nextDouble();

        if(salario >= 3000) {
            System.out.println("Você é rico!");
        } else {
            System.out.println("Você é pobre!");
        }

        sc.close();
    }
}