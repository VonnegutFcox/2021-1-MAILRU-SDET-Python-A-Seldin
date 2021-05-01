from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from ui.locators.pages_locators import BasePageLocators
from utils.decorators import wait

CLICK_RETRY = 3
BASE_TIMEOUT = 5


class PageNotLoadedException(Exception):
    pass


class BasePage(object):

    url = 'https://target.my.com/'
    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver
        assert self.is_opened()

    def is_opened(self):
        def _check_url():
            if self.driver.current_url != self.url:
                raise PageNotLoadedException(
                    f'{self.url} did not opened in {BASE_TIMEOUT} for {self.__class__.__name__}.\n'
                    f'Current url: {self.driver.current_url}.')
            return True

        return wait(_check_url, error=PageNotLoadedException, check=True, timeout=BASE_TIMEOUT, interval=0.1)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def input_textarea(self, locator, query):
        input_text = self.find(locator)
        input_text.clear()
        input_text.send_keys(query)
        return input_text

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def check_exists(self, locator):
        try:
            self.find(locator)
        except TimeoutException:
            return False
        return True

    def scroll_to(self, locator):
        element = self.find(locator)
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)
