from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import  WebDriverWait #bekleme islemlerini yapar
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class Test_Sauce:
    def __init__(self): #ctor olusturdum boylece bu classi kullandigim zaman ilk bura caliscak(Don't repeat yourself)
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    def test_invalid_login(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) #max 5 sn olcak sekilde user-name id'li elementin gorunmesini bekle
        usernameInput=self.driver.find_element(By.ID,"username")
        passwordInput=self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/text()")
        testResult=errorMessage.text =="HATALI GİRİŞ"
        print(f"TEST SONUCU {testResult}")
        
    def test_valid_login(self):
        self.driver.get("https://www.sauedemo.com/")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        passwordInput=self.driver.find_element(By.ID,"password")
        #Action Chains
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard-user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform() #ustteki 2 kod birlikte execute edilebilir oldu
        #usernameInput.send_keys("standard_user")
        #passwordInput.send_keys("secret_sauce")
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")  #javascript boyle cagrilir
testClass=Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()
while True:
    continue

