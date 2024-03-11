from selenium.webdriver.common.by import By
from locators.OrangeHRM import OHRM_Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Edit_employe:

    def __init__(self, driver):
        super().__int__(driver)
        self.driver = driver

    def edit_emp(self, search_id, lst_name, empl_id):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, OHRM_Data.search_emp_id_x)).send_keys(search_id)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, OHRM_Data.search_button_lt)).click()
        driver.implicitly_wait(10)

        l_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, OHRM_Data.add_lname_n))
        l_name.clear()
        l_name.send_keys(lst_name)

        em_id = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, OHRM_Data.em_id_x ))
        em_id.clear()
        em_id.send_keys(empl_id)

        save_btn_b = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT,OHRM_Data.save_button_b_lt ))
        save_btn_b.click()
        driver.implicitly_wait(20)

