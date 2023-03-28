from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import  WebDriverWait #bekleme islemlerini yapar
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
class Test_Swag:
    
    def setup_method(self):
          driver=webdriver.Chrome(ChromeDriverManager().install())
          driver.maximize_window()
          driver.get("https://www.saucedemo.com/")
          self.folderPath(str(date.today()))
          Path(self.folderPath).mkdir(exist_ok=True)


    def teardown_method(self):
          self.driver.quit()

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))


    def test_password_username(self):
        self.waitForElementVisible(By.ID,"login-button")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        errorMessage=self.driver.find_elements(By.CLASS_NAME,"error-button") 
        self.driver.save_screenshot(f"{self.folderPath}test_password_username.png")       
        assert errorMessage.text== "Epic sadface: Username is required"

    @pytest.mark.parametrize("username",[("hiked","standard_user","problem_user")])
    def test_null_password(self,username):
         self.waitForElementVisible(By.ID,"user-name")
         inputname=self.driver.find_element(By.ID,"user-name")
         loginBtn=self.driver.find_element(By.ID,"login-button")
         loginBtn.click()
         sleep(2)
         errorMessage=self.driver.find_elements(By.CLASS_NAME,"error-button")   
         self.driver.save_screenshot(f"{self.folderPath}test_null_password{username}.png")     
         assert errorMessage.text== "Epic sadface: Password is required"

   # @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_check_user(self,username,password):
         self.waitForElementVisible(By.ID,"user-name")
         
         inputname=self.driver.find_element(By.ID,"user-name")
         input_password=self.driver.find_element(By.ID,"password")
         loginBtn=self.driver.find_element(By.ID,"login-button")
         
         actions=ActionChains(self.driver)
         actions.send_keys_to_element(inputname)
         actions.send_keys_to_element(input_password)
         actions.send_keys_to_element(loginBtn,Keys.Enter)
         actions.perform()
         
         sleep(2)
         errorMessage=self.driver.find_elements(By.CLASS_NAME,"error-button") 
         self.driver.save_screenshot(f"{self.folderPath}test_check_user{username},{password}.png")       
         assert errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        
    def test_button(self):
         self.waitForElementVisible(By.ID,"login-button")
         loginBtn=self.driver.find_element(By.ID,"login-button")
         loginBtn.click()
         sleep(2)
         button=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[1]/svg")
         errorMessage=self.driver.find_elements(By.CLASS_NAME,"error-button") 
         sleep(2)
         errorMessageBtn=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button/svg")
         errorMessageBtn.click()
         self.driver.save_screenshot(f"{self.folderPath}test_button.png")    
         assert errorMessageBtn==0

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])    
    def test_user_login(self,username,password):
         self.waitForElementVisible(By.ID,"user-name")
         inputname=self.driver.find_element(By.ID,"user-name")
         inputname.send_keys(username)
         self.waitForElementVisible(By.Id,"password")
         input_password=self.driver.find_element(By.ID,"password")
         input_password.send_keys(password)
         loginBtn=self.driver.find_element(By.ID,"login-button")
         loginBtn.click()
         sleep(2)
         self.waitForElementVisible(By.CLASS_NAME,"inventory_item")
         list=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
         self.driver.save_screenshot(f"{self.folderPath}test_user_login{username}-{password}.png")
         assert len(list)==6


    @pytest.mark.parametrize("username,password",[("standard_user","1"),("problem_user","sfggdff"),("performance_glitch_user","23"),("locked_out_user","jdjdj")])        
    def test_wrong_password(self,username,password):
      self.waitForElementVisible(By.ID,"user-name")

      inputname=self.driver.find_element(By.ID,"user-name")
      inputpassword=self.driver.find_element(By.ID,"password")
      loginBtn=self.driver.find_element(By.ID,"login-button")


      actions=ActionChains(self.driver)
      actions.send_keys_to_element(inputname)
      actions.send_keys_to_element(inputpassword)
      actions.send_keys_to_element(loginBtn,Keys.Enter)
      actions.perform()
      
      error_message=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button/svg")
      self.driver.save_screenshot(f"{self.folderPath}test_wrong_password{username}-{password}.png")
      assert error_message=='Epic sadface: Username and password do not match any user in this service'

    @pytest.mark.parametrize("username",[("standard_user"),("problem_user"),("locked_out_user"),("performance_glitch_user")])
    def test_add_to_cart(self,username):
     self.waitForElementVisible(By.ID,"user-name")
     inputname=self.driver.find_element(By.ID,"user-name")
     inputpassword=self.driver.find_element(By.ID,"password")
     loginBtn=self.driver.find_element(By.ID,"login-button")


     actions=ActionChains(self.driver)
     actions.send_keys_to_element(inputname)
     actions.send_keys_to_element(inputpassword,"secret-sauce")
     actions.send_keys_to_element(loginBtn,Keys.Enter)
     actions.perform()

     self.waitForElementVisible(By.CLASS_NAME,"inventory_item")

     productName=self.driver.find_elements(By.CLASS_NAME,"inventory_item_name")
     list=[]
     for x in productName:
       names=x.text.replace(" ","-").lower()
       list.append(names)

     products=self.waitForElementVisible(By.CLASS_NAME,"inventory_item")
     i=0
     for product in products:
          self.waitForElementVisible(By.CLASS_NAME,"btn_inventory")
          addToCart=self.driver.find_element(By.ID,f"add-to-cart{list[i]}") 
          addToCart.click()
          i+=1
     shopping=self.driver.find_element(By.ID,"shopping-cart-container")
     self.driver.save_screenshot(f"{self.folderPath}test_add_to_cart.png")
     assert shopping==6

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_filter(self,username,password):
          self.waitForElementVisible(By.ID,"user-name")

          inputname=self.driver.find_element(By.ID,"user-name")
          inputpassword=self.driver.find_element(By.ID,"password")
          loginBtn=self.driver.find_element(By.ID,"login-button")

          actions=ActionChains(self.driver)
          actions.send_keys_to_element(inputname)
          actions.send_keys_to_element(inputpassword)
          actions.send_keys_to_element(loginBtn,Keys.Enter)
          actions.perform()

          filtrele = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select")
          filtrele.click()
          filtrele2 = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[2]")
          self.driver.save_screenshot(f"{self.folderPath}/test-filter.png")
          filtrele2.click()

