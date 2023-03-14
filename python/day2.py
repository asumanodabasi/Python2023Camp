faiz=1,53
vade="36"
krediAdi="Taşit Kredisi"
print(type(faiz)) #faiz degiskninin tipini verir
print(int(vade)+12) #vadenin tipi stringti int donusturduk(tip donusumu)
vade=input("Sayı gir: ")  #kullanıcıdan bilgi alir
print(type(vade))#kullanıcıdan alınana input python da default olarak string tir!!
print(int(vade)+12) #bu islemi yapmak icin strig olan vadeyi int e cevirdik
vade=int(input("sayi gir:")) #boyle de yapabiliriz
vade=vade+12

#string interpolation
print("Sectiginiz vade sonucu ortya cıkan vade:"+ str(vade))
print("Sectiginiz vade sonucu ortya cıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Sectiginiz vade sonucu ortya cıkan vade: {vade}")
#3 farkli kullanim
isim="Asuman"
metin="Merhaba {name}".format(name=isim)
print(metin)

#f-string
metin=f"Hosgeldiniz {isim}"
print(metin)

#listeler
krediler=["İhtiyac Kredisi","Tasit Kredisi","Konut Kredisi"]
print(krediler[0])
print(len(krediler)) #length
krediler.append("Ozel Kredi") #listedeki son indexe eleman ekler #append
krediler.pop() #son indexteki(-1) elemani siler.içine sayi girersen o indexi siler
krediler.remove("Tasit Kredisi") #index bazlı degil deger bazli silme islemi yapar ilk gordugu Tasit Kredisi ni siler
krediler.extend("Y Kredisi" ,"Z Kredisi") #birden fazla degeri tek satirda eklememizi sagladi
#ptyhon da farkli veri tiplerinden dizi olusturulabilir
dizi=["ihtiyac kredisi",10,5.2,False]
print(dizi)

#donguler
#for
for i in range(10):
    print("xx")
    print(i)
for i in range(5,10):
    print(i)
for i in range(0,51,10): #0 dan 50 ye kadar 10 ar artarak yazar
    print(i) 

krediler=["İhtiyac Kredisi","Tasit Kredisi","Konut Kredisi"]
for kredi in krediler:
    print(kredi)
for i in range(len(krediler)): #yukardaki kodla ayni islemi yapar.
    print(krediler[i])

#while
i=0
while i<10:
    print("x")
    i+=1 

#fonksiyonlar    
def sayHello(name):
    print(f"Hello {name}")
sayHello("Asuman")
fiyat=100
indirim=20
def calculate():
    print(100-20)
def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)
calculateWithParams(50,30)
calculate()

#geriye donduren fonksiyon ornegi
def caculateAndReturn(fiyat,indirim):
    return fiyat-indirim
yeniFiyat=caculateAndReturn(200,50)
print(yeniFiyat)
