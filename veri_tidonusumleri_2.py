# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:41:10 2020

@author: ibrah
"""

"""
     Daire alanı πr2 (pi r kare)
     Dairenin çevresi 2πr
     
     *yarı çapı verilen bir dairenin alan ve cevresini hesaplayınız.
     pi=3.14
"""

pi=3.14
r=input("Yarı çap giriniz:")
r=float(r)

alan=pi*(r**2)

cevre=2*pi*r

print("Alan: ",+alan)
print("Cevre: ",+cevre)



