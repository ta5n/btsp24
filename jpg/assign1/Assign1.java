
import javax.swing.JOptionPane;

/**
 *
 * @author Osman Tas <me@tasosman.com> s24161
 */
public class Assign1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int odev1Not, odev2Not, vizeNot, finalNot;
        odev1Not = Integer.parseInt(JOptionPane.showInputDialog(null, "Birinci odev notunu giriniz ", "Not Girisi", 0));
        odev2Not = Integer.parseInt(JOptionPane.showInputDialog(null, "Ikinci odev notunu giriniz ", "Not Girisi", 0));
        vizeNot = Integer.parseInt(JOptionPane.showInputDialog(null, "Vize notunu giriniz ", "Not Girisi", 0));
        finalNot = Integer.parseInt(JOptionPane.showInputDialog(null, "Final notunu giriniz ", "Not Girisi", 0));
        // ödev not ortalaması alındığı için ikiye bölüyoruz
        double ortalama = (odev1Not + odev2Not) * 0.1 + vizeNot * 0.3 + finalNot * 0.5;
        JOptionPane.showMessageDialog(null, "Not ortalamasi: " + ortalama, "Not Ortalamaniz",
                JOptionPane.INFORMATION_MESSAGE);
    }
}
