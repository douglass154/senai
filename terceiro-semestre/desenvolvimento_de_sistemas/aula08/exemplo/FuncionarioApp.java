package exemplo;

public class FuncionarioApp {
    public static void main(String[] args) {
        Funcionario funcionario = new Funcionario("Leo", 2400, 18);
        Gerente gerente = new Gerente("Douglas", 12600, 20, 400);

        System.out.println("Funcionário: " + funcionario.getName());
        System.out.println("Idade: " + funcionario.getAge());
        System.out.println("Salário: " + funcionario.getSalary());
        System.out.println("");

        System.out.println("Gerente: "+ gerente.getName());
        System.out.println("Idade: "+ gerente.getAge());
        System.out.println("Salário: "+ gerente.getSalary());
        System.out.println("Bonus: "+ gerente.getBonus());
    }
}
