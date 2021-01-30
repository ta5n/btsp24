import random

# print(random.randrange(3, 9))

def zar_at():
   roll = random.randrange(1,7)
   return roll
    
# def zar_at(zar_adedi=1):
#     donus = []
#     for i in range(zar_adedi):
#         donus.append(random.randrange(1,7))
#     return donus

print("Tutulan sayi " + str(zar_at()))
sonuc = zar_at()
print(sonuc)
# for sayi in sonuc:
#     print("gelen sayi: " + str(sayi))
# print(zar_at(3))




def km_gideri(depo_tutar, km_yol):
    return depo_tutar/km_yol*100
    
kurus = km_gideri(400, 1000)
print(kurus)

def tahmini_tuketim_gideri(litre_fiyat, ortalama_tuketim=5.4):
    return litre_fiyat * ortalama_tuketim

gerceklesen = tahmini_tuketim_gideri(6.64, 6.1)
print(gerceklesen)

kitabi = tahmini_tuketim_gideri(6.64)
print(kitabi)
