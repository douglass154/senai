package ex02;

import java.util.ArrayList;
import java.util.Scanner;

public class App {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        ArrayList<ArCondicionado> arCondicionados = new ArrayList<>();

        while (true) {
            menu();
            System.out.print("Qual das opções você deseja?(1-3): ");
            int option = sc.nextInt();

            switch (option) {
                case 1:
                    cadastrarArCondicionado(arCondicionados);
                    break;
            
                default:
                    break;
            }
        }
    }

    public static void menu() {
        System.out.println("");
        System.out.println("=== Cadastro de Ar Condicionados ===");
        System.out.println("");
        System.out.println("1. Cadastrar novo Ar Condicionado");
        System.out.println("2. Listar todos os Ar Condicionados");
        System.out.println("3. Encerrar programa");
        System.out.println("");
    }

    public static void cadastrarArCondicionado(ArrayList<ArCondicionado> arCondicionados) {
        int codigo;
        String marca;
        String btu;
        boolean isBreak = false;
        String tipoDoDefeito = "";

        sc.nextLine();
        System.out.print("Digite qual é o modelo do Ar condicionado: ");
        String modelo = sc.nextLine();

        // if(!modelo.contains("splinter") || !modelo.contains("portatil")) {
        //     System.out.println("Modelo inválido!");
        //     return;
        // }

        System.out.print("Código do Ar Condicionado: ");
        codigo = sc.nextInt();

        sc.nextLine();
        System.out.print("Marca: ");
        marca = sc.nextLine();

        System.out.print("BTU: ");
        btu = sc.nextLine();

        System.out.print("Possui algum defeito?(sim/não): ");
        String defeito = sc.nextLine();

        if(defeito.toLowerCase().contains("sim")) {
            isBreak = true;
            System.out.print("Tipo do defeito: ");
            tipoDoDefeito = sc.nextLine();
        }

        if(modelo.toLowerCase().contains("splinter")) {
            String tipo;
            int tamanho;

            System.out.print("Tipo do Ar condicionado: ");
            tipo = sc.nextLine();

            System.out.print("Tamanho (cm): ");
            tamanho = sc.nextInt();

            Splinter splinter = new Splinter(codigo, marca, btu, isBreak, tipoDoDefeito, tipo, tamanho);
            arCondicionados.add(splinter);
        
        } else if(modelo.toLowerCase().contains("portatil")) {
            int voltagem;
            String cor;

            System.out.print("Voltagem: ");
            voltagem = sc.nextInt();

            System.out.print("Cor: ");
            cor = sc.next();
            
            Portatil portatil = new Portatil(codigo, marca, btu, isBreak, tipoDoDefeito, voltagem, cor);
        }

        System.out.println("Ar condicionado cadastrado com sucesso!");
    }
}
