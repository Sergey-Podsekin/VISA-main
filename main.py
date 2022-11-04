from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://yopmail.com/en/')

driver.implicitly_wait(20)
inputElement = driver.find_element(By.ID, 'login')
inputElement.send_keys('visa-france')
inputElement.send_keys(Keys.ENTER)

driver.find_element(By.ID, 'newmail').click()


