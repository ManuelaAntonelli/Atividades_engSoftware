public class Client {
    
    public static void main(String arg[]){
        HDMI hdmi = new HDMI();
        AdapterVideo adapter = new AdapterVideo(hdmi);
        adapter.ligarNoVGA();
    }
}
