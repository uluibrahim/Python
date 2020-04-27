# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:39:35 2020

@author: ibrah
"""

# *** STRİNG FORMATLAMA ***

name="İbrahim"
surname="ULU"
# str ifadeden sonra .format() içine yazdığımız değişken str daki süüslü parantez içinde çalıştırılır.
# birden fazla argüman gönderilebilir.
# argümanlar sırayla çağırılır  1. paranteze 1. argüman eklenir.
"""
print("My name is {} {}".format(name,surname))

# indexs no vererek sırayı istediğimiz gibi ayarlayabiliriz.
print("My name is {1} {0}".format(name,surname))

# istenirsede değğişken tanımlanarak sıralama özelleştirileblir.
print("My name is {s} {n}".format(n=name,s=surname))

# aynı değişkeni birden fazla parantezde sırasız çağırabiliriz
print("My name is {s} {n} {s}".format(n=name,s=surname))



result=200/750

# r:1.3 yaparak virgül den sonra sadece 3 rakam almasını sağladık.
print("Sonnuc: {r:1.3}".format(r=result))

"""
""" 
    Üst kısımda yaptığımız format işlemlerine gerek kalmadan,
    f string ile değişkenlerimizi string içinde yazdırabilir.
    Diğer işlemlerden çok daha basit ve pratik
"""
# f string

print(f"My name is {name} {surname}")


