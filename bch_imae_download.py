from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_SISEE(username, password, save_to):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option("prefs", {"download.default_directory": save_to})
    driver = webdriver.Chrome(options=options)
    driver.get('https://sisee.bch.hn/IMAE/Login.aspx')

    username_field = driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$UserName')
    password_field = driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$Password')
    submit_button = driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$LoginButton')

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()
    return driver 

def click_button_and_wait(driver, button_locator, wait_time=10):
    time.sleep(2)
    btn = driver.find_element(By.NAME, button_locator[0])
    btn.click()
    wait = WebDriverWait(driver, wait_time)
    btn_all = wait.until(EC.presence_of_element_located((By.NAME, button_locator[1])))
    btn_all.click()

def downaload_IMAE_query(driver, global_only):
    time.sleep(1)
    driver.get('https://sisee.bch.hn/IMAE/ReportePublicaciones.aspx')

    if global_only:
        global_imae = driver.find_element(By.XPATH, "//input[@name='ctl00$ContentPlaceHolder1$RadioButtonList1'][@value='4']")
        global_imae.click()

    button_locators = [('ctl00$ContentPlaceHolder1$BtnAños','ctl00$ContentPlaceHolder1$SeleccionardeListaAños$BtnSeleccionarTodo'),
                        ('ctl00$ContentPlaceHolder1$BtnMeses', 'ctl00$ContentPlaceHolder1$SeleccionardeListaMes$BtnSeleccionarTodo'),
                        ('ctl00$ContentPlaceHolder1$BtnIMAE', 'ctl00$ContentPlaceHolder1$SeleccionardeListaIMAE$BtnSeleccionarTodo'),
                        ]

    for button_locator in button_locators:
        click_button_and_wait(driver, button_locator)
    
    time.sleep(1)
    download_btn = driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$BtnDescargar')
    download_btn.click()
    time.sleep(5)
