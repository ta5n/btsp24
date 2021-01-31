import java.util.Scanner;

// Tamsayı elemanlarını tutan yığıt sınıfı. 
class Stack {
	// Yığıtın alabileceği eleman sayısının üst sınırı. 
	public final int MAX_SIZE = 100;
	private int top;
	private int[] elements;

	// Yığıt yaratıcı işlev.
	public Stack() {
		top = -1;
		elements = new int[MAX_SIZE]; // diziyi yarat
	}

	// full() işlevi, yığıt dolu ise true, değilse false döner. 
	public boolean full() {
		return (top == MAX_SIZE - 1);
	}

	// empty() işlevi, yığıt boş ise true, değilse false döner. 
	public boolean empty() {
		return (top == -1);
	}

	// push(x) işlevi, yığıt dolu ise hata verir, değilse verilen x değerini yığıta ekler. 
	public void push(int x) {
		if (full())
			throw new RuntimeException("Hata: Yigit dolu"); // yığıt doluysa hata ver
		++top; // eleman sayısını artır
		elements[top] = x; // yığıtın üzerine x'i ekle
	}

	// pop() işlevi, yığıt boş ise hata verir, değilse yığıtın en üst elemanını alıp döndürür. 
	public int pop() {
		if (empty())
			throw new RuntimeException("Hata: Yigit bos"); // yığıt boşsa hata ver
		int temp = elements[top]; // üstteki elemanı al
		top--; // eleman sayısını azalt
		return temp; // daha önce üstte olan elemanı döndür
	}

	static void hesapla() {
		// Kodlarinizi bu islevin icine yaziniz
		Scanner scan = new Scanner(System.in);
		final int MAXNUM = 100;
		int count = 0;
		Stack prime = new Stack();
		Stack nonPrime = new Stack();
		int input = 0;
		while (count < MAXNUM) {
			count++;
			input = scan.nextInt();
			if (input < 1) {
				break;
			}
			if (isPrime(input)) {
				prime.push(input);
			} else {
				nonPrime.push(input);
			}
		}
		Stack temp = new Stack();
		while (!prime.empty()) {
			temp.push(prime.pop());
		}
		System.out.println("\nAsal Sayilar:");
		while (!temp.empty()) {
			System.out.println(temp.pop());
		}
		System.out.println("\nAsal olmayan Sayilar:");
		while (!nonPrime.empty()) {
			System.out.println(nonPrime.pop());
		}

	}

	static boolean isPrime(int number) {
		if (number < 2) {
			return false;
		}
		for (int i = 2; i <= Math.sqrt(number); i++) {
			if (number % i == 0)
				return false;
		}
		return true;
	}

	public static void main(String[] args) {

		//Ornek sayi listesi : 3, 7, 12, 23, 37, 44, 43, 75, 2, 97, 113
		hesapla();

	}
}

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
