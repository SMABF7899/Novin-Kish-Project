from Configs import seleniumConfig
from TestUtils import Utils

configName = seleniumConfig.set_config(".env")

class ValidateUser:
    def __init__(self):
        self.system_user_title = (configName.By.XPATH, "//h5[contains(.,'System Users')]")
        self.username_input = (configName.By.XPATH, "//div[2]/input")
        self.search_btn = (configName.By.XPATH, "//button[contains(.,'Search')]")
        self.username = (configName.By.XPATH, "//div[2]/div[3]/div/div[2]/div/div/div[2]/div")
        self.user_role = (configName.By.XPATH, "//div[3]/div/div[2]/div/div/div[3]/div")
        self.employee_name = (configName.By.XPATH, "//div[2]/div/div/div[4]/div")
        self.status = (configName.By.XPATH, "//div[2]/div/div/div[5]/div")
        self.reset_btn = (configName.By.XPATH, "//button[contains(.,'Reset')]")

    def check_system_user(self, title):
        configName.WebDriverWait(configName.driver, 30).until(configName.EC.text_to_be_present_in_element(self.system_user_title, title))
        title_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.system_user_title))
        Utils.highLight(title_element)

    def enter_username(self, username):
        username_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.username_input))
        Utils.highLight(username_element)
        username_element.clear()
        username_element.send_keys(username)

    def click_search(self):
        search_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.search_btn))
        Utils.highLight(search_element)
        search_element.click()

    def check_username(self, username):
        configName.WebDriverWait(configName.driver, 30).until(configName.EC.text_to_be_present_in_element(self.username, username))
        username_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.username))
        Utils.highLight(username_element)

    def check_user_role(self, role):
        configName.WebDriverWait(configName.driver, 30).until(configName.EC.text_to_be_present_in_element(self.user_role, role))
        user_role_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.user_role))
        Utils.highLight(user_role_element)

    def check_employee_name(self, employee_name):
        configName.WebDriverWait(configName.driver, 30).until(configName.EC.text_to_be_present_in_element(self.employee_name, employee_name))
        employee_name_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.employee_name))
        Utils.highLight(employee_name_element)

    def check_status(self, status):
        configName.WebDriverWait(configName.driver, 30).until(configName.EC.text_to_be_present_in_element(self.status, status))
        status_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.status))
        Utils.highLight(status_element)

    def click_reset(self):
        reset_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.reset_btn))
        Utils.highLight(reset_element)
        reset_element.click()