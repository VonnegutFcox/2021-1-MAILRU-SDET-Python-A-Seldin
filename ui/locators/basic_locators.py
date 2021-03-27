from selenium.webdriver.common.by import By

ENTER_LOCATOR = (By.XPATH, '//div[text()="Войти"]')
INPUT_MAIL_LOCATOR = (By.NAME, 'email')
INPUT_PASSWORD_LOCATOR = (By.NAME, 'password')
ENTER_REG_LOCATOR = (By.CLASS_NAME, 'authForm-module-button-2G6lZu')

PROFILE_LOCATOR = (By.CLASS_NAME, 'right-module-rightButton-39YRvc')

LOGOUT_LOCATOR = (By.XPATH, '//a[@href="/logout"]')

PROFILE_LINK_LOCATOR = (By.XPATH, '//a[@href="/profile"]')

PROFILE_FIO_LOCATOR = (By.XPATH, '//div[@data-name="fio"]//input')
PROFILE_PHONE_LOCATOR = (By.XPATH, '//div[@data-name="phone"]//input')
PROFILE_MAIL_LOCATOR = (By.XPATH, '//li[4]//input')

PROFILE_SAVE_LOCATOR = (By.XPATH, '//button')

TOOLS_LINK_LOCATOR = (By.XPATH, '//a[@href="/tools"]')
STATISTICS_LINK_LOCATOR = (By.XPATH, '//a[@href="/statistics"]')
