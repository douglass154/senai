package aula04.exercicios.ex001;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite quantos números deseja inserir: ");
        int tamanho = sc.nextInt();

        double[] numeros = new double[tamanho];

        sc.close();
    }
}
