import matematik as m  #takma isim verdik 
import random
from day2 import sayHello
from human import Human

from seleniumExample import webdriver
print(m.Matematik.topla(10,20))
print(random.randint(0,100))
human1=Human("Ali")
human1.talk("Merhaba")

chromDriver=webdriver.Chrome()
