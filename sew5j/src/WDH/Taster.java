package WDH;

/**
 * @Autor Luca Sautter
 */
public class Taster extends Component{
    /**
     * Konstruktor der die länge der vererbten arrays festlegt
     */
    public Taster() {
        super(0,1,0);
        output[0] = false;
    }

    /**
     * kann man leer lassen nachdem der taster kein input hat
     */
    @Override
    public void gTakt(){

    }

    /**
     * liefert den Out des Tasters zurück
     * @param outIndex
     * @return
     */
    @Override
    public boolean getOut(int outIndex) {
        return output[0];
    }

    /**
     * kann man leer lassen nachdem der Taster keine Logik hat
     */
    @Override
    public void calc() {

    }

    /**
     * kann man leer lassen nachdem der Taster kein kabel davor hat nur danach
     * @param kabel
     * @param index
     */
    @Override
    public void setKabel(Kabel kabel, int index) {

    }

    /**
     * Methode welche den state des taster ändert
     */
    public void click(){
        output[0] = !output[0];
    }

}
