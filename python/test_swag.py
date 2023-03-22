from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Test_Swag:
    def test_passwors_username(self):
        driver=webdriver.Chorme(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        loginBtn=driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        errorMessage=driver.find_elements(By.CLASS_NAME,"error-button")        
        errorMessage.text= "Epic sadface: Username is required"

    def null_password():
         driver=webdriver.Chorme(ChromeDriverManager().install())
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/")
         inputname=driver.find_element(By.ID,"user-name")
         inputname.send_keys("Asuman")
         sleep(1)
         loginBtn=driver.find_element(By.ID,"login-button")
         loginBtn.click()
         sleep(2)
         errorMessage=driver.find_elements(By.CLASS_NAME,"error-button")        
         errorMessage.text= "Epic sadface: Password is required"

    def check_user():
         driver=webdriver.Chorme(ChromeDriverManager().install())
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/")
         inputname=driver.find_element(By.ID,"user-name")
         inputname.send_keys("locked_out_user")
         sleep(1)
         input_password=driver.find_element(By.ID,"password")
         input_password.send_keys("secret_sauce")
         loginBtn=driver.find_element(By.ID,"login-button")
         loginBtn.click()
         sleep(2)
         errorMessage=driver.find_elements(By.CLASS_NAME,"error-button")        
         errorMessage.text= "Epic sadface: Sorry, this user has been locked out."
        
    def button():
         driver=webdriver.Chorme(ChromeDriverManager().install())
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/")

         loginBtn=driver.find_element(By.ID,"login-button")
         loginBtn.click()
         sleep(2)
         button=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[1]/svg")
         errorMessage=driver.find_elements(By.CLASS_NAME,"error-button") 
         sleep(2)
         errorMessageBtn=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button/svg")
         errorMessageBtn.click()

    def user_login():
         driver=webdriver.Chorme(ChromeDriverManager().install())
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/")
         inputname=driver.find_element(By.ID,"user-name")
         inputname.send_keys("standard_user")
         sleep(1)
         input_password=driver.find_element(By.ID,"password")
         input_password.send_keys("secret_sauce")
         loginBtn=driver.find_element(By.ID,"login-button")
         loginBtn.click()
         sleep(2)
         driver.get("https://www.saucedemo.com/inventory.html")
         list=driver.find_elements(By.CLASS_NAME,"inventory_item")
         if(len(list)==6):
            print("giriş başarılı")





