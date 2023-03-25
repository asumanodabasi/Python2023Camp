#self-->this  yani sinifin icinde bi degiskene ya da metoda ulasmak icin (self.) diyerek kullaniriz

class Human:
    #built-in
    #initialize
    def __init__(self,name): #constructor
        self.name=name
        print("bir human instance ı üretildi")

    def __str__(self):
        return f"str fonksiyonndan donen deger: {self.name}"
    

    def talk(self,sentence):
        print(f"{self.name} is talking.. {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

