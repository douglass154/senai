package aula06.ex004;

public class Cadastro {
    private String nome;
    private String telefone;

    public Cadastro(String nome, String telefone) {
        this.nome = nome;
        this.telefone = telefone;
    }

    public String getName() {
        return this.nome;
    }

    public String getPhone() {
        return this.telefone;
    }

}
