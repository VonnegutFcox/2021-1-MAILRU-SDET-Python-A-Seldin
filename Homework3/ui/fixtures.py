import os

import allure
import pytest

from api.client import ApiClient


class UnsupportedBrowserType(Exception):
    pass


@pytest.fixture(scope='session')
def cookies(credentials, config):
    api_client = ApiClient(config['url'])
    api_client.post_login(*credentials)

    cookies_list = []
    for cookie in api_client.session.cookies:
        cookie_dict = {'domain': cookie.domain, 'name': cookie.name, 'value': cookie.value, 'secure': cookie.secure}
        cookies_list.append(cookie_dict)

    return cookies_list
