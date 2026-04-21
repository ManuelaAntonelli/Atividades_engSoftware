public class Voice_Recorver implements Device_Interface {
     
    @Override
    public void turnOn(){

        System.out.println("Voice Recorver esta ligado");
    }

    @Override
    public void turnOff(){

        System.out.println("Voice Recorver esta desligado");
    }

    @Override
    public void start(){

        System.out.println("Voice Recorver esta iniciando");
    }

     @Override
    public void pause(){

        System.out.println("Voice Recorver esta pausado");
    }

     @Override
    public void stop(){

        System.out.println("Voice Recorver foi encerrado");
    }

     @Override
    public void reset(){

        System.out.println("Voice Recorver esta iniciando novamente");
    }
}
