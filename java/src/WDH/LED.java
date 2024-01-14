package WDH;

/**
 * @Autor Luca Sautter
 */
public class LED extends Component{
    /**
     * Konstruktor
     */
    public LED() {
        super(1,0,1);
    }


    /**
     * lifert den Output zurück
     * @param outIndex
     * @return
     */
    @Override
    public boolean getOut(int outIndex) {
        return input[0];
    }

    /**
     * kann leer gelassen werden nachdem eine LED keine logik hat
     */
    @Override
    public void calc() {
    }

    /**
     * setzt ein kabel davor, von welchen der input geholt wird
     * @param kabel
     * @param index
     */
    @Override
    public void setKabel(Kabel kabel, int index) {
        vorInput[0] = kabel;
    }

    /**
     * liefert einen string zurück der sagt ob die LED leutet oder nicht (eigentlich unnötig aber mir war langweilig)
     * @return
     */
    public String istAnOderAus(){
        if(input[0]){
            return "LED Leuchtet";
        }
        else{
            return "LED Leuchtet nicht";
        }
    }
}
