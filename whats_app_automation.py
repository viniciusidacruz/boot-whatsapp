from time import sleep

from pyperclip import copy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

keyboard_button_enter = Keys.ENTER;

def search_contact(browser: WebDriver):
    search_icon_whatsApp = browser.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span')
    search_icon_whatsApp.click()
    sleep(2)
    
    field_search_input = browser.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
    field_search_input.send_keys("Vinicius Italo da Cruz")
    field_search_input.send_keys(Keys.ENTER)
    sleep(2)

def send_message(browser: WebDriver, message: str):
    copy(message)
    combination_past_message = Keys.CONTROL + "v"
    sleep(2)
    
    field_message_text_area = browser.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
    field_message_text_area.send_keys(combination_past_message)
    field_message_text_area.send_keys(Keys.ENTER)
    sleep(2)