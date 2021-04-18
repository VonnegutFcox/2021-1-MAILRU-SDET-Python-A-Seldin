import os

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage
from ui.locators.pages_locators import CampaignPageLocator


class CampaignPage(BasePage):

    url = 'https://target.my.com/dashboard'
    locators = CampaignPageLocator()

    def create_the_campaign(self, campaign_name):
        try:
            self.click(self.locators.CREATE_CAMPAIGN)
        except TimeoutException:
            self.click(self.locators.CREATE_CAMPAIGN1)

        self.click(self.locators.STORE_OBJECTIVE)
        self.input_textarea(self.locators.INPUT_LINK, query='https://test.com')
        self.wait()

        name = self.find(self.locators.INPUT_NAME)
        self.click(self.locators.CLEAR_FIELD)
        name.send_keys(campaign_name)

        self.scroll_to(self.locators.TOTAL_BUDGET)
        self.input_textarea(self.locators.DAILY_BUDGET, '100')
        self.input_textarea(self.locators.TOTAL_BUDGET, '600')

        self.scroll_to(self.locators.MULTIFORMAT)
        self.click(self.locators.MULTIFORMAT)
        self.wait()

        self.scroll_to(self.locators.TITLE_INPUT)
        self.click(self.locators.PATTERN_TAB)
        self.find(self.locators.IMG1).send_keys(os.getcwd()+"/img/icon_1080_607.jpg")
        self.input_textarea(self.locators.TITLE_INPUT, 'test title')
        self.click(self.locators.BUTTON_SAVE_AD)

        self.wait()
        self.click(self.locators.BUTTON_CREATE_CAMPAIGN)
        self.wait(10)
        name = name.get_attribute("value")
        if self.check_exists((By.XPATH, f'//a[@title="{name}"]')):
            return True
        else:
            return False
