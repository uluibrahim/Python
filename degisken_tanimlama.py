
#***deişken tanımlama***
print(50+68-47)
#yukarıdaki gibi sayilari veya başka tipleri print içinde uzunca yazmak yerine,
# kullanacağımız degerlere değişkenler aracılığıyla ulaşabiliriz.

# bir evin aylık fatura giderini hesaplayalım

kira=1500
elektrik=150
su=60
tel=50
isinma=200
toplamGider=kira+su+elektrik+tel+isinma
print(toplamGider)

# daha sonrada bu degerleritekrar tekrar kullanabiliriz
print(su+elektrik)

# değişken isimleri rakamla başlamaz

sayi1=45
sayi1=25 #sayi1 değişkeninin içindeki degeri değiştirdik.

sayi1 += 10 # sayi1 e += operatöriyle 10 eklemiş olduk
# sayi += 10 ile sayi1=sayi1+10 ifadeleri aynı anlamı taşır

# metinsel ifade için değişken kullanımı
# değişkenşn tutacağı deger tek tırnak veya çift tırkbak içinde yazılır.
isim='İbrahim'
soyIsim="ULU"
print(isim +" "+ soyIsim)
#print içerisinde string(metinsel) değişkenleri birleştirebiliriz.

# boolean tipi
# evet yada hayır  türünde bir deger saklamak istenirse kullanılır.

isStudent=True
print( isStudent)

# tek seferde birçok değişkene deger atayabilirz.

ad=a,b,isim2,soyIsim2, isStudent2=(4,5,'Esra',"KOÇ",False)
print(ad)

"""
    Genel Örnek
    Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

 Müşteri adı 
 Müşteri soyadı
 Müşteri adı+soyadı
 cinsiyet
 tc kimlik no
 doğum yılı
 adres bilgisi
 yaşı
 
"""
mAdi="İbrahim"
mSoyadi='ULU'
mAS=mAdi + " " + mSoyadi
cinsietErkek=True
tcKNo="12345678912" #hesaplama olmayacağından string olarak tanımladık
doguYili=1905
adres='Denizli'
yas=23

"""
    Genel örnek2
    Aşağıdaki siparişlerin toplam bilgisini hesaplayınız
    
    sipariş 1 => 110 tl
    
    sipariş 2 => 1100.5 tl
    
    sipariş 3 => 356.95 tl

"""

siparis1=110
siparis2=1100.5
siparis3=356.95 

siparisToplam=siparis1+siparis2+siparis3

print("Tüm sipariş toplamı: ",+ siparisToplam) 









