package WDH;

/**
 * @Autor Luca Sautter
 * Parent Klasse für alle Componenten
 */
public abstract class Component {
    /**
     * Alle Kabel vor dem Komponenet (da wo die getOut methode aufgerufen wird)
     */
    Kabel [] vorInput;
    /**
     * Array aus booleans welche für die inputs stehen
     */
    boolean [] input;
    /**
     * Array aus booleans welche für die outputs stehen
     */
    boolean [] output;

    public Component(int inputCount, int outputCount, int vorInputCount) {
        input = new boolean[inputCount];
        output = new boolean[outputCount];
        vorInput = new Kabel[vorInputCount];
    }

    /**
     * getTakt methode wird in einer schleife von Takt ausgeführt und fürt auf allen inputs die get Out methode aus
     */
    public void gTakt(){
        for (int i = 0; i < input.length; i++) {
            input[i] = vorInput[i].getOut(i);
        }
    }

    /**
     * liefert den State das Out interfaces mit dem richtigen index zurück
     * @param outIndex
     * @return
     */
    public abstract boolean getOut(int outIndex);

    /**
     * Methode welche den State berechnet
     * wird von Takt in einer schleife durch alle komponenten aufgerufen
     */
    public abstract void calc();

    /**
     * Setzt das InKabel wo dann die getOut methode aufgerufen wird
     * @param kabel
     * @param index
     */
    public abstract void setKabel(Kabel kabel, int index);

}
