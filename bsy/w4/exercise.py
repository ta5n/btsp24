# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

''' q1
Girilen bir sayı için

Pozitif ise ekrana "pozitif"
Negatif ise ekrana "negatif"
Bu iki şartı sağlamayan durum için ekrana "notr"
yazdırınız.

'''


def negpos(x):
    if x > 0:
        print("pozitif")
    elif x < 0:
        print("negatif")
    else:
        print("notr")
    pass


''' q2
Sırasıyla alt alta girilen iki karakter dizisi için:

Eğer karakter dizileri "mor" ve "kirmizi" ise ekrana "purpleandred"
Eğer karakter dizileri "siyah" ve "beyaz" ise ekrana "blackandwhite"
Eğer karakter dizileri "gri" ve "sari" ise ekrana "grayandyellow"
Bu şartların dışındaki her durum için ekrana "rainbow"
yazdırınız. 
'''


def rainbow(birinci_renk, ikinci_renk):
    if birinci_renk == "mor" and ikinci_renk == "kirmizi":
        print("purpleandred")
    elif birinci_renk == "siyah" and ikinci_renk == "beyaz":
        print("blackandwhite")
    elif birinci_renk == "gri" and ikinci_renk == "sari":
        print("grayandyellow")
    else:
        print("rainbow")
    pass


''' q3
Girilen iki sayı arasında kalan sayıların toplamını hesaplayan 
python programını  döngüleri kullanarak yazınız ve sonucu ekrana yazdırınız. 
Örnek olarak 3 ve 7 sayıları girilmiş olsun. Bu durumda toplanacak değerler 
şu şekilde olmalı:  4 + 5 + 6 = 15    
'''


def ara_toplam(baslangic, bitis):
    topl = 0
    for i in range(baslangic + 1, bitis):
        topl += i
    return topl
    pass


''' q4
Girilen bir n sayisi için 0 ile n arasında (sıfır dahil, n dahil değil) olan sayıların ikili gösterimini alt alta ekrana yazdıran python programını yazınız. Örnek olarak n =4 olsun: bu durumda çıktı şu şekilde olmalı:

0b0
0b1
0b10
0b11

Not: bir sayını ikili sayıya çevirmek icin bin() fonksiyonunu kullanabilirsiniz.
'''


def dec2bin(n):
    for nn in range(0, n):
        print(bin(nn))
    pass


''' q5
Girilen bir n sayısı için aşağıdaki şartları sağlayan programı yazınız:

Bu program 1'den n'e kadar olan sayıların toplamını hesaplamalı (n dahil değil)
Eğer o esnada topladığınız sayı 23'e eşitse döngü bir sonraki değerden devam etmeli
Eğer toplam değeri 700'den büyükse program sonlanmalı
Son olarak toplamın en son değeri ekrana yazdırılmalıdır. 
'''


def sumOf(n):
    sum = 0
    for nn in range(1, n):
        if sum > 700:
            break
        if nn == 23:
            continue
        sum += nn
    print(sum)
    pass


''' q6
Verilen bir str türündeki değişken ve int türündeki sayı için ekrana ilk olarak ismi
 sonrasında bir boşluk bırakarak sayıyı yazdıran bir kodu fonksiyon içerisinde yazınız.
Yazacağınız fonksiyonun ismi "yazdir" olmalı ve 2 parametre içermelidir. 
İlk parametre str türüne ikinci parametre int türüne ait olacaktır.    

For example:

Test	Result
yazdir("elma",3)
elma 3
Answer:(penalty regime: 10, 20, ... %)
'''
def yazdir(s, n):
    print("%s %d" %(s, n))



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_hi('PyCharm')
    yazdir("elma", 3)
    sumOf(50)
    dec2bin(5)
    '''
    negpos(0)
    rainbow("mor", "kirmizi")
    rainbow("siyah", "beyaz")
    rainbow("gri", "sari")
    rainbow("mavi", "yesil")
    for i in range(0, 10):
        print(i, " Merhaba Dunya")
    '''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
