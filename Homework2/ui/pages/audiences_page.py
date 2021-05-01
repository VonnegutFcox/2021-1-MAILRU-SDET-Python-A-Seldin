from selenium.common.exceptions import NoSuchElementException, WebDriverException

from ui.pages.base_page import BasePage
from ui.locators.pages_locators import AudiencesPageLocators
from selenium.webdriver.common.by import By


class AudiencesPage(BasePage):
    url = 'https://target.my.com/segments/segments_list'
    locators = AudiencesPageLocators()

    def segment_create(self, segment_name):
        try:
            self.click(self.locators.CREATE_AUDIENCES)
        except WebDriverException:
            self.click(self.locators.BUTTON_CREATE_AUDIENCES)

        self.click(self.locators.ADDINDG_SEGMENTS_checkbox)
        self.click(self.locators.BUTTON_ADD_SEGMENT)
        segment = self.input_textarea(self.locators.SEGMENT_NAME,
                                      query=str(segment_name))
        self.click(self.locators.BUTTON_CREATE_AUDIENCES)
        self.wait()
        segment_check = self.find((By.XPATH,
                                   f'//a[@title="{segment_name}"]'))
        print(segment_name, segment_check.get_attribute('text'))
        return [
            str(segment_name),
            str(segment_check.get_attribute('text'))
        ]

    def segment_delete(self, segment):
        if self.check_exists((By.XPATH,
                              f'//a[@title="{segment}"]/../../following-sibling::div/span')):
            self.click((By.XPATH,
                        f'//a[@title="{segment}"]/../../following-sibling::div/span'))
            self.wait(2)
            self.click(self.locators.BUTTON_SEGMENT_DELETE)
            return True
        else:
            return False
