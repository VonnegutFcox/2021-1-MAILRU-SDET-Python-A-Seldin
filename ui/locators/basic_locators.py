from selenium.webdriver.common.by import By

ENTER_LOCATOR = (By.XPATH, '//div[text()="Войти"]')
INPUT_MAIL_LOCATOR = (By.NAME, 'email')
INPUT_PASSWORD_LOCATOR = (By.NAME, 'password')
ENTER_REG_LOCATOR = (By.XPATH,
                     '//div[contains(@class, "authForm-module-button")]')

PROFILE_LOCATOR = (By.XPATH,
                   '//div[contains(@class, "right-module-rightButton")]')

LOGOUT_LOCATOR = (By.XPATH, '//a[@href="/logout"]')

PROFILE_LINK_LOCATOR = (By.XPATH, '//a[@href="/profile"]')

PROFILE_FIO_LOCATOR = (By.XPATH, '//div[@data-name="fio"]//input')
PROFILE_PHONE_LOCATOR = (By.XPATH, '//div[@data-name="phone"]//input')
PROFILE_MAIL_LOCATOR = (By.XPATH, '//div[@data-email-index="0"]//input')

PROFILE_SAVE_LOCATOR = (By.XPATH, '//button')

TOOLS_LINK_LOCATOR = (By.XPATH, '//a[@href="/tools"]')
STATISTICS_LINK_LOCATOR = (By.XPATH, '//a[@href="/statistics"]')
