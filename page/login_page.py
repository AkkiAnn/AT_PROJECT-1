from selenium.webdriver.common.by import By
from locators.OrangeHRM import OHRM_Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:

    def __init__(self, driver):
        self.driver = driver

    # Login operation with Username and Password.
    def login(self, username, password):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, OHRM_Data.username_login_n)).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, OHRM_Data.password_login_n)).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, OHRM_Data.login_btn_lt)).click()

        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert.accept()  # Accept the alert
        except Exception as e:
            print(" Error in login ", e)
