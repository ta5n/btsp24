# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# =============================================================================
# q1
# Sırasıyla aşağıdaki işlemleri yapınız:
#
# Sırasıyla 10'dan 20'ye kadar olan (20 dahil) tamsayıları içeren, ardından
# alfabenin "abcdefghijklmnopqrstuvwxyz" harflerini içeren bir "list" verisi
# oluşturunuz ve ekrana yazdırınız.
# Oluşturduğunuz listenin uzunluğunu yazdırınız.
# Oluşturduğunuz listeden 'k' harfini çıkarınız ve listeyi yazdırınız.
# Oluşturduğunuz listeye sırasıyla 'a' karakterini, 3 rakamını, 'a' karakterini
# ve 58 sayısını ekleyiniz.
# Oluşturduğunuz listedeki 'a' karakterinin tekrarlanma sayısını bulunuz ve
# ekrana yazdırınız.
# Listedeki 17. indeksden 27. indekse  (27 dahil değil) kadar siliniz ve
# listeyi ekrana yazdırınız.
#
# =============================================================================


# mylist = [*range(10, 21)]
# alphabet = []
# for letter in range(97, 123):
#     alphabet.append(chr(letter))
# mylist += alphabet
# print(mylist)
# print(len(mylist))

# mylist.remove('k')
# print(mylist)

# mylist.append('a')
# mylist.append(3)
# mylist.append('a')
# mylist.append(58)

# print(mylist.count('a'))

# del mylist[17:27]
# print(mylist)

# =============================================================================
# q2
# Döngüleri kullanarak size girdi olarak verilen list türündeki yapının elemanlarını
# toplayıp sonucu ekrana yazdırınız.
#
# For example:
#
# Test	Result
# toplama([1,2,3,4,5])
# 15
# =============================================================================


def toplama(sayiListesi):
    sum = 0
    for num in sayiListesi:
        sum += num
    print(sum)


# =============================================================================
# q3
# Elimizde tamamen aynı list türünde iki liste bulunmaktadır. Fakat x ışınları bu
# listelerden birinin elemanlarının bazılarında değişikliğe sebep olmuştur. Bu soruda
# iki listeyi karşılaştırmanızı ve kaç tane elemanın farklı olduğunu bulup bunu ekrana
# yazdırmanızı istiyoruz. Bunun için:
# karsilastir fonksiyonunu tanımlamanız ve bu fonksiyonun iki parametre içermesi
# gerekmektedir. bütün işlemlerin karsilastir fonksiyonu içinde olması  gerekmektedir.
# Parametre olarak verilen listelerin aynı sayıda eleman içerdiğini varsayabilirsiniz.
# For example:
#
# Test	Result
# karsilastir([0,1,2,1,2,1,2],[1,1,1,1,3,1,2])
# 3
#
# =============================================================================


def karsilastir(list1, list2):
    diff = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            diff += 1
    print(diff)


# karsilastir([0, 1, 2, 1, 2, 1, 2], [1, 1, 1, 1, 3, 1, 2])

# =============================================================================
# q4
# Küçükten büyüğe sıralı olarak verilmiş bir listeye yeni bir elemanı listenin
# sıralanmış özelliğini bozmadan ekleyeniz. Yazacağınız programın aşağıdaki şartları
# sağladığına dikkat ediniz:
#
# İki parametreli "insert" fonksiyonunu tanımlayınız. Bu fonksiyonun ilk parametresi
# list, ikinci parametresi int türüne ait olmalıdır.
# Yeni sayıyı ekledikten sonra listenin son halini ekrana yazdırınız.
#
# =============================================================================


def insert(list1, num):
    p = 0
    while p < len(list1) and num > list1[p]:
        p += 1
    list1.insert(p, num)
    print(list1)


# insert([2, 3, 5, 6], 9)

# =============================================================================
# q5
# Size verilen bir liste veri yapısında bulunan karakter dizilerinin uzunluklarını
# listedeki sırayı bozmadan alt alta yazdırınız. Cevabınızı "lenListElements"
# fonksiyonunun içine yazınız.
#
# Örnek: ["ali","veli","ahmet","a"] listesinin çıktısı aşağıdaki gibi olmalıdır:
#
# 3
# 4
# 5
# 1
#
# =============================================================================


def lenListElements(list1):
    for el in list1:
        print(len(el))


# lenListElements(["ali", "veli", "ahmet", "a"])


# =============================================================================
# q6
# Aynı uzunlukta sadece tamsayılardan oluşan iki list veri yapısı (A ve B) için
# aşağıdaki şartları sağlayan programı yazınız:
#
# A ve B listelerinin aynı indekslerindeki elemanları karşılaştırınız.
# Eğer A listesindeki eleman B listesindekinden büyükse +1
# Eğer B listesindeki eleman A listesindekinden büyükse -1
# Eşitse 0 (sıfır) ile  değerlendiriniz.
# Sonuçta oluşan değeri ekrana yazdırınız.
# Kodunuzun hepsini "karsilastir" fonksiyonu içinde yazınız.
# Örnek:
#
# A = [1,2,4,6]
#
# B = [0,2,5,4]
#
# A listesinin ilk elemanı B listesinin ilk elemanından büyüktür.  (+1)
#
# A listesinin ikinci elemanı B listesinin ikinci elemanına eşittir. (0)
#
# A listesinin üçüncü elemanı B listesinin üçüncü elemanından küçüktür. (-1)
#
# A listesinin son elemanı B listesinin son elemanından büyüktür. (+1)
#
# Buna göre 1 + 0 - 1 + 1 = 1 olduğundan ekrana sadece 1 değeri yazdırılır.
# =============================================================================


def karsilastir(A, B):
    sum = 0
    for p in range(len(A)):
        if A[p] > B[p]:
            sum += 1
        elif A[p] < B[p]:
            sum -= 1
    print(sum)


# A = [1, 3, 4, 6]
# B = [0, 2, 5, 4]
# karsilastir(A, B)


# =============================================================================
# q7
# Verilen bir listedeki elemanların dict veri yapısındaki bir değişkende anahtar kelime
# olarak kullanılıp kullanılmadığını kontrol eden ve eğer anahtar kelime olarak
# mevcutsa bu değerleri çarpıp sonucu ekrana yazdıran programı yazınız. Programinizi
# iki parametreli "carpma" fonksiyonu icinde yaziniz.
#
# Not: Hiçbir eşleşme olmadığı durumda ekrana 1 yazdırılmalıdır.
#
# Örnek:
#
# liste = [1,3,5,7]
#
# sozluk = {1 : 5, 5 : 15 }
#
# liste değişkeninden sadece 1 ve 5 anahtarları sözlükte olduğundan bu iki anahtara
# karşılık gelen değerleri çarpıp ekrana
# 75
# yazdırıyoruz.
# =============================================================================


def carpma(liste, sozluk):
    sonuc = 1
    for el in liste:
        sonuc *= sozluk.get(el, 1)
    print(sonuc)


# liste = [1, 3, 5, 7]
# sozluk = {1: 5, 5: 10, 3: 2}

# carpma(liste, sozluk)
