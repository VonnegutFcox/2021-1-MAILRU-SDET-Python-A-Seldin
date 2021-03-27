import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--url',
                     default='https://target.my.com/')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",
                                    ["enable-logging"])
    return {'url': url, 'options': options}


@pytest.fixture(scope='function', autouse=True)
def driver(config):
    browser = webdriver.Chrome(options=config['options'],
                               executable_path="chromedriver.exe")
    browser.set_window_size(1400, 1000)
    url = config['url']
    browser.get(url)
    yield browser
    browser.close()
