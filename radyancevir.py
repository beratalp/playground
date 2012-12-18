#!-*- coding: cp1254 -*-

import math
print "Derece-radyan çevirici. Sürüm 1.1"
print "2011 Berat Alp Erbil"
print "Dosya yazımı açık"
dosya = open("log.txt","a")
while True:
    
    cevir = input("Lütfen dereceden radyana çevireceğiniz dereceyi girin: ")
    derece = math.radians(cevir)
    print derece
    dosya.write(str(derece))
    cik = raw_input("Çıkmak istiyor musunuz: ")
    if cik == "e":
        break
    else:
        pass
