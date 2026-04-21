public class Adapter_USB extends USB_Femea {
    
    private USB_C usb_C;

    public Adapter_USB (USB_C usb_C){
        this.usb_C = usb_C;
    }

    public void saidaUSB_Femea(){
        usb_C.saidaUSBC();
    }
}
