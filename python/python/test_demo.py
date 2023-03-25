from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import  WebDriverWait #bekleme islemlerini yapar
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path #klasor olusturmak icin
from datetime import date
#prefix-->on ek e gore yani (test_)ile baslamali test fonk olarak gorur

class Test_DemoClass:
    def setup_method(self): #her testten once cagirilir
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
#gunun tarihini al bu tarih ile bir lasor var mı kontrol et yoksa 
        self.folderPath=str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True) #exist_ok=True ilgili klasor varsa olusturma demek
    
    
    def teardown_method(self): #her testten sonra cagrilir
        self.driver.quit() 
    #setup->test_demoFunc->teardown
    def test_demoFunc (self):
        # 3A Act Arrange Assert
        text="Hello"
        assert text=="Hello"
    #setup->test_demo2->teardown
    def test_demo2(self):
        assert True
    
    #bu alttaki yorum satiri decoratordur
    #@pytest.mark.skip() bu fonk test ederken atla dedik
    @pytest.mark.parametrize("username,password",[("1","1"),("kullaniciadin","sifren")])
    def test_invalid_login(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"username")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput=self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        sleep(2)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/text()")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text=="Epic sadface: Username and password do not match any user in this service"

        def waitForElementVisible(self,locator,timeout=5):
            WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator)) #max 5 sn olcak sekilde ilgili locatorun gorunmesini bekle
