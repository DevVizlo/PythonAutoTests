from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

textFormUsername = driver.find_element(By.CSS_SELECTOR, '#user-name')
textFormPassword = driver.find_element(By.CSS_SELECTOR, '#password')
textFromLoginButton = driver.find_element(By.CSS_SELECTOR, '#login-button')

if textFormUsername is None and textFormPassword is None and textFromLoginButton is None:
    print('Не все элементы обнаружены')
else:
    print('Все элементы обнаружены')
