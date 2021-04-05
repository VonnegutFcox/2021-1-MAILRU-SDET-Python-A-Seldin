import pytest
from base import BaseCase


class TestThree(BaseCase):

    @pytest.mark.UI
    def test_profile(self):
        self.login()
        profile_dict = self.profile()
        assert profile_dict == {
            'fio': self.FIO,
            'phone': self.PHONE,
            'email': self.EMAIL
        }
