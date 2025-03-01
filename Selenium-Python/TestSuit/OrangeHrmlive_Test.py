from OrangeHrmlive.LoginPage import LoginPage
from Configs import seleniumConfig

configName = seleniumConfig.set_config(".env")
class OrangeHrmLive:
    def login(self):
        loginPage = LoginPage(configName.driver)
        loginPage.get_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        loginPage.check_title("Login")
        loginPage.enter_username("Admin")
        loginPage.enter_password("admin123")
        loginPage.click_login()
        loginPage.check_login("Dashboard")