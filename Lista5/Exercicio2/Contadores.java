public class Contadores {
    public static void main(String[] args) {
        
        int valor = 6;
        int valor2 = 6;
        int valor3 = 8;

        Incremental incremental1 = Incremental.getInstance();
        Incremental incremental2 = Incremental.getInstance();
        Incremental incremental3 = Incremental.getInstance();

        incremental1.adicionarNumero(valor);
        System.out.println(incremental1.toString()); 

        incremental2.adicionarNumero(valor2);
        System.out.println(incremental1.toString()); 

        incremental3.adicionarNumero(valor3);
        System.out.println(incremental3.toString());
    }
}