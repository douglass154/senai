import java.util.ArrayList;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> numeros = new ArrayList<>();

        int contador = 1;
        boolean pair = false;

        while(true) {
            if(contador == 1) {
                System.out.println("Digite 0 para parar o programa.");
            };

            System.out.print("Digite o "+ contador +"º número: ");
            int userNumber = sc.nextInt();

            if(userNumber == 0) {
                System.out.println("");
                System.out.println("Saindo do programa...");
                sc.close();
                break;
            }

            numeros.add(userNumber);
            contador++;
        }

        for(int numero : numeros) {
            if(numero % 2 != 0) {
                System.out.println("Nem todos os números na lista são pares.");
                pair = false;
                break;
            }
            pair = true;
        }
        
        if(pair) {
            System.out.println("Todos os números na lista são pares.");
        }
    }
}