public class Main {
    public static void main(String[] args)
    {
        DeviceFactory deviceFactory = new DeviceFactory();
        Device_Interface device = deviceFactory.createDispositivo("CD");
        device.turnOn();
    }
}
