import java.util.Scanner;

public class Soru1ve2 {

    /*
    Soru 1:
    Aşağıdaki hesapla işlevinin hesaplama karmaşıklığını
    O gösterimi ile ifade ediniz:
    */
    /*
    static void ciz(int m) {
        for (int i = 1; i <= m; i++) {
            // birinci dongu m defa tekrar ediyor
            for (int j = i; j >= 1; j--)
                // ikinci dongu her i değeri için i den 1 e kadar i kadar tekrar ediyor
                System.out.print("*");
            System.out.println();
        }
        // ciz metodu m sayisina bagli olarak
        // m * (m+1) /2 defa tekrar ediyor
        // basitlestirilmiş O(n) gosterimine gore 
        // hesaplama karmasikliği m^2 (m kare) dir.
    }
    */

    /*
    Soru 2:
    Birinci soruya verdiğiniz yanıtı kullanarak, aşağıdaki main
    işlevinin hesaplama karmaşıklığını O gösterimi ile
    ifade ediniz:
    */
    /*
    public static void main(String[] args) {
        int n = 10; // O(1)
        Scanner oku = new Scanner(System.in); // O(1)
        System.out.print("N="); // O(1)
        n = oku.nextInt(); // O(1)
        for (int j = n; j >= 1; j--) {
            ciz(j); // O(j^2)
            j--;
            // for dongusu sayacina dongu icerisinde mudahale edilerek iterasyon yari yariya azaltiliyor
            // bu durumda hesaplama karmasikligi (n * (n+1)/2)/2 haline geliyor.
            // yani (n * n+1) / 4 olarak ortaya cikmaktadır.
            System.out.println(); // O(1)
        }
        // O() gosteriminde n sayisina bagli olarak n^2/4, (n kare) / 4 karmasikligi elde ediyoruz.
        // bu ise n^2 n kare ye bagli bir deger oldugundan hesaplama karmasikligi
        // O(n^2) n kare olarak hesaplanmistir.
    }
    */
}
