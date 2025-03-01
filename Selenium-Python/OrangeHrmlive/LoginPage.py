from Configs import seleniumConfig
from TestUtils import Utils

configName = seleniumConfig.set_config(".env")

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.title = (configName.By.XPATH, "//h5[contains(.,'Login')]")
        self.username_input = (configName.By.NAME, "username")
        self.password_input = (configName.By.NAME, "password")
        self.login_btn = (configName.By.XPATH, "//button[contains(.,'Login')]")
        self.dashboard = (configName.By.XPATH, "//h6[contains(.,'Dashboard')]")

    def get_url(self, url):
        self.driver.get(url)

    def check_title(self, title):
        configName.WebDriverWait(self.driver, 30).until(configName.EC.text_to_be_present_in_element(self.title, title))
        title_element = configName.WebDriverWait(self.driver, 30).until(configName.EC.presence_of_element_located(self.title))
        Utils.highLight(title_element)

    def enter_username(self, username):
        username_element = configName.WebDriverWait(self.driver, 30).until(configName.EC.presence_of_element_located(self.username_input))
        Utils.highLight(username_element)
        username_element.clear()
        username_element.send_keys(username)

    def enter_password(self, password):
        password_element = configName.WebDriverWait(self.driver, 30).until(configName.EC.presence_of_element_located(self.password_input))
        Utils.highLight(password_element)
        password_element.clear()
        password_element.send_keys(password)

    def click_login(self):
        login_element = configName.WebDriverWait(self.driver, 30).until(configName.EC.presence_of_element_located(self.login_btn))
        Utils.highLight(login_element)
        login_element.click()

    def check_login(self, dashboard_title):
        configName.WebDriverWait(self.driver, 30).until(configName.EC.text_to_be_present_in_element(self.dashboard, dashboard_title))
        dashboard_element = configName.WebDriverWait(self.driver, 30).until(configName.EC.presence_of_element_located(self.dashboard))
        Utils.highLight(dashboard_element)