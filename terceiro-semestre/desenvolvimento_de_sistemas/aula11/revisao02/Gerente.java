public class Gerente extends Funcionario {
    private double bonus;

    public Gerente(String nome, double salario, String cargo) {
        super(nome, salario, cargo);
        this.bonus = salario * 0.10;
    }

    public double getBonus() {
        return bonus;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

}
