public class Pessoa {
    private String nome;
    private String telefone;

    // Construct
    public Pessoa(String nome, String telefone) {
        this.nome = nome;
        this.telefone = telefone;
    }

    public String getNome() {
        return this.nome;
    }

    public String getPhone() {
        return this.telefone;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setPhone(String telefone) {
        this.telefone = telefone;
    }
}