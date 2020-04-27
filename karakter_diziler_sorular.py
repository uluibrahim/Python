# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:01:07 2020

@author: ibrah
"""
website="http://www.sadikturan.com"
course="Python kursu: baştan sona python programlama rehberinin(40saat)"

"""
1 'course' karakter dizisinde kaç karakte bulunmaktadır?
2 'website' içinde www karakterlerini alın
3 'wesite' içinde com karakterlerini alın
4 'course' içinden ilk 15 ve son 15 karakterleri alın.
5 'course' ifadesindeki karakterleri tersten yazdırın
"""
name,surname,age,job="Bora","Yılmaz",32,"mühendis"

"""
  6  yukarıdaki değişkenleri kullanarak
    'benim adım bora yılmaz, yaşım 22 ve mesleğim mühendis.'
  7 'Hello world' ifadesindeki w karkterini W karakteri ile değiştirin
  
  8 'abc' ifadesini yanyana 3 defa yazdırın

"""
"""
# 1
lengthCourse=len(course)
print(lengthCourse)

#2
wwwKarakterleri=website[7:10]
print(wwwKarakterleri)

#3
comKarekterleri=website[22:25]
print(comKarekterleri)

#4
ilk15=course[0:15]
son15=course[63-15:63]
ilk15VeSon15=ilk15+" "+son15
print(ilk15VeSon15)


#5
# :: tüm karakterleri al demktir.
tersten=course[::-1]
print(tersten)

#6
print(f"Benim adım {name} {surname}, yaşım {age} mesleğim {job}")


#7
ifade="Hello world"
ifade=ifade[0:6]+"W"+ifade[7:]

print(ifade)

#8

sonuc="abc "*3
print(sonuc)
"""