import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = 0;
        
        System.out.print("Quantos números deseja adicionar: ");
        int tam = sc.nextInt();

        int[] numeros = new int[tam];

        for(int i = 0; i < numeros.length; i++) {
            System.out.print("Digite o "+ (i + 1) +"º número: ");
            numeros[i] = sc.nextInt();
        }
        System.out.println("");
        System.out.print("Qual número deseja procurar: ");
        int searchedNumber = sc.nextInt();

        for(int numero : numeros) {
            if(numero == searchedNumber) {
                count++;
            }
        }

        System.out.println("O número "+ searchedNumber +" apareceu "+ count +" vezes na lista.");

        sc.close();

    }   
}
