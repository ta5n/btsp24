public class Calisan {
    private long sicilNo; /* sicil no */
    private String adSoyad; /* ad soyad */
    private double satisTutari; /* satış tutarı */
    private double prim; /* prim */

    public Calisan(long sicilNo, String adSoyad, double satisTutari) {
        this.sicilNo = sicilNo;
        this.adSoyad = adSoyad;
        this.satisTutari = satisTutari;
    }

    public Calisan(Calisan clsn) {
        this.sicilNo = clsn.sicilNo;
        this.adSoyad = clsn.adSoyad;
        this.satisTutari = clsn.satisTutari;
    }

    public long getSicilNo() {
        return this.sicilNo;
    }

    public String getAdSoyad() {
        return this.adSoyad;
    }

    public double getSatisTutari() {
        return this.satisTutari;
    }

    public void setSatisTutari(double satisTutari) {
        this.satisTutari = satisTutari;
    }

    public double getPrim() {
        return this.prim;
    }

    public void setPrim(double prim) {
        this.prim = prim;
    }

    public static void guncelle(Calisan[] calisanlar, Calisan[] liste) {
        int cInd = 0;
        for (int i = 0; i < liste.length - 1; i++) {
            if (liste[i] == null)
                continue;
            Calisan temp = new Calisan(liste[i]);
            for (int j = i + 1; j < liste.length; j++) {
                if (liste[j] != null && temp.getSicilNo() == liste[j].getSicilNo()) {
                    temp.setSatisTutari(temp.getSatisTutari() + liste[j].getSatisTutari());
                    liste[j] = null;
                }
            }
            calisanlar[cInd] = new Calisan(temp);
            cInd++;
        }
        if (liste[liste.length - 1] != null) {
            calisanlar[cInd] = new Calisan(liste[liste.length - 1]);
        }
    }

    public static void primHesapla(Calisan[] calisanlar, double primOrani) {
        // TODO: Her bir çalışan için verilen prim oranına göre alacağı primi hesaplayacak

        for (int i = 0; i < calisanlar.length; i++) {
            if (calisanlar[i] == null)
                continue;
            calisanlar[i].setPrim(calisanlar[i].getSatisTutari() * primOrani);
        }
    }

    public static void listele(Calisan[] calisanlar) {
        for (Calisan c : calisanlar) {
            if (c == null)
                continue;
            System.out.println("Sicil No: " + c.getSicilNo() + ", Ad-Soyad: " + c.getAdSoyad() + ", Satis Tutari: "
                    + c.getSatisTutari() + ", Prim: " + c.getPrim());
        }
    }

    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        Calisan[] liste = { new Calisan(1111111111l, "Ali Deniz", 23455.0),
                new Calisan(2222222222l, "Derya Gunes", 5696.70), new Calisan(3333333333l, "Mehmet Mavi", 2750.0),
                new Calisan(4444444444l, "Ada Yesil", 7255), new Calisan(5555555555l, "Yagmur Kirmizi", 2753),
                new Calisan(4444444444l, "Ada Yesil", 2750.0), new Calisan(2222222222l, "Derya Gunes", 10000),
                new Calisan(2222222222l, "Derya Gunes", 100), new Calisan(3333333333l, "Mehmet Mavi", 50.0) };
        Calisan[] calisanlar = new Calisan[30];
        guncelle(calisanlar, liste);
        primHesapla(calisanlar, 0.1);
        listele(calisanlar);
    }
}
