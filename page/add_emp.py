from selenium import webdriver
from selenium.webdriver.common.by import By
from confi.config import Acts
from locators.OrangeHRM import OHRM_Data
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import os

class Add_employe:

    def __init__(self, driver):
        super().__int__(driver)
        self.driver = driver

# Click PIM Module in Left side Menu.
    def click_pim(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, OHRM_Data.pim_menubutton_lt )).click()

# Click Add button after clicking PIM Module.
    def click_ad_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, OHRM_Data.pim_addbutton_lt )).click()

# Click Add profile
    def ad_profile_snap(self, img_path):
        click_add= WebDriverWait(self.driver, 15).until( EC.presence_of_element_located(By.XPATH, OHRM_Data.add_profile_pic_x)).click()
        click_add.send_keys(os.path.abspath(img_path))
        driver.implicitly_wait(10)

    def add_emp(self,fst_name, mid_name, lst_name, empl_id, other_id, driving_no, lic_exp_dt, d_o_b, gender, Test_field):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, OHRM_Data.add_fname_n )).send_keys(fst_name)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, OHRM_Data.add_mname_n )) .send_keys(mid_name)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, OHRM_Data.add_lname_n )).send_keys(lst_name)

        emp_id = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, OHRM_Data.em_id_x ))
        emp_id.clear()
        emp_id.send_keys(empl_id)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, OHRM_Data.save_button_a_lt )).click()
        driver.implicitly_wait(30)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, OHRM_Data.other_id_x )).send_keys(other_id)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH,OHRM_Data.drive_lic_no_x )).send_keys(driving_no)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, OHRM_Data.calender_licnese_x )).send_keys(lic_exp_dt)

        nationality = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, OHRM_Data.nationality_button_x  )))
        nationality.select_by_visible_text("India")

        marital_sts = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, OHRM_Data.martial_status_x )))
        marital_sts.select_by_visible_text("Single")

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, OHRM_Data.d_o_b_x )).send_keys(d_o_b)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, OHRM_Data.gender_m_lt )).send_keys(gender)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, OHRM_Data.save_button_b_lt )).click()

        blood_type = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, OHRM_Data.blood_x)))
        blood_type.select_by_visible_text("O+")

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, OHRM_Data.test_field_x )).send_keys(Test_field)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, OHRM_Data.save_button_c_lt )).click()

        driver.implicitly_wait(20)



