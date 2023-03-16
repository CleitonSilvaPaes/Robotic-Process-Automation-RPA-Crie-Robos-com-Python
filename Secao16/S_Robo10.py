import pyautogui as p
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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


web.get('https://consultacnpj.com/cnpj/')
cnpjs = ["45997418000153", "72273196001090", "33000167000101"]

for cnpj in cnpjs:
    dado = web.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/input') # noqa
    dado.clear()
    dado.send_keys(cnpj)
    p.sleep(3)
    texto = web.find_element(By.XPATH, '//*[@id="company-data"]')
    with open(f'{cnpj}.csv', 'w', encoding='UTF-8') as csv:
        csv.write(texto.text)
    p.sleep(2)
web.quit()