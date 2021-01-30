import java.lang.Math;
import java.util.Random;

public class Fonks {

	public static void main(String args[]) {
	
		int min = 1, max = 7;
		double mr = Math.random() * (max - min + 1) + min;
		int mri = (int) mr;
		System.out.println(mr + " " + mri);
		
		Random rnd = new Random();
		double ur = rnd.nextDouble();
		int uri = rnd.nextInt(6) + 1;
		
		System.out.println(ur + " " + uri);
		int[] zz = zarAt(2);
		System.out.println(zz);
	}
	
	public static int zarAt() {
		return (int) Math.random() * 6 + 1;
	}
	
	public static int[] zarAt(int zarAdedi) {
		int[] sonuc = new int[zarAdedi];
		for (int i = 0; i < zarAdedi, i++) {
			sonuc[i] = zarAt();
		return sonuc;
	}
