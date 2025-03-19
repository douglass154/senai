public class PessoaApp {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa("Douglas", "71 98888-1111");

        System.out.println("Nome: "+ p1.getNome() +" - Telefone: "+ p1.getPhone());
    }
}
