import allure
import pytest

from tests.base import BaseCase
from ui.fixtures import audiences_page


@pytest.mark.UI
class TestAudiences(BaseCase):

    @allure.feature("UI Test")
    @allure.description(
        """
        1. create a segment
        2. remember the segment name
        3. find the name of this segment in the created table
        4. and then delete it
        """
    )
    def test_audiences(self, audiences_page):
        segment, segment_check = audiences_page.segment_create()
        # self.logger.info("# Results checking...")
        assert segment == segment_check
        # self.logger.info("# all went according plan...")
        # self.logger.info("# Results checking...")
        delete = audiences_page.segment_delete(segment_check)
        assert delete is True
        # self.logger.info("# all went according plan...")

    @allure.feature("UI Test")
    @allure.description(
        """
        1. create a segment
        2. remember the segment name
        3. find the name of this segment in the created table
        4. and then delete it
        5. check if the table is cleared
        """
    )
    def test_audiences_delete(self, audiences_page):
        segment, segment_check = audiences_page.segment_create()
        delete = audiences_page.segment_delete(segment_check)
        # self.logger.info("# Results checking...")
        assert delete is True
        # self.logger.info("# all went according plan...")
