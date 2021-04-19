import pytest


@pytest.mark.API
class TestApi:

    def test_valid_login(self, api_client, credentials):
        result = api_client.post_login(*credentials)
        assert result.status_code == 200

    def test_create_segment(self, api_client, credentials):
        result = api_client.post_login(*credentials)
        segment = api_client.create_segment('TEST')
        assert isinstance(segment['id'], int)

    def test_delete_segment(self, api_client, credentials):
        result = api_client.post_login(*credentials)
        segment = api_client.create_segment('TEST')
        if isinstance(segment['id'], int):
            segment = api_client.delete_segment(segment['id'])
            assert segment.status_code == 204
