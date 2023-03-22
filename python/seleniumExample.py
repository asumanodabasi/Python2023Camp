#Selenium = Tarayicida yaptiklarimizi otomize eden bi yapi
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome(ChromeDriverManager().install())
#bu kodu driver i esitlemek icin yazdik bu yuzden chrromedriver i yuklemeye gerek kalmadi 
driver.maximize_window() #chromu tam ekran yapar
driver.get("https://www.google.com/") #uzerinde calistigimiz taryiciyi hangi url e gondermek istiyorsan onu yaz
#sleep(10)
# HTML Locators --->Seleniuma elementleri tanıtıyoz
input=driver.find_element(By.NAME,"q") #name=q olan yeri buldu
input.send_keys("kodlama.io")
searchButton=driver.find_element(By.NAME,"btnK")
sleep(2)
searchButton.click()
sleep(2)
firstResult=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCourses=driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlama.io sitesinde : {len(listOfCourses)} adet kurs var")

while True:
    continue 