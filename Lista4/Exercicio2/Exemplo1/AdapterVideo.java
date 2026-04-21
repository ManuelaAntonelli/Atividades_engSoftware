public class AdapterVideo extends VGA {

    private HDMI hdmi;

    public AdapterVideo(HDMI hdmi) {
        this.hdmi = hdmi;
    }

    public void ligarNoVGA() {
        hdmi.ligarNoHDMI();
    }
}
