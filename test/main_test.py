import pytest
from confi.figuration import fetch_data
from page.add import Add_employe
from page.delete_emp import Delete_employe
from page.Edit_emp import Edit_employe
from page.login_page import Login
from utilitee.Exl_Util import EXL

@pytest.mark.usefixtures("setup")
class Test_project1_:

# TestCase Login_01
    def test_login(self):
        username = EXL.readData(xl_file, sheet1, 2, 6)
        password = EXL.readData(xl_file, sheet1, 2, 7)
        l= Login(self.driver)
        after_log= l.login(username, password)
        try:
            after_log.dashb_page().is_displayed()
            assert self.driver.current_url == fetch_data.dashboard_url
        except Exception as e:
            print("An error occurred in Login", e)

# TestCase Login_02
    def test_invalid_login(self):
        username = EXL.readData(xl_file, sheet1, 3, 6)
        password = EXL.readData(xl_file, sheet1, 3, 7)
        l = Login(self.driver)
        after_log = l.login(username, password)
        try:
            after_log.dashb_page().is_displayed()
            assert self.driver.current_url != fetch_data.dashboard_url
        except Exception as e:
            print("An error occurred in Invalid Login", e)

# TestCase PIM_01
    @pytest.mark.parametrize("username, password, first_name, mid_name, last_name, empo_id, others_id, driving_no, lice_ex_dt, dob, gender, test_field",[(EXL.including_data(xl_file, sheet1))])
    def test_add_employee(self, username, password, first_name, mid_name, last_name, empo_id, others_id, driving_no,lice_ex_dt, dob, gender, test_field):
        try:
            l = Login(self.driver)
            l.login(username, password)
            ad_emp = Add_employe(self.driver)

            # Click PIM Menu
            ad_emp.click_pim()

            # Click the Add Button
            ad_emp.click_ad_button()

            # Upload Profile Picture
            ad_emp.ad_profile_snap(fetch_data.img_path)

            # Add Employee Information
            ad_emp.add_emp(first_name, mid_name, last_name, empo_id, others_id, driving_no, lice_ex_dt, dob, gender, test_field)

            ad_emp.click_pim().is_displayed()

            assert self.driver.current_url == fetch_data.pim_url
        except Exception as e:
            print("An error occurred in Adding Employee", e)

# TestCase PIM_02
    @pytest.mark.parametrize("username, password, search_id, last_name, empo_id", [(EXL.editing_datas(xl_file, sheet1))])
    def test_edit_employee(self, username, password, search_id, last_name, empo_id):
        try:
            l = Login(self.driver)
            l.login(username, password)
            edit_emp = Edit_employe(self.driver)

            # Click PIM Menu.
            edit_emp.click_pim()

            # Add the existing Employee Information
            edit_emp.edit_emp(search_id, last_name, empo_id)

            edit_emp.click_pim().is_displayed()

            assert self.driver.current_url == fetch_data.pim_url
        except Exception as e:
            print("An error occurred in Editing Employee", e)


# TestCase PIM_03
    def test_delete_employee(self, username, password):
        try:
            l = Login(self.driver)
            l.login(username, password)
            delt_emp = Delete_employe(self.driver)

            # Click PIM Menu
            delt_emp.click_pim()

            # Delete the existing Employee Information.
            delt_emp.delete_emp()

            delt_emp.click_pim().is_displayed()

            assert self.driver.current_url == fetch_data.pim_url
        except Exception as e:
            print("An error occurred in Deleting employee", e)

