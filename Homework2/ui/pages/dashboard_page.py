from ui.pages.base_page import BasePage
from ui.pages.audiences_page import AudiencesPage
from ui.locators.pages_locators import DashboardPageLocators
from ui.pages.campaign_page import CampaignPage


class DashboardPage(BasePage):

    url = 'https://target.my.com/dashboard'
    locators = DashboardPageLocators()

    def go_to_segment(self):
        self.click(self.locators.AUDIENCES_LOCATOR)
        return AudiencesPage(self.driver)

    def go_to_campaign(self):
        self.click(self.locators.CAMPAIGN_LOCATOR)
        return CampaignPage(self.driver)
