import java.util.ArrayList;
import java.util.Scanner;

public class TesteArrayNumero {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> numeros = new ArrayList<>();
        
        for(int i = 1; i <= 10; i++) {
            System.out.print("Digite o " + i +"º número: ");
            int num = sc.nextInt();
            
            numeros.add(num);
        }

        for(int numero : numeros) {
            
        }
    }
}