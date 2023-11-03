from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os

class descargar_IMAE:
    def __init__(self, save_to):
        self.save_to = save_to
        self.driver = None
        self.global_only = None

    def login(self, username, password):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_experimental_option("prefs", {"download.default_directory": self.save_to})
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://sisee.bch.hn/IMAE/Login.aspx')

        username_field = self.driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$UserName')
        password_field = self.driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$Password')
        submit_button = self.driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$LoginButton')

        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_button.click()

    def click_button_and_wait(self, button_locator, wait_time=10):
        time.sleep(2)
        btn = self.driver.find_element(By.NAME, button_locator[0])
        btn.click()
        wait = WebDriverWait(self.driver, wait_time)
        btn_all = wait.until(EC.presence_of_element_located((By.NAME, button_locator[1])))
        btn_all.click()

    def descargar_IMAE_query(self, global_only):
        time.sleep(1)
        self.global_only = global_only
        self.driver.get('https://sisee.bch.hn/IMAE/ReportePublicaciones.aspx')
        button_locators = [('ctl00$ContentPlaceHolder1$BtnAños', 'ctl00$ContentPlaceHolder1$SeleccionardeListaAños$BtnSeleccionarTodo'),
                           ('ctl00$ContentPlaceHolder1$BtnMeses', 'ctl00$ContentPlaceHolder1$SeleccionardeListaMes$BtnSeleccionarTodo'),]
        imae_slct_all = ('ctl00$ContentPlaceHolder1$BtnIMAE', 'ctl00$ContentPlaceHolder1$SeleccionardeListaIMAE$BtnSeleccionarTodo')

        if global_only:
            global_imae = self.driver.find_element(By.XPATH, "//input[@name='ctl00$ContentPlaceHolder1$RadioButtonList1'][@value='4']")
            global_imae.click()
        else:
            button_locators.append(imae_slct_all)

        for button_locator in button_locators:
            self.click_button_and_wait(button_locator)

        time.sleep(1)
        download_btn = self.driver.find_element(By.NAME, 'ctl00$ContentPlaceHolder1$BtnDescargar')
        download_btn.click()
        time.sleep(5)
        self.driver.quit()

    def view_download(self, delete_file):
        if self.global_only:
            f_type = "xls"
        else:
            f_type = 'xlsx'

        file = os.path.join(self.save_to, 'IndiceMensualIMAE.' + f_type)
        data = pd.read_excel(file)
        file_path = file  # Replace with the path to the file you want to delete

        if delete_file:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"{file_path} eliminado.")
            else:
                print(f"{file_path} eliminado.")

        return data
