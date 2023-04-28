import threading
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By


def run_selenium():
    useragent = UserAgent()

    optinos = webdriver.ChromeOptions()
    optinos.add_argument(f'user-agent={useragent.random}')

    url = 'https://www.pari.ru/'
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                   options=optinos)

    browser.get(url=url)
    time.sleep(5)

    vhod_button = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/header/div[2]/div/div[4]/div/a[1]').click()
    time.sleep(3)

    browser.quit()