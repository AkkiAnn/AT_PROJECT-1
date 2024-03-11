from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Emp_add_cls:

    def __init__(self, driver):
        super().__int__(driver)
        self.driver = driver

    # Validate Dashboard page
    def dashb_page(self):
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert.accept()  # Accept the alert
        except Exception as e:
            print("Dashboard page present")

