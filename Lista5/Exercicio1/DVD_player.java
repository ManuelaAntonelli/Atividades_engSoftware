public class DVD_player implements Device_Interface {
    
    @Override
    public void turnOn(){

        System.out.println("DVD esta ligado");
    }

    @Override
    public void turnOff(){

        System.out.println("DVD esta desligado");
    }

    @Override
    public void start(){

        System.out.println("DVD esta iniciando");
    }

     @Override
    public void pause(){

        System.out.println("DVD esta pausado");
    }

     @Override
    public void stop(){

        System.out.println("DVD foi encerrado");
    }

     @Override
    public void reset(){

        System.out.println("DVD esta iniciando novamente");
    }
}
