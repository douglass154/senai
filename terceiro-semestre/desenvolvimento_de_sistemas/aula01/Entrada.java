import java.util.Scanner;

public class Entrada {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o seu nome: ");
        String nome = sc.next();

        System.out.print("Digite a sua idade: ");
        int idade = sc.nextInt();

        System.out.println("Olá " + nome + ", você tem " + idade + " anos");

        sc.close();
    }
}
