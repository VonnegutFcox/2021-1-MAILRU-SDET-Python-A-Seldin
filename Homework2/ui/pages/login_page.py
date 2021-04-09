from ui.pages.base_page import BasePage
from ui.locators.pages_locators import LoginPageLocators
from ui.pages.dashboard_page import DashboardPage


class LoginPage(BasePage):
    locators = LoginPageLocators()
    LOGIN = "alexandrhering@gmail.com"
    PASSWORD = "S4f-aUv-7bB-Tws"

    def login(self, login=LOGIN, password=PASSWORD):
        self.click(locator=self.locators.ENTER_LOCATOR)
        self.find(locator=self.locators.INPUT_MAIL_LOCATOR,
                  timeout=1).send_keys(login)
        self.find(locator=self.locators.INPUT_PASSWORD_LOCATOR,
                  timeout=1).send_keys(password)
        self.click(locator=self.locators.ENTER_REG_LOCATOR,
                   timeout=1)
        return DashboardPage(self.driver)

    def negitive_check(self):
        try:
            error = self.check_exists(self.locators.ERROR_MESSAGE)
            return error
        except AssertionError:
            error = self.check_exists(self.locators.ERROR_MESSAGE1)
            return error
