from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
while(True):
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.socialcube.net/login")
    email_field = driver.find_element_by_id("inputEmail")
    email_field.send_keys("max.musterman@gmail.com")
    password_field = driver.find_element_by_id("inputPassword")
    password_field.send_keys("ChangePassword")
    loginButton = driver.find_element_by_class_name("btn.btn-primary")
    loginButton.click()
    driver.get("https://www.socialcube.net/games/thebutton");
    thebutton = driver.find_element_by_class_name("btn.btn-primary")
    thebutton.click()
    time.sleep(5)
    driver.close()
    time.sleep(60*30)
