from fractions import Fraction as frac

###############################################################  
# Programinizi yazmaya bu yorumun altindan baslayiniz.        #
# Fonksiyon isimlerini ve parametre sayisini degistirmeyiniz. #
# Ust satiri kesinlikle silmeyiniz                            #
###############################################################


############# kullaniciFonksiyonlari #########################









############# ontanimli Fonksiyonlar #########################


def kesirKarsilastirma(kesir1, kesir2):
	""" 
	kesir1 ve kesir2, [pay, payda] seklinde tutulan iki elemanli listelerdir.
	Buyukten kucuge, ya da kucukten buyuge siralama yaparken iki kesrin karsilastirilmasini bu fonksiyon blogunda tanimlayiniz:

	Kodunuzu bu satirdan itibaren yaziniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:
	"""

	# kesir2 > kesir1 durumu
	return kesir2[0] * kesir1[1] > kesir2[1] * kesir1[0]


def kucuktenbuyuge(liste, eleman):
	""" 
	liste kucukten buyuge sirali olacagi icin 
	eklenecek 'eleman'in yerini tespit edip, uygun yere ekleyeceksiniz 
	Kodunuzu bu satirdan itibaren yaziniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:
	"""

	i = 0
	for i in range(len(liste)):
		# eleman, liste icindeki degerden buyuk degilse, yani kucuk veya esitse
		if not kesirKarsilastirma(liste[i], eleman):
	        # elemani ekleyecegimiz yeri bulduk
			break
	else:
        # eleman listedeki butun elemanlardan buyuk oldugu icin indis degerini bir artirip en sona ekliyoruz
		i += 1

	liste.insert(i, eleman)
            
    

def buyuktenkucuge(liste, eleman):
	""" 
	liste buyukten kucuge sirali olacagi icin 
	eklenecek 'eleman'in yerini tespit edip, uygun yere ekleyeceksiniz 
	Kodunuzu bu satirdan itibaren yaziniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:
	"""

	i = 0
	for i in range(len(liste)):
		# eleman, liste icindeki degerden buyukse diye kontrol ediyoruz
		if kesirKarsilastirma(liste[i], eleman):
			# elemani ekleyecegimiz yeri bulduk
			break
	else:
		# eleman, listedeki butun elemanlardan kucuk veya esit oldugu icin indis degerini bir artirip en sona ekliyoruz
		i += 1
		
	liste.insert(i, eleman)

def soru1(liste):
	""" 
	1. soru icin gerekenleri bu fonksiyonun altinda yapacaksiniz:
	liste1 icerisinde kucukten buyuge olan elemanlari, liste2 icerisinde de buyukten kucuge olan elemanlari tutacaksiniz 
	"""
	liste1 = []
	liste2 = []
	# Kodunuzu bu satirdan itibaren yaziniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz: 
	for reel in liste:
		pay = frac(str(reel)).numerator
		payda = frac(str(reel)).denominator
		if pay + payda > 50:
			kucuktenbuyuge(liste1, [pay, payda])
		else:
			buyuktenkucuge(liste2, [pay, payda])

	return liste1, liste2



def soru2(liste):
	""" 
	soru2 icerisinde istenilen sozlugu olusturduktan sonra, size verdigimiz ornekteki stile bagli kalarak sonucu ekrana yazdiriniz, 
	lutfen gorsellik katacagini dusunerek ekrana ekstra ifadeler bastirmayiniz.
	2. soru icin gerekenleri bu fonksiyonun altinda yapacaksiniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:
	"""
	sozluk = {}
	for reel in liste:
		pay = frac(str(reel)).numerator
		payda = frac(str(reel)).denominator
		if payda in sozluk.keys():
			sozluk[payda].append(pay)
		else:
			sozluk[payda] = [pay]

	for k in sozluk:
		if len(sozluk[k]) == 1:
			print(sozluk[k][0])
		else:
			toplam = 0
			for i in range(len(sozluk[k]) - 1):
				print(sozluk[k][i], "+ ", end="")
				toplam += sozluk[k][i]
			toplam += sozluk[k][len(sozluk[k]) - 1]
			print(sozluk[k][len(sozluk[k]) - 1], "=", toplam)

    


############ test ##############################################
""" 
Fonksiyon cagirma icin bir ornek, bu kismi kodunuzu test etmek icin yorumdan cikararak calistirabilir ve degisiklikler yapabilirsiniz:
Testleri tamamladiktan sonra, gondermeden once test kismini tamamen silebilir, ya da yoruma alabilirsiniz
"""

"""
i = 0
listeler = [[1.1, 13.86, 25.346, 17.1, 2.2], [1.7], [5.7], [10.9, 0.2, 0.6, 3], [1, 2, 3], [1, 2, 3, 50, 60, 70]]
for liste in listeler:
    print("Girdi", i, ":", liste)
    liste1, liste2 = soru1(liste)
    print(liste1)
    print(liste2)
"""
