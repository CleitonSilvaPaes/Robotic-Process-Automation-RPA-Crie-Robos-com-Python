import pyautogui as p

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("--disable-notifications")
option.add_argument('--disable-infobars')
option.add_argument('--start-maximized')
option.add_argument('--disable-popup-blocking')

prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "download.default_directory": "download_directory",
    "download.prompt_for_download": True,
    "plugins.always_open_pdf_externally": True
    }
option.add_experimental_option("prefs", prefs)
option.add_experimental_option('excludeSwitches', ['enable-logging'])

web = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option) # noqa
web.execute_script('window.alert = null;')
web.execute_script('Window.prototype.alert = null;')
web.execute_script('window.onbeforeunload = null;')


p.sleep(2)
web.get('https://busca.inpi.gov.br/pePI/servlet/LoginController?action=login')
web.find_element(By.XPATH, '//*[@id="Map3"]/area[2]').click()
p.sleep(5)
web.find_element(By.XPATH, '//*[@id="principal"]/table[2]/tbody/tr[7]/td[2]/font[1]/input').send_keys('03768202000176') # noqa
web.find_element(By.XPATH, '//*[@id="principal"]/table[2]/tbody/tr[7]/td[2]/select[2]/option[4]').click() # noqa
web.find_element(By.XPATH, '//*[@id="principal"]/table[2]/tbody/tr[10]/td/font/input[1]').click() # noqa
p.sleep(15)
web.quit()