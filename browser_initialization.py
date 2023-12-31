from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def initialize_browser():
    service_browser = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service_browser)
    
    browser.get('https://web.whatsapp.com')
    sleep(20)
    
    return browser