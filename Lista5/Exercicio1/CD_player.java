public class CD_player implements Device_Interface {
    
    @Override
    public void turnOn(){

        System.out.println("CD esta ligado");
    }

    @Override
    public void turnOff(){

        System.out.println("CD esta desligado");
    }

    @Override
    public void start(){

        System.out.println("CD esta iniciando");
    }

     @Override
    public void pause(){

        System.out.println("CD esta pausado");
    }

     @Override
    public void stop(){

        System.out.println("CD foi encerrado");
    }

     @Override
    public void reset(){

        System.out.println("CD esta iniciando novamente");
    }

}
