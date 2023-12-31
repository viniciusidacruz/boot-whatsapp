from browser_initialization import initialize_browser
from whats_app_automation import search_contact, send_message
from contact_manager import send_message_for_contacts

browser = initialize_browser();

search_contact(browser);

message_whatsApp = """Fala galera!
Mais uma automação Python com WhatsApp feita com sucesso!!!
"""

send_message(browser, message_whatsApp);

send_message_for_contacts(browser, message_whatsApp);

input("Pressione Enter para encerrar o navegador...");