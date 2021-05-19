import pytest
import settings
import requests
from client.client import Client


class TestBase:
    url = None
    client = None

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'
        self.client = Client(settings.MOCK_HOST, settings.MOCK_PORT)
        self.prepare()


class TestMock(TestBase):
    def test_mock(self):
        post_param = '/create_surname'
        request1 = f'POST {post_param} HTTP/1.1\r\n' \
                   f'Host: {settings.MOCK_HOST}:{settings.MOCK_PORT}\r\n' \
                   f'Content-Type: application/x-www-form-urlencoded\r\n' \
                   f'Content-Length: {str(len("TEST"))}\r\n\r\n' \
                   f'TEST\r\n'

        get_param = '/get_surname/TEST'
        request2 = f'GET {get_param} HTTP/1.1\r\nHost:{settings.MOCK_HOST}\r\n\r\n'

        self.client.method_post(request1.encode())
        self.client.method_post(request2.encode())

        result = self.client.method_get()
        print('#->> ', result)
