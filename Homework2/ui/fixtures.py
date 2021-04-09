import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ui.pages.audiences_page import AudiencesPage
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
# from ui.pages.search_page import SearchPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def dashboard_page(login_page):
    return login_page.login()


@pytest.fixture
def audiences_page(dashboard_page):
    return dashboard_page.go_to_segment()


@pytest.fixture
def campaign_page(dashboard_page):
    return dashboard_page.go_to_campaign()


@pytest.fixture(scope='function')
def driver(config):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    url = config['url']
    browser.get(url)
    yield browser
    browser.close()
