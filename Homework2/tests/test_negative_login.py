import pytest
import allure

from tests.base import BaseCase


@pytest.mark.UI
class TestNegativeLogin(BaseCase):
    authorize = False

    @allure.feature("UI Test")
    @allure.description("""
    1. going to target.com
    2. trying to authorize with invalid data
    3. check for the negative results
    """)
    @pytest.mark.parametrize(
        "login,password",
        [
            ("test@gmail.com", "123123123"),
            ("alexandrhering@gmail.com", "1")
        ]
    )
    def test_negative_login_wrong_email(self, login, password):
        with pytest.raises(TimeoutError):
            self.login_page.login(
                login=login,
                password=password
            )
            # self.logger.info("# Results checking...")
        assert self.login_page.negitive_check() is True
        # self.logger.info("# all went according plan...")
