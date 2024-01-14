package WDH;

/**
 * @Autor Luca Sautter
 */
public class FlipFlop extends Component{
    State state = State.LOW;

    /**
     * Konstruktor
     */
    public FlipFlop() {
        super(2,2,2);
    }

    /**
     * Statemaschine welche den state ausrechnen kann
     */

    enum State{
        HIGH{
            @Override
            State calcState(boolean S, boolean R) {
                if(!S && R){
                    return State.LOW;
                }else{
                    return State.HIGH;
                }
            }
        },
        LOW{
            @Override
            State calcState(boolean S, boolean R) {
                if(S && !R){
                    return State.HIGH;
                }else{
                    return State.LOW;
                }
            }
        };

        /**
         * berechnet mit zwei varibalen den output
         * @param S
         * @param R
         * @return
         */
        abstract State calcState(boolean S, boolean R);

    }


    /**
     * liefert den output zurück
     * @param outIndex
     * @return
     */

    @Override
    public boolean getOut(int outIndex) {
        return output[outIndex];
    }

    /**
     * ruft die calcState methode auf
     */
    @Override
    public void calc() {
        this.state = state.calcState(input[0], input[1]);
        if (state == State.HIGH){
            output[0] = true;
            output[1] = false;
        }else{
            output[1] = true;
            output[0] = false;
        }
    }

    /**
     * connected ein kabel
     * @param kabel
     * @param index
     */
    @Override
    public void setKabel(Kabel kabel, int index) {
        vorInput[index] = kabel;
    }
}
