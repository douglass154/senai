package exemplo;

public class Funcionario {
    private String nome;
    private double salario;
    private int idade;

    public Funcionario(String nome, double salario, int idade) {
        this.nome = nome;
        this.salario = salario;
        this.idade = idade;
    }

    public String getName() {
        return this.nome;
    }

    public double getSalary() {
        return this.salario;
    }

    public int getAge() {
        return this.idade;
    }

    public void setName(String nome) {
        this.nome = nome;
    }

    public void setSalary(double salario) {
        this.salario = salario;
    }

    public void setAge(int idade) {
        this.idade = idade;
    }
}