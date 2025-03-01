import time

from Configs import seleniumConfig
from TestUtils import Utils

configName = seleniumConfig.set_config(".env")

class AddUser:
    def __init__(self):
        self.admin_btn = (configName.By.XPATH, "//span[contains(.,'Admin')]")
        self.admin = (configName.By.XPATH, "//h6[contains(.,'Admin')]")
        self.add_btn = (configName.By.XPATH, "//button[contains(.,' Add')]")
        self.form = (configName.By.XPATH, "//h6[contains(.,'Add User')]")
        self.user_role_select = (configName.By.XPATH, "//div[2]/i")
        self.admin_role_select = (configName.By.XPATH, "//div[2]/div/div[2]/div[2]")
        self.ess_role_select = (configName.By.XPATH, "//div[2]/div/div[2]/div[3]")
        self.status_select = (configName.By.XPATH, "//div[3]/div/div[2]/div/div/div[2]/i")
        self.enable_status_select = (configName.By.XPATH, "//div[2]/div/div[2]/div[2]")
        self.disable_status_select = (configName.By.XPATH, "//div[2]/div/div[2]/div[3]")
        self.employee_name_input = (configName.By.XPATH, "//div/div[2]/div/div/input")
        self.employee_name_btn = (configName.By.XPATH, "//div[2]/div/div[2]/div/div[2]/div")
        self.username_input = (configName.By.XPATH, "//div[2]/input")
        self.password_input = (configName.By.XPATH, "//div[2]/div/div/div/div[2]/input")
        self.confirm_password_input = (configName.By.XPATH, "//div[2]/div/div[2]/input")
        self.save_btn = (configName.By.XPATH, "//button[contains(.,'Save')]")
        self.save_message = (configName.By.XPATH, "//p[contains(.,'Successfully Saved')]")

    def click_admin(self):
        admin_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.admin_btn))
        Utils.highLight(admin_element)
        admin_element.click()

    def check_admin(self, admin_title):
        configName.WebDriverWait(configName.driver, 30).until(configName.EC.text_to_be_present_in_element(self.admin, admin_title))
        title_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.admin))
        Utils.highLight(title_element)

    def click_add(self):
        add_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.add_btn))
        Utils.highLight(add_element)
        add_element.click()

    def check_form(self, form_title):
        configName.WebDriverWait(configName.driver, 30).until(configName.EC.text_to_be_present_in_element(self.form, form_title))
        title_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.form))
        Utils.highLight(title_element)

    def select_user_role(self, role):
        select_user_role_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.user_role_select))
        Utils.highLight(select_user_role_element)
        if role == "admin":
            select_user_role_element.click()
            select_admin_role_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.admin_role_select))
            Utils.highLight(select_admin_role_element)
            select_admin_role_element.click()
        elif role == "ess":
            select_user_role_element.click()
            select_ess_role_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.ess_role_select))
            Utils.highLight(select_ess_role_element)
            select_ess_role_element.click()
        else:
            print("Role not defined")

    def select_status(self, status):
        select_status_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.status_select))
        Utils.highLight(select_status_element)
        if status == "enable":
            select_status_element.click()
            select_enable_status_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.enable_status_select))
            Utils.highLight(select_enable_status_element)
            select_enable_status_element.click()
        elif status == "disable":
            select_status_element.click()
            select_disable_status_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.disable_status_select))
            Utils.highLight(select_disable_status_element)
            select_disable_status_element.click()
        else:
            print("Status not defined")

    def enter_employee_name(self, employee_name):
        employee_name_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.employee_name_input))
        Utils.highLight(employee_name_element)
        employee_name_element.clear()
        employee_name_element.send_keys(employee_name)

    def click_employee_name(self, employee_name):
        configName.WebDriverWait(configName.driver, 30).until(configName.EC.text_to_be_present_in_element(self.employee_name_btn, employee_name))
        employee_name_btn_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.employee_name_btn))
        Utils.highLight(employee_name_btn_element)
        employee_name_btn_element.click()

    def enter_username(self, username):
        username_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.username_input))
        Utils.highLight(username_element)
        username_element.clear()
        username_element.send_keys(username)

    def enter_password(self, password):
        password_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.password_input))
        Utils.highLight(password_element)
        password_element.clear()
        password_element.send_keys(password)

    def enter_confirm_password(self, confirm_password):
        confirm_password_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.confirm_password_input))
        Utils.highLight(confirm_password_element)
        confirm_password_element.clear()
        confirm_password_element.send_keys(confirm_password)

    def click_save(self):
        save_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.save_btn))
        Utils.highLight(save_element)
        save_element.click()

    def check_save(self, save_message):
        configName.WebDriverWait(configName.driver, 30).until(configName.EC.text_to_be_present_in_element(self.save_message, save_message))
        save_message_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.save_message))
        Utils.highLight(save_message_element)