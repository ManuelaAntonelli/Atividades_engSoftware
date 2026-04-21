public class DeviceFactory {
   public Device_Interface createDispositivo(String dispositivo){

      if (dispositivo == null || dispositivo.isEmpty())
         return null;

   switch (dispositivo) {
    case "CD":
    return new CD_player();
    case "DVD":
    return new DVD_player();
    case "Voice Recorver":
    return new Voice_Recorver();
    default:
    throw new IllegalArgumentException("Não encontrado nenhum dispositivo " + dispositivo);
   }
}
}
