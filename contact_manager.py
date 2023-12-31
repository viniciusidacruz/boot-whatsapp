from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

def send_message_for_contacts(browser: WebDriver, message_whatsApp: str):
    contact_list = ["Metas 2023", "Amiguinhos de algodão", "Família Cruz"];
    qty_of_contacts_in_list = len(contact_list);

    if qty_of_contacts_in_list % 5 == 0:
        qty_of_blocks = qty_of_contacts_in_list / 5;
    else:
        qty_of_blocks = int(qty_of_contacts_in_list / 5) + 1;

    for i in range(qty_of_blocks):
        i_start = i * 5;
        i_end = (i + 1) * 5;
        
        send_list = contact_list[i_start:i_end];
        
        messages_list = browser.find_elements('class name', '_1uv-a');

        for message_in_list in messages_list:
            message_whatsApp = message_whatsApp.replace("\n", "");
            text = message_in_list.text.replace("\n", "");
            
            if message_whatsApp in text:
                currentMessage = message_in_list;
                break;
        
        ActionChains(browser).move_to_element(currentMessage).perform();

        sleep(2);

        arrow_down_icon = currentMessage.find_element('class name', '_3u9t-');
        arrow_down_icon.click();

        sleep(2);

        forward_button = browser.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[4]');
        forward_button.click();

        sleep(2);

        forward_icon_arrow = browser.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]');
        forward_icon_arrow.click();

        sleep(2);
        
        for name in send_list:
            field_search_forward_input = browser.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p');
            field_search_forward_input.send_keys(name);
            sleep(1);
            
            field_search_forward_input.send_keys(Keys.ENTER);
            sleep(1);
            
            field_search_forward_input.send_keys(Keys.BACKSPACE);
            sleep(1);
            
        send_message_button = browser.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div');
        send_message_button.click();
        sleep(3)
