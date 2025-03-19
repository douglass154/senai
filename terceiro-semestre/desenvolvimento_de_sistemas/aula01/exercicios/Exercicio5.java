package exercicios;

import java.util.Scanner;

public class Exercicio5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Calculadora calc = new Calculadora();
    
        System.out.print("Digite a força: ");
        double forca = sc.nextDouble();

        System.out.print("Digite a distancia: ");
        double distancia = sc.nextDouble();

        calc.calcularTrabalho(forca, distancia);

        sc.close();
    } 

}