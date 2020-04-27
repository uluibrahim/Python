# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:05:26 2020

@author: ibrah
"""

name ="ibrahim"
surname="ULU"
age=22

selam="My name is "+name+" "+surname+" and \nI am "+str(age)+"years old."
print(selam)
# \n bir alt satıra inmeye yarar.

""" String dizisinde herbir karakter index numrasıyla ulaşılabliri.
    Dizinin sağdan ilk karakterinin indexi 0 dır. 1 artarak sola ilerler.
    Dizinin sağdan ilk karakterinin indexi -1 dır. 1 azalarak sağa ilerler.
"""
print(selam[0])  # çıktı:  M olacaktır.
print(selam[-1]) # çıktı: . olacaktır.
print(selam[-10])

# Dizinin kaç karakterli olduğunu bulabilmek için len fonksiyonunu kullanabiliriz.
length=len(selam)
print(length)
# len yardımıylada son karaktere ulaşabiliriz.
print(selam[length-1]) # -1 yazmanın nedeni dizinin 1 den değil 0 dan başlamasıdır.

print(selam[3:7]) # 3,4,5,6 (3 ten 7 ye kadar olan) indexleri aldı.
print(selam[3: ]) # 3. indexten başlar dizinin sonuna kadar gider
print(selam[:18]) # en baştan başla 18 e kadar.
print(selam[2:40:2]) # 2 den başla 40 a kadar 2 den 1 i al.



