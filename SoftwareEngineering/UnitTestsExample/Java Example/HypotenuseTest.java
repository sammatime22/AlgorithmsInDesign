import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;

public class HypotenuseTest extends Hypotenuse {

	@Test
	public void testCalculateHypotenuse(){
		// 3^2 + 4^2 = 5^2
		assertEquals(5.0, Hypotenuse.calculateHypotenuse(3, 4), 0.01);
	}

	@Test
    public void testAnotherCorrectCase(){
        // 6^2 + 8^2 = 10^2
        assertEquals(10.0, Hypotenuse.calculateHypotenuse(6, 8), 0.01);
    }

    @Test
    public void testAnIncorrectCase(){
        // 9^2 + 16^2 != 30, rather something like 18.357-ish
        assertNotEquals(30.0, Hypotenuse.calculateHypotenuse(9, 16), 0.01);
    }
}