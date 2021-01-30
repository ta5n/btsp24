from fractions import Fraction as frac

###############################################################  
# Programinizi yazmaya bu yorumun altindan baslayiniz.        #
# Fonksiyon isimlerini ve parametre sayisini degistirmeyiniz. #
# Ust satiri kesinlikle silmeyiniz                            #
###############################################################


############# kullaniciFonksiyonlari #########################

def kesir(sayi):
    # verilen sayiyi, pay ve payda sirasiyla liste olarak donduruyoruz
    return [frac(str(sayi)).numerator, frac(str(sayi)).denominator]

############# ontanimli Fonksiyonlar #########################

def kesirKarsilastirma(kesir1, kesir2):
    """ 
    kesir1 ve kesir2, [pay, payda] seklinde tutulan iki elemanli listelerdir.
    Buyukten kucuge, ya da kucukten buyuge siralama yaparken iki kesrin karsilastirilmasini bu fonksiyon blogunda tanimlayiniz:
    
    Kodunuzu bu satirdan itibaren yaziniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:
    """
    # Birinci kesir kucuk ise True, ikinci kesir kucuk ise False donduruyoruz
    if kesir1[0]/kesir1[1] < kesir2[0]/kesir2[1]:
        return True
    return False

def kucuktenbuyuge(liste, eleman):
    """ 
    liste kucukten buyuge sirali olacagi icin 
    eklenecek 'eleman'in yerini tespit edip, uygun yere ekleyeceksiniz 
    Kodunuzu bu satirdan itibaren yaziniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:
    """
    if len(liste) == 0:
        # liste boş ise eleman listeye ekleniyor
        liste.append(eleman)
        return
    # listede eleman var ise liste tek tek eleman ile karsilastirilip
    # listede mevcut sayı elemandan kucuk ise sonraki liste elemanına ilerliyoruz
    # listedeki mevcut sayı büyük olduğunda araya elemanı ekliyoruz
    i = 0
    while i < len(liste) and kesirKarsilastirma(liste[i],eleman):
        i += 1
    liste.insert(i, eleman)
    return


def buyuktenkucuge(liste, eleman):
    """ 
    liste buyukten kucuge sirali olacagi icin 
    eklenecek 'eleman'in yerini tespit edip, uygun yere ekleyeceksiniz 
    Kodunuzu bu satirdan itibaren yaziniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:
    """
    if len(liste) == 0:
        # liste boş ise eleman listeye ekleniyor
        liste.append(eleman)
        return
    # listede eleman var ise liste tek tek eleman ile karsilastirilip
    # eleman listede mevcut sayıdan kucuk ise sonraki liste elemanına ilerliyoruz
    # listedeki mevcut sayı küçük olduğunda araya elemanı ekliyoruz
    i = 0
    while i < len(liste) and kesirKarsilastirma(eleman, liste[i]):
        i += 1
    liste.insert(i , eleman)
    return


def soru1(liste):
    """ 
    1. soru icin gerekenleri bu fonksiyonun altinda yapacaksiniz:
    liste1 icerisinde kucukten buyuge olan elemanlari, liste2 icerisinde de buyukten kucuge olan elemanlari tutacaksiniz 
    """
    liste1 = []
    liste2 = []
    # Kodunuzu bu satirdan itibaren yaziniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:

    # girdi olarak verilen listenin her bir elemanı için pay ve payda toplamı 50 ile karşılaştırılıp
    # 50 den büyük ise kucukten buyuge kesirleri tutan liste1 e aktarılmak için kucuktenbuyuge()
    # fonksiyonuna gonderiliyor, aksi durumda <= 50 için liste2 ye aktarılmak üzere buyuktenkucuge()
    # fonksiyonuna gonderiliyor
    for item in liste:
        if kesir(item)[0] + kesir(item)[1] > 50:
            kucuktenbuyuge(liste1, kesir(item))
        else:
            buyuktenkucuge(liste2, kesir(item))
    return liste1, liste2


def soru2(liste):
    """ 
    soru2 icerisinde istenilen sozlugu olusturduktan sonra, size verdigimiz ornekteki stile bagli kalarak sonucu ekrana yazdiriniz, 
    lutfen gorsellik katacagini dusunerek ekrana ekstra ifadeler bastirmayiniz.
    2. soru icin gerekenleri bu fonksiyonun altinda yapacaksiniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:
    """
    # girdi listesini pay ve payda ikilisi olarak listeye kaydediyoruz
    rational_num_list = list()
    for item in liste:
        rational_num_list.append(kesir(item))

    # rasyonel sayi listemizden paydaların uniq setini kaydediyoruz
    # bu seti sonuc sözlüğümüzün anahtarları olarak kullanacağız
    denom_set = set()
    for i in range(len(rational_num_list)):
        denom_set.add(rational_num_list[i][1])

    # tekrar etmeyen anahtarlar ile boş sözlüğümüzü oluşturuyoruz.
    result_dict = dict.fromkeys(denom_set, list())
    # payda setindeki her bir değer için
    for k in denom_set:
        # rasyonel sayılar listesinden her bir rasyonel sayı çiftini alıyoruz
        for item in rational_num_list:
            # aldığımız rasyonel sayının payda değeri setimizden bir sayı ile eşleşiyorsa
            if k == item[1]:
                if not result_dict[k]:
                    # ilk eleman olarak ekliyoruz
                    result_dict[k] = [item[0]]
                else:
                    result_dict[k].append(item[0])

    # sonuç sözlüğümüzdeki değerler listesinde her bir anahtara karşılık gelen değerler için
    # toplamı hesaplıyoruz
    for key, value in result_dict.items():
        if len(value) > 1:
            # eğer sıradaki değer birden fazla sayı içeriyorsa
            # listedeki her bir değeri toplama ekleyip ekrana yazdırıyoruz
            sums = 0
            for v in value:
                sums += v
                print(v, end="")
                # eğer sonuncu elemanda değilsek aralarına + işareti ekliyoruz
                if v != value[-1]:
                    print(" + ", end="")
                else:
                    # sonuncu elemandan sonra eşittir işareti ekliyoruz
                    print(" = ", end="")
            print(sums)
        else:
            # o anki değer liste yerine tek bir sayı ise sayımızı yazdırıyoruz
            print(value[0])


############ test ##############################################
""" 
Fonksiyon cagirma icin bir ornek, bu kismi kodunuzu test etmek icin yorumdan cikararak calistirabilir ve degisiklikler yapabilirsiniz:
Testleri tamamladiktan sonra, gondermeden once test kismini tamamen silebilir, ya da yoruma alabilirsiniz
"""
i = 0
listeler = [[1.1, 13.86, 25.346, 17.1, 2.2], [1.7], [5.7], [10.9, 0.2, 0.6, 3], [1, 2, 3], [1, 2, 3, 50, 60, 70]]
for liste in listeler:
    print("Girdi", i, ":", liste)
    liste1, liste2 = soru1(liste)
    print(liste1)
    print(liste2)

    soru2(liste)
    i += 1
    print("\n")

# liste3 = [2.2, 0.6, 2.7, 3.5, 5.5]
# soru2(liste3)
