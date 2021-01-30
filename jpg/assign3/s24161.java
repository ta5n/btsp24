import java.util.Scanner;
import java.util.Random;

public class s24161 {
    Random rnd = new Random();

    public static void main(String[] args) throws Exception {
        s24161 me = new s24161();
        int c = me.askCount();
        int[] arr = me.randArray(c);
        me.printArray(arr);
        me.printMaxNegNumber(arr);
    }

    public int askCount() {
        Scanner in = new Scanner(System.in);
        System.out.print("n sayisini giriniz: ");
        return in.nextInt();
    }

    public void printArray(int[] array) {
        System.out.print("dizi 1:");
        for (int i = 0; i < array.length; i++) {
            System.out.print(" " + array[i]);
        }
        System.out.println();
    }

    public int[] randArray(int count) {
        int[] result = new int[count];

        for (int i = 0; i < result.length; i++) {
            result[i] = randInt(-25, 25);
        }
        return result;
    }

    // generate a random integer between min and max inclusive
    public int randInt(int min, int max) {
        // rnd attribute is class member
        return min + rnd.nextInt(max - min + 1);
    }

    public void printMaxNegNumber(int[] array) {
        System.out.println("sonuc: " + findMaxNegNumber(array));
    }

    public int findMaxNegNumber(int[] array) {
        int maxNeg = -26;

        for (int i = 0; i < array.length; i++) {
            if (array[i] < 0 && array[i] > maxNeg) {
                maxNeg = array[i];
            }
        }
        if (maxNeg == -26) {
            return 0;
        }
        return maxNeg;
    }
}
