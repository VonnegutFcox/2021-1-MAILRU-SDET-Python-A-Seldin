import allure
import pytest

from tests.base import BaseCase
from ui.fixtures import campaign_page


@pytest.mark.UI
class TestCampaign(BaseCase):

    @allure.feature("UI Test")
    @allure.description(
        """
        1. go to the /dashboard tab
        2. fill out the form
        3. creating an advertising campaign
        4. check whether the name of the created campaign
         is in the table of existing ones 
        """)
    def test_campaign(self, campaign_page):
        campaign = campaign_page.create_the_campaign()
        # self.logger.info("# Results checking...")
        assert campaign is True
        # self.logger.info("# all went according plan...")
