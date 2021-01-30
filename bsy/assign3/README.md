[![METU CEC](https://sem.metu.edu.tr/img/logo-sem.png)](https://sem.metu.edu.tr/)

# BSY Ödev 3

- ### Ödev Talimatları

  Bu soruda, sizlere tamsayılardan oluşan bir liste verilecektir. 
  Sizlerden çözüm olarak istediğimiz; liste içerisinde bulunan ardışık elemanların arasındaki mesafeyi hesaplayan ve toplam mesafeyi bulan (değer olarak dönen) fonksiyonu tamamlamanız. 

  Çözümünüzü, size verilen tasklak odev2.py dosyasının yapısını değiştirmeden önceden tanımlı rank fonksiyonu içerisine yazınız. 
  rank fonksiyonu parametre olarak değişen uzunlukta bir liste alacak ve hesapladığınız toplam mesafeyi değer olarak döndürecektir. 

  **ÖRNEK 1:**
  rank([21, 4, 13, 5, 8, 17, 22, 6, 23]) şeklinde çağırıldığında aşağıdaki hesaplamaları gerçekleştirmesi beklenmektedir. 

  ''' [21, 4, 13, 5, 8, 17, 22, 6, 23]  '''


  * 21 sayısı 0. indiste ve kendisinden büyük ardışığı olan 22 sayısı ise 6. indistedir. Dolayısıyla aralarındaki mesafe: |0 - 6| = 6.
  * 4 sayısı 1. indiste ve kendisinden büyük ardışığı olan 5 sayısı ise 3. indistedir. Dolayısıyla aralarındaki mesafe: |1 - 3| = 2.
  * 5 sayısı 3. indiste ve kendisinden büyük ardışığı olan 6 sayısı ise 7. indistedir. Dolayısıyla aralarındaki mesafe: |3 - 7| = 4.
  * 22 sayısı 6. indiste ve kendisinden büyük ardışığı olan 23 sayısı ise 8. indistedir. Dolayısıyla aralarındaki mesafe:|6 - 8| = 2.

  Fonksiyonun dönmesi gereken toplam skor değeri 14 olmalıdır. (14 = 6 + 2 + 4 + 2 olduğu için)

  

  **ÖRNEK 2:**
  rank([21, 4, 13, 5, 8, 17, 23, 6, 22]) şeklinde çağırıldığında aşağıdaki hesaplamaları gerçekleştirmesi beklenmektedir. 

  ''' [21, 4, 13, 5, 8, 17, 23, 6, 22]  '''


  * 21 sayısı 0. indiste ve kendisinden büyük ardışığı olan 22 sayısı ise 8. indistedir. Dolayısıyla aralarındaki mesafe: |0 - 8| = 8.
  * 4 sayısı 1. indiste ve kendisinden büyük ardışığı olan 5 sayısı ise 3. indistedir. Dolayısıyla aralarındaki mesafe: |1 - 3| = 2.
  * 5 sayısı 3. indiste ve kendisinden büyük ardışığı olan 6 sayısı ise 7. indistedir. Dolayısıyla aralarındaki mesafe: |3 - 7| = 4.
  * 22 sayısı 8. indiste ve kendisinden büyük ardışığı olan 23 sayısı ise 6. indistedir. Dolayısıyla aralarındaki mesafe:|8 - 6| = 2.


  Fonksiyonun dönmesi gereken toplam skor değeri 16 olmalıdır. (16 = 8 + 2 + 4 + 2 olduğu için)

  *NOT 1: Ardışık sayılar arasındaki mesafe sayıların bulundukları indislerin farklarının mutlak değeri olacaktır.* 
  *NOT 2: Yazdığınız kod ekrana hiçbir bilgi yazdırmayacak olup rank() fonksiyonunuzun sadece istenilen sonucu dönmesi gerekmektedir.* 
  *NOT 3: Listedeki elemanları ele alırken, liste içinde herhangi bir yerde, varsa kendisinden büyük olan ardışık sayı ile birlikte işlem yapmanız gerekmektedir.*

  

- ### Ödevlerin Sisteme Yüklenmesi

  Ödevlerinizi sisteme yüklerken sadece “*.py” uzantılı dosyayı yükleyiniz. Sisteme yüklenecek dosyanın isminin “s24XXX.py” olmasına, 24XXX kısmına öğrenci numaranızın gelmesi gerektiğine dikkat ediniz. Ödevin son teslim tarihi 5 Ocak 2021 Saat 23:50 olacaktır. **Geç teslim kesinlikle kabul edilmeyecektir.** Ödevleriniz kopya kontrolünden geçirilecektir, benzerlik yüzdesi yüksek olan ödevlerin hepsine **SIFIR** verilecektir.

- [Ödev Taslak Dosya](./odev3.py)

- [Ödev Çözümü](./solution.py)


