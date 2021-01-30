###Soru 1

###  Tuple

sayilar = (25, 12, 47, 48, 6, 19, 17)
print(min(sayilar) + max(sayilar) + len(sayilar)) 

# ekrana ne yazdırır?


# a) 62
# b) 61
# c) 60
# d) 59
# 
# Dogru Cevap = b 
# 
############################################################

#  Soru 2

###  Tuple

b = (1,2,3,4)
c = ("a","b","c","d")
f = b , c
print(f)

# işleminin sonucu nedir?
# 
# a) Hata verir
# b) (1, 2, 3, 4, 'a', 'b', 'c', 'd')
# c) ('a', 'b', 'c', 'd', 1, 2, 3, 4)
# d) ((1, 2, 3, 4), ('a', 'b', 'c', 'd'))
# 
# Doğru Cevap : d
# 

############################################################

# Soru 3: 

###  Tuple

temp  = ('h', 'w', 'e', 'o', 'l', 'r', 'l', 'l','o','d')

for i in range(0,len(temp),2):
    print(temp[i],end="")	

# ekrana ne yazdirir?
# 
# a) hello	
# b) world
# c) hweolrllod
# d) Hata verir
# 
# Doğru cevap: a
# 

############################################################

# Soru 4:

### List

liste1 = [1, 2, 3, 4, 5]
del liste1[3:]
for i in range(liste1[2]):
    liste1.extend([1,3])
print(liste1.count(3))

# ekrana ne yazdirir?
# 
# a) 1
# b) 2
# c) 3
# d) 4
# 
# Doğru cevap: d 
# 
############################################################

# Soru 5: 

### List

liste1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 

# listesinde 6000 sayısının yanına 7000 sayısını ekleyip 

# liste1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]  

# sonucunu veren kod aşağıdakilerden hangisidir?
# 
# a) liste1[2][2].append(7000)
# b) liste1[2].append(7000)
# c) liste1[3].append(7000)
# d) Hata verir
# 
# Doğru cevap: a

############################################################


# Soru 6: 

### List

liste1 = [1, 2, 3, 4, 5, 6, 7]
if len(liste1) % 3 == 1:
    liste1.pop()
    if len(liste1) % 3 == 2:
        liste1.pop()
    else:
        del liste1[1] 
else:
    liste1.remove(3)	

print(sum(liste1))

# ekrana ne yazdirir?
# 
# a) 25
# b) 19
# c) 15
# d) 21
# 
# Doğru cevap: b
# 

############################################################

# Soru 7:

# Dict

sonuc = ""
harf = {'a':'1','b':'2', 'c':'3' }
for i in harf.values():
    sonuc += i
print(sonuc)

# kodu ekrana ne yazdırır?
# 
# a) 6
# b) 123
# c) Hata verir
# d) abc
# 
# Dogru cevap: b
# 
############################################################

# Soru 8:

### Dict

sonuc = 1
rakamlar = { 1:'a',2:'b', 3:'c' }
for i in rakamlar:
    sonuc *= i
print(sonuc,i,sep=",")

# kodu ekrana ne yazdırır?
# 
# a) 6,3
# b) 1,3
# c) 1,1
# d) Hata verir
# 
# Dogru cevap: a
# 

############################################################

# Soru 9:

### Set

sayilar1 = {(100, 200), 100, 200 }
sayilar2 = {(100), (200), 100, 'a'}
print(sayilar1.intersection(sayilar2))

# ekrana ne yazdirir?
# 
# a) (100, 200)
# b) {200, 100}
# c) {100}
# d) 100
# 
# Doğru cevap: b
# 
############################################################

# Soru 10:

### Set

sayilar1 = {(100, 200), 100, 200 }
sayilar2 = {(100), (200), 100, 'a'}
sayilar1.intersection_update(sayilar2)
print(sayilar1)

# ekrana ne yazdirir?
# a) (100, 200) 
# b) {200, 100}
# c) {100}
# d) 100
# 
# Doğru cevap: b
