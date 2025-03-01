from Configs import seleniumConfig
from TestUtils import Utils

configName = seleniumConfig.set_config(".env")

class LogoutPage:
    def __init__(self):
        self.admin_user_title = (configName.By.XPATH, "//p[contains(.,'manda user')]")
        self.profile_btn = (configName.By.XPATH, "//span[contains(.,'manda user')]")
        self.logout_btn = (configName.By.LINK_TEXT, "Logout")
        self.login_title = (configName.By.XPATH, "//h5[contains(.,'Login')]")

    def check_admin_title(self, admin_title):
        configName.WebDriverWait(configName.driver, 30).until(configName.EC.text_to_be_present_in_element(self.admin_user_title, admin_title))
        admin_user_title_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.admin_user_title))
        Utils.highLight(admin_user_title_element)

    def click_profile(self):
        profile_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.profile_btn))
        Utils.highLight(profile_element)
        profile_element.click()

    def click_logout(self):
        logout_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.logout_btn))
        Utils.highLight(logout_element)
        logout_element.click()

    def check_logout(self, title):
        configName.WebDriverWait(configName.driver, 30).until(configName.EC.text_to_be_present_in_element(self.login_title, title))
        login_title_element = configName.WebDriverWait(configName.driver, 30).until(configName.EC.presence_of_element_located(self.login_title))
        Utils.highLight(login_title_element)