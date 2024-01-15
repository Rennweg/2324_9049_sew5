package WDH;

/**
 * @Autor Luca Sautter
 */
public class Kabel extends Component {
    boolean state = false;
    int inputIndex;
    Component inputComponent;

    /**
     * holt sich den input
     */
    @Override
    public void gTakt(){
        state = inputComponent.getOut(inputIndex);
    }

    /**
     * leifert den output
     * @param outIndex
     * @return
     */
    @Override
    public boolean getOut(int outIndex){
        return state;
    }

    /**
     * kann leer gelassen werden nachdem ein kabel keine logik hat
     */
    @Override
    public void calc() {

    }

    /**
     * kann leer gelassen werden weil man keine 2 kabel verketten kann
     * @param kabel
     * @param index
     */

    @Override
    public void setKabel(Kabel kabel, int index) {

    }

    /**
     * Konstruktor
     * @param inputComponent
     * @param inputIndex
     * @param outputComponent
     * @param outputIndex
     */

    public Kabel(Component inputComponent, int inputIndex, Component outputComponent, int outputIndex) {
        super(0,0,0);
        this.inputIndex = inputIndex;
        this.inputComponent = inputComponent;
        outputComponent.setKabel(this, outputIndex);
    }
}
