from selenium.webdriver.common.by import By
from locators.OrangeHRM import OHRM_Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Delete_employe:

    def __init__(self, driver):
        super().__int__(driver)
        self.driver = driver

    # Tests Deleting Employee.
    def delete_emp(self, search_id):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, OHRM_Data.search_emp_id_x)).send_keys(search_id)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, OHRM_Data.search_button_lt)).click()
        driver.implicitly_wait(10)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, OHRM_Data.delete_button_x)).click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, OHRM_Data.yes_delete_lt)).click()



