import pytest
from base import BaseCase
from Homework1.ui.locators import basic_locators as bl


class TestFour(BaseCase):

    TESTDATA = [
        (bl.STATISTICS_LINK_LOCATOR, "statistics/summary"),
        (bl.TOOLS_LINK_LOCATOR, "tools/feeds"),
    ]

    @pytest.mark.UI
    @pytest.mark.parametrize("locator,url", TESTDATA)
    def test_page_navigation(self, locator, url):
        self.login()
        self.click(locator)
        self.wait()
        assert self.driver.current_url == f"https://target.my.com/{url}"
