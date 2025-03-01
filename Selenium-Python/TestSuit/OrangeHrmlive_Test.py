from OrangeHrmlive.LoginPage import LoginPage
from OrangeHrmlive.AddUser import AddUser
from OrangeHrmlive.ValidateUser import ValidateUser
from OrangeHrmlive.LogoutPage import LogoutPage
from Configs import seleniumConfig

configName = seleniumConfig.set_config(".env")
class OrangeHrmLive:
    def __init__(self):
        df = configName.pd.read_excel("TestUtils/Users.xlsx")
        self.users_list = [row.tolist() for index, row in df.iterrows()]

    def login(self):
        loginPage = LoginPage()
        loginPage.get_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        loginPage.check_title("Login")
        loginPage.enter_username("Admin")
        loginPage.enter_password("admin123")
        loginPage.click_login()
        loginPage.check_login("Dashboard")

    def addUserOne(self):
        addUser = AddUser()
        addUser.click_admin()
        addUser.check_admin("Admin")
        addUser.click_add()
        addUser.check_form("Add User")
        addUser.select_user_role(self.users_list[0][3])
        addUser.select_status(self.users_list[0][4])
        addUser.enter_employee_name(self.users_list[0][0])
        addUser.click_employee_name(self.users_list[0][0])
        addUser.enter_username(self.users_list[0][1])
        addUser.enter_password(self.users_list[0][2])
        addUser.enter_confirm_password(self.users_list[0][2])
        addUser.click_save()
        addUser.check_save("Successfully Saved")

    def addUserTwo(self):
        addUser = AddUser()
        addUser.click_admin()
        addUser.check_admin("Admin")
        addUser.click_add()
        addUser.check_form("Add User")
        addUser.select_user_role(self.users_list[1][3])
        addUser.select_status(self.users_list[1][4])
        addUser.enter_employee_name(self.users_list[1][0])
        addUser.click_employee_name(self.users_list[1][0])
        addUser.enter_username(self.users_list[1][1])
        addUser.enter_password(self.users_list[1][2])
        addUser.enter_confirm_password(self.users_list[1][2])
        addUser.click_save()
        addUser.check_save("Successfully Saved")

    def validateUserOne(self):
        validateUser = ValidateUser()
        validateUser.check_system_user("System Users")
        validateUser.enter_username(self.users_list[0][1])
        validateUser.click_search()
        validateUser.check_username(self.users_list[0][1])
        validateUser.check_user_role(self.users_list[0][3])
        validateUser.check_employee_name(self.users_list[0][0])
        validateUser.check_status(self.users_list[0][4])
        validateUser.click_reset()

    def validateUserTwo(self):
        validateUser = ValidateUser()
        validateUser.check_system_user("System Users")
        validateUser.enter_username(self.users_list[1][1])
        validateUser.click_search()
        validateUser.check_username(self.users_list[1][1])
        validateUser.check_user_role(self.users_list[1][3])
        validateUser.check_employee_name(self.users_list[1][0])
        validateUser.check_status(self.users_list[1][4])
        validateUser.click_reset()

    def logout(self):
        logoutPage = LogoutPage()
        logoutPage.check_admin_title("manda user")
        logoutPage.click_profile()
        logoutPage.click_logout()
        logoutPage.check_logout("Login")