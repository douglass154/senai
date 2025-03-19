package aula04;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos nomes deseja inserir? ");
        int tamanho = sc.nextInt();
        sc.nextLine();

        String[] nomes = new String[tamanho];

        for(int i = 0; i < nomes.length; i++) {
            System.out.print("Digite o "+ (i + 1) +"º nome: ");
            nomes[i] = sc.nextLine();
        }

        System.out.println("Nomes digitados:");
        for(int i = 0; i < nomes.length; i++) {
            System.out.println(nomes[i]);
        }

        sc.close();
    }
}
