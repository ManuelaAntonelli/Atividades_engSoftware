class Incremental 
{
    private Incremental(){}

    private static Incremental instance;

    public static Incremental getInstance(){
        if(instance == null) // primeira vez que se chama getInstance
            instance = new Incremental();
        return instance;
    }
    private int numero;

    public void adicionarNumero(int valor){
        numero += valor;  
    }

    public String toString() 
    {
    return "Incremental " + numero;
    } 
}