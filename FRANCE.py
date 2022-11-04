import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

#options = Options()
#options.headless = True
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


def send_to_telegram(message):  # Telegram bot

    apiToken = '5704612050:AAEIS4ZcP19CDgZ5-g3uNFxw64Dvsmn0HRA'
    chatID = '-819110848'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

def send_to_telegram_log(message):  # Telegram bot

    apiToken = '5704612050:AAEIS4ZcP19CDgZ5-g3uNFxw64Dvsmn0HRA'
    chatID = '-860708556'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)


count = 1

driver.get("https://consulat.gouv.fr/ambassade-de-france-a-minsk/rendez-vous?name=R%C3%A9ception%20des%20demandes"
           "%20de%20visa")

driver.implicitly_wait(20)
driver.find_element(By.XPATH, '//button[@class="fr-btn fr-btn--primary fr-icon-check-line fr-btn--icon-left "]').click()

driver.implicitly_wait(20)
driver.find_element(By.XPATH, '//div[4]/button').click()

driver.implicitly_wait(20)
driver.find_element(By.CLASS_NAME, 'custom-control-label').click()

driver.implicitly_wait(20)
driver.find_element(By.XPATH, '//button[@class="fr-btn fr-btn--primary fr-icon-check-line fr-btn--icon-left "]').click()

while True:

    try:
        time.sleep(3)
        elem = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//p[@class="lead fr-text mt-4 mb-3 text-center"]')))

        driver.get(
            "https://consulat.gouv.fr/ambassade-de-france-a-minsk/rendez-vous?name=R%C3%A9ception%20des%20demandes"
            "%20de%20visa")
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH,
                            '//button[@class="fr-btn fr-btn--primary fr-icon-check-line fr-btn--icon-left "]').click()

        driver.implicitly_wait(20)
        driver.find_element(By.XPATH, '//button[@class ="btn btn-primary btn-md"]').click()

        driver.implicitly_wait(20)
        driver.find_element(By.XPATH,
                            '//button[@class="fr-btn fr-btn--primary fr-icon-check-line fr-btn--icon-left "]').click()

    finally:
        send_to_telegram(
            "Свободные места на визу Франция https://consulat.gouv.fr/ambassade-de-france-a-minsk/rendez-vous?name=R%C3%A9ception%20des%20demandes"
            "%20de%20visa")
        driver.save_screenshot(f'WARNING!!!!!{count}.png')

    send_to_telegram_log(count)
    count = count + 1
