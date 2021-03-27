import pytest
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.locators import basic_locators


CLICK_RETRY = 3


class BaseCase:
    driver = None
    config = None

    LOGIN = "alexandrhering@gmail.com"
    PASSWORD = "S4f-aUv-7bB-Tws"

    FIO = "Test Test Test"
    PHONE = "81234567890"
    EMAIL = "test@gmail.com"

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(
                    EC.element_to_be_clickable(locator),
                    message=f"Can't click element by locator {locator}")
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def input_field(self, locator, text):
        field = self.find(locator)
        field.clear()
        field.send_keys(text)
        return field

    def login(self):
        self.click(basic_locators.ENTER_LOCATOR)
        self.find(basic_locators.INPUT_MAIL_LOCATOR,
                  timeout=1).send_keys(self.LOGIN)
        self.find(basic_locators.INPUT_PASSWORD_LOCATOR,
                  timeout=1).send_keys(self.PASSWORD)
        self.click(basic_locators.ENTER_REG_LOCATOR,
                   timeout=1)

    def logout(self):
        self.click(basic_locators.PROFILE_LOCATOR)
        logout = self.find(basic_locators.LOGOUT_LOCATOR)
        self.driver.execute_script("arguments[0].click();", logout)

    def profile(self):
        self.click(basic_locators.PROFILE_LINK_LOCATOR)
        fio = self.input_field(
            basic_locators.PROFILE_FIO_LOCATOR, self.FIO)
        phone = self.input_field(
            basic_locators.PROFILE_PHONE_LOCATOR, self.PHONE)
        email = self.input_field(
            basic_locators.PROFILE_MAIL_LOCATOR, self.EMAIL)
        data = {
            'fio': fio.get_attribute('value'),
            'phone': phone.get_attribute('value'),
            'email': email.get_attribute('value')
        }
        self.click(basic_locators.PROFILE_SAVE_LOCATOR)
        self.driver.refresh()
        return data
