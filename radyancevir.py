#!-*- coding: cp1254 -*-

import math
print "Derece-radyan �evirici. S�r�m 1.1"
print "2011 Berat Alp Erbil"
print "Dosya yaz�m� a��k"
dosya = open("log.txt","a")
while True:
    
    cevir = input("L�tfen dereceden radyana �evirece�iniz dereceyi girin: ")
    derece = math.radians(cevir)
    print derece
    dosya.write(str(derece))
    cik = raw_input("��kmak istiyor musunuz: ")
    if cik == "e":
        break
    else:
        pass
