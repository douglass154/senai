public class App {
    public static void main(String[] args) {
        Produto produto = new Produto("Ventilador", 67.90, 150);
        produto.setNome("Geladeira");
        produto.setPreco(2373.90);
        produto.setQuantidade(120);

        double valorTotal = produto.calcularValorTotal();
        System.out.println("O valor total do produto "+ produto.getNome() +" é R$"+ valorTotal);
    }
}