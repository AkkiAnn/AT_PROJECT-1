class OHRM_Data:

# Login window locators
    username_login_n="username"
    password_login_n="password"
    login_btn_lt=" Login "
    forgot_pass_lt="Forgot your password? "

# PIM Menu locators
    pim_menubutton_lt ="PIM"
    pim_addbutton_lt =" Add "
    add_fname_n = "firstName"
    add_mname_n ="middleName"
    add_lname_n ="lastName"
    em_id_x='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    save_button_a_lt=" Save "

# After entering the Personal Details page
    other_id_x = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    drive_lic_no_x='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    calender_licnese_x = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    nationality_button_x = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
    martial_status_x = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
    d_o_b_x = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
    gender_m_lt = "Male"
    gender_n_lt = "Female"
    save_button_b_lt=" Save "
    blood_x= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
    test_field_x= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[2]/div/div[2]/input'
    save_button_c_lt=" Save "

# PIM Module Locators for Search option [ Edit and Delete employee]
    search_emp_id_x= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input'
    search_button_lt=" Search "

    edit_button_x= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]'
    delete_button_x= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]'
    yes_delete_lt= " Yes, Delete "

# Add Profile Picture
    add_profile_pic_x= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button'

# Logout Locators
    kebab_button_logout_x= '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span'
    logout_button_lt="Logout"