import pytest
from base import BaseCase


class TestTwo(BaseCase):

    @pytest.mark.UI
    def test_logout(self):
        self.login()
        self.logout()
        assert self.driver.current_url == \
               "https://target.my.com/"
