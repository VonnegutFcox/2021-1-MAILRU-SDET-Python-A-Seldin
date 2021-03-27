import pytest
from base import BaseCase


class TestOne(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.login()
        assert self.driver.current_url == \
               "https://target.my.com/dashboard"
