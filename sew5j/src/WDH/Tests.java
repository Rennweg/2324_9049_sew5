package WDH;
import org.junit.Assert;
import org.junit.jupiter.api.Test;
public class Tests {
    @Test
    public void TestFFRS(){
        Taster taster1 = new Taster();
        Taster taster2 = new Taster();
        FlipFlop ffrs = new FlipFlop();
        LED led = new LED();
        Kabel kabel1 = new Kabel(taster1, 0, ffrs,0);
        Kabel kabel2 = new Kabel(taster2, 0, ffrs,1);
        Kabel kabel3 = new Kabel(ffrs, 0, led,0);
        Takt takt = new Takt(taster1, taster2, ffrs, led, kabel1, kabel2, kabel3);
        Assert.assertEquals("LED Leuchtet nicht", led.istAnOderAus());
        takt.getTakt();
        takt.calcTakt();
        Assert.assertEquals("LED Leuchtet nicht", led.istAnOderAus());
        taster1.click();
        takt.getTakt();
        takt.calcTakt();
        Assert.assertEquals("LED Leuchtet nicht", led.istAnOderAus());
        takt.getTakt();
        takt.calcTakt();
        Assert.assertEquals("LED Leuchtet nicht", led.istAnOderAus());
        takt.getTakt();
        takt.calcTakt();
        Assert.assertEquals("LED Leuchtet nicht", led.istAnOderAus());
        takt.getTakt();
        takt.calcTakt();
        Assert.assertEquals("LED Leuchtet", led.istAnOderAus());
        taster1.click();
        takt.getTakt();
        takt.calcTakt();
        takt.getTakt();
        takt.calcTakt();
        takt.getTakt();
        takt.calcTakt();
        takt.getTakt();
        takt.calcTakt();
        takt.getTakt();
        takt.calcTakt();
        takt.getTakt();
        takt.calcTakt();
        takt.getTakt();
        takt.calcTakt();
        Assert.assertEquals("LED Leuchtet", led.istAnOderAus());
        taster2.click();
        takt.getTakt();
        takt.calcTakt();
        takt.getTakt();
        takt.calcTakt();
        takt.getTakt();
        takt.calcTakt();
        takt.getTakt();
        takt.calcTakt();
        Assert.assertEquals("LED Leuchtet nicht", led.istAnOderAus());
    }
}
