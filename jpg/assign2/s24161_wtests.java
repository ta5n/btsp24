import java.util.Scanner;

public class s24161 {
    public static void main(String[] args) throws Exception {
        /*
        int p1 = 5;
        int x1 = 20;
        System.out.println(buyuluSayilar(p1, x1));
        
        p1 = 7;
        x1 = 4;
        System.out.println(buyuluSayilar(p1, x1));
        
        p1 = 7;
        x1 = 24;
        System.out.println(buyuluSayilar(p1, x1));
        
        p1 = 3;
        x1 = 40;
        System.out.println(buyuluSayilar(p1, x1));
        
        p1 = 10;
        x1 = 50;
        System.out.println(buyuluSayilar(p1, x1));
        */
        sor();
    }

    public static void sor() {
        Scanner in = new Scanner(System.in);

        System.out.print("p sayisini giriniz: ");
        int p = in.nextInt();
        System.out.print("x sayisini giriniz: ");
        int x = in.nextInt();

        System.out.println(buyuluSayilar(p, x));
    }

    public static String buyuluSayilar(int p, int x) {
        String sonuc = "p-buyulu sayilar: ";
        // p < x değilse veya p > 10 ise veya p < 2 ise boş sonuc donuyor
        if (p >= x || p > 10 || p < 2)
            return sonuc;

        for (int i = p + 1; i <= x; i++) {
            if ((i + 1) % 3 == 0) {
                continue;
            }
            for (int j = 2; j <= p; j++) {
                if ((i % j) == 0) {
                    sonuc += i + " ";
                    break;
                }
            }
        }
        return sonuc;
    }
}
