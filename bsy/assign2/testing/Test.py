import os
import importlib
import sys, io
from itertools import permutations  
import pandas as pd
from math import ceil

def permutasyonlar(liste):
    # Parametre olarak verilen listenin butun permutasyonlarini olustur
    sonuc = []
    perm = permutations(liste)

    if len(liste) == 1:
        sonuc.append(str(liste[0]))

    else:
        for permut in list(perm):
            # Her permutasyon icin toplam ifadesini elde edip, sonucu don, ornegin liste = [1, 2] ise, sonuc = ['1+2=3', '2+1=3']
            toplam = 0
            result = ""
            for i in range(len(permut) - 1):
                result += str(permut[i]) + "+"
                toplam += permut[i]

            toplam += permut[len(permut) - 1]
            result += str(permut[len(permut) - 1]) + "=" + str(toplam)
            sonuc.append(result)

    return sonuc


def testIt(dosya, testNo, test):
    module = importlib.import_module(os.path.splitext(dosya)[0])

    # sys.stdout objesini oldstdout olarak sakliyoruz, boylece calistiracagimiz .py dosyasinin ekrana yazdirdiklarini alacagiz
    oldstdout = sys.stdout
    sys.stdout = io.StringIO()

    # her test icin iki fonksiyon cagirilacak, toplam sonuc en fazla 2 olacak
    dogruSayisi = 0
    
    try:
        # dogruTestSayisi degiskeni verilen test icin ekrana yazilmasi gereken satirlarin kac tanesinin dogru oldugunu tutuyor
        dogruTestSayisi = 0
        module.soru2(test[0])
        output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__

        # cagirilan .py dosyasinin ekrana yazdirdigi satirlari newline karakterine gore split edip result degiskenine atiyoruz
        result = output.split("\n")

        # yaptigimiz test icin gelen butun payda degerleri icin gereken permutasyonlari olusturup, toplam ifadesini yazdiriyoruz
        allResults = []
        for anahtar in test[3]:
            allResults.append(permutasyonlar(test[3][anahtar]))

        # cagirilan .py dosyasinin ekrana yazdirdigi satirlarin her birisini i degiskenine atiyoruz
        for i in result:
            print("Yazdirilan satir: ", i)

            # butun permutasyonlara bakiyoruz
            for j in allResults:
                print("Olasi sonuclar: ", j)
                puan = False
                for satir in j:

                    # bu permutasyonlar icinden herhangi birisi bosluklari silinmis i degiskenine esit ise kullanici ekrana dogru yazdirmis
                    if i.replace(" ", "") == satir:
                        print("Test No: %d, soru2 icin dogru sonuc.\n" %(testNo))
                        dogruTestSayisi += 1
                        puan = True
                        break
                if puan:
                    break
            else:
                # butun permutasyonlari inceledik ancak kullanici dogru sonucu ekrana yazdiramamis
                print("Test No: %d, soru2 icin yanlis sonuc.\n" %(testNo))
        
        # kullanicinin bu testin soru2 kismindan alacagi puan : (ekrana dogru bastirdigi satir)/(toplam yazdirilmasi gereken satir)
        dogruSayisi += dogruTestSayisi/len(test[3])
    
    except:
        # soru2 icin herhangi bir exception olusursa kullanici bu sorudan puan alamiyor
        sys.stdout = sys.__stdout__
        print("Test No: %d, soru2 hata" %(testNo))

    
    try:
        a = module.soru1(test[0])
        # soru1 icin verdigimiz girdi icin 1. ve 2. indiste sakladigimiz listeler donuyor ise kullanici tam puan alir
        if a[0] == test[1]:
            print("Test No: %d, soru1 icin liste1 dogru.\n" %(testNo))
            dogruSayisi += 0.5
        if a[1] == test[2]:
            print("Test No: %d, soru1 icin liste2 dogru.\n" %(testNo))
            dogruSayisi += 0.5
        if a[0] != test[1] and a[1] != test[2]:
            print("Test No: %d, soru1 icin yanlis sonuc.\n" %(testNo))
    
    except:
        print("Test No %d, soru1 hata" % (testNo))
    
    return dogruSayisi


def main():
    testCases = {
            1: ([49.4, 30.6, 22.0625, 20.15625, 4.5625, 3.25, 1.5], [[73, 16], [645, 32], [353, 16], [153, 5], [247, 5]], [[13, 4], [3, 2]], {5: [247, 153], 16: [353, 73], 32: [645], 4: [13], 2: [3]}),
            2: ([0.275, 50,  1.04, 1.01, 24.5, 23.75], [[11, 40], [101, 100], [26, 25], [95, 4], [49, 2], [50, 1]], [], {40: [11], 1: [50], 25: [26], 100: [101], 2: [49], 4: [95]}),
            3: ([1.1, 13.86, 25.346, 17.1, 2.2], [[693, 50], [171, 10], [12673, 500]], [[11, 5], [11, 10]], {10: [11, 171], 50: [693], 500: [12673], 5: [11]}),
            4: ([1.04, 10.25, 49, 0.4, 50, 1.01, 0.15625, 23.75, 1.6, 1.04, 23.75], [[101, 100], [26, 25], [26, 25], [95, 4], [95, 4], [50, 1]], [[49, 1], [41, 4], [8, 5], [2, 5], [5, 32]], {25: [26, 26], 4: [41, 95, 95], 1: [49, 50], 5: [2, 8], 100: [101], 32: [5]}),
            5: ([1.6, 10.25, 49, 49,  0.4, 50, 1.01, 0.15625, 23.75, 1.6, 0.15625, 1.04], [[101, 100], [26, 25], [95, 4], [50, 1]], [[49, 1], [49, 1], [41, 4], [8, 5], [8, 5], [2, 5], [5, 32], [5, 32]], {5: [8, 2, 8], 4: [41, 95], 1: [49, 49, 50], 100: [101], 32: [5, 5], 25: [26]}),
            6: ([1.6],[], [[8, 5]], {5: [8]}),
            7: ([50], [[50, 1]], [], {1: [50]} ),
            8: ([0.7, 1.6, 2.15625, 0.5625, 10.25, 49], [[69, 32]], [[49, 1], [41, 4], [8, 5], [7, 10], [9, 16]], {10: [7], 5: [8], 32: [69], 16: [9], 4: [41], 1: [49]}),
            9: ([1, 2, 41, 4, 9], [], [[41, 1], [9, 1], [4, 1], [2, 1], [1, 1]], {1: [1, 2, 41, 4, 9]}),
            10: ([0.6, 2.2, 2.7, 3.5, 5.5], [], [[11, 2], [7, 2], [27, 10], [11, 5], [3, 5]], {5: [3, 11], 10: [27], 2: [7, 11]}),
            }
 
    dosyalar = os.listdir()
    # raw_data = {'Numara': [], 'Not': []}
    # df = pd.DataFrame(raw_data, columns = ['Numara', 'Not'])
    f = open("Puanlar.txt", "a")
    f.write("Numara" + "\t" "Puan" + "\n")

    for dosya in dosyalar:
        print("Calisan Dosya: ", dosya)

        if dosya == __file__ or dosya[-2:] != 'py':
            continue
        
        toplam = 0
        for test in testCases:
            print("--------------------------------------------------------")
            print("Test No: %d" %(test)) 
            testPuani = testIt(dosya, test, testCases[test])
            print("Test puani: %f" %(testPuani))
            toplam += testPuani
            print("--------------------------------------------------------")
        
        print("Dogru : %f/%d" %(toplam, 2 * len(testCases)))
        print("Ogrenci No: ", dosya[1:-3])
        print("Not : %d\n\n" %(ceil(5 * toplam)))
        f.write(dosya[1:-3] + "\t" + str(ceil(5 * toplam)) + "\n")

        # raw_data['Numara'].append(dosya[1:-3])
        # raw_data['Not'].append(ceil(5 * toplam))
    
    # df.to_excel('Sonuc.xlsx', sheet_name='Sonuclar')
    f.close()

if __name__ == "__main__":
    main()
