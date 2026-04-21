public class Controlador {
    public static void main(String[] args){

        Receiver lampada = new Receiver();
        Invoker controleRemoto = new Invoker();

        Command turnON = new TurnOnCommand(lampada);
        Command turnOff = new TurnOffCommand(lampada);


        controleRemoto.setCommand(turnON);
        controleRemoto.pressButton();
        controleRemoto.setCommand(turnOff);
        controleRemoto.pressButton();
    }
}
