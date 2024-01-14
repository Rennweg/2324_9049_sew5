package WDH;

import java.util.ArrayList;
import java.util.List;

/**
 * @Autor Luca Sautter
 */
public class Takt {
    List<Component> componentList = new ArrayList<>();

    /**
     * Konstruktor
     * @param components
     */
    public Takt(Component...components) {
        for(Component a: components){
            componentList.add(a);
        }
    }

    /**
     * Methode wellche kompnenten in die liste aufnimmt
     * @param components
     */
    public void addComponent(Component...components){
        for(Component a: components){
            componentList.add(a);
        }
    }

    /**
     * Methode die den Get Takt bei allen Componenten in der Liste ausführt
     */
    public void getTakt(){
        for(Component a: componentList){
            a.gTakt();
        }
    }

    /**
     * Methode die den calc Takt bei allen Componenten in dewr Liste ausführt
     */
    public void calcTakt(){
        for(Component a: componentList){
            a.calc();
        }
    }
}
