class Matematik:
  def __init__(self,sayi1,sayi2): #consturactor 
    self.sayi1=sayi1
    self.sayi2=sayi2
    print("Matematik başladı(referansı olustu)")
  def topla(self):
    return self.sayi1+self.sayi2
  def cikar(self):
    return self.sayi1-self.sayi2
  def bol(self):
    return self.sayi1/self.sayi2
  def carp(self):
    return self.sayi1*self.sayi2

matematik=Matematik(6,7)
sonuc=matematik.topla()
print("Sonuc : " +str(sonuc))