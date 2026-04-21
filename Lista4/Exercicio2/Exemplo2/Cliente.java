public class Cliente {
    
    public static void main(String args[]){
        USB_C usb_C = new USB_C();
        Adapter_USB adapter = new Adapter_USB(usb_C);
        adapter.saidaUSB_Femea();
    }
}
