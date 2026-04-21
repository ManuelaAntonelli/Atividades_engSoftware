public class Receiver implements ConcreteCommand {
    
    @Override
    public void turnOn(){
        System.out.println("Lâmpada esta ligada");
    }

    @Override
    public void turnOff(){
        System.out.println("Lâmpada esta desligada");
    }
}
