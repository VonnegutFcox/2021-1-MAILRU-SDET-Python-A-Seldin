from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class DashboardPageLocators(BasePageLocators):
    AUDIENCES_LOCATOR = (By.XPATH, '//a[@href="/segments"]')
    CAMPAIGN_LOCATOR = (By.XPATH, '//a[@href="/dashboard"]')


class LoginPageLocators(BasePageLocators):
    ENTER_LOCATOR = (By.XPATH, '//div[text()="Войти"]')
    INPUT_MAIL_LOCATOR = (By.NAME, 'email')
    INPUT_PASSWORD_LOCATOR = (By.NAME, 'password')
    ENTER_REG_LOCATOR = (By.XPATH,
                         '//div[contains(@class, "authForm-module-button")]')
    ERROR_MESSAGE = (By.XPATH, '//div[@class="formMsg_title"]')
    ERROR_MESSAGE1 = (By.XPATH, '//div[contains(@class, "error")]')


class AudiencesPageLocators(BasePageLocators):
    CREATE_AUDIENCES = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    BUTTON_CREATE_AUDIENCES = (By.XPATH, '//div[text()="Create segment"]')

    ADDINDG_SEGMENTS_checkbox = (By.XPATH,
                                 '//input[contains(@class, "adding-segments-source__checkbox")]')
    BUTTON_ADD_SEGMENT = (By.XPATH,
                          '//div[text()="Add segment"]')
    SEGMENT_NAME = (By.XPATH,
                    '//input[contains(@class,"input__inp") and contains(@maxlength,"60")]')
    BUTTON_SEGMENT_DELETE = (By.XPATH, '//div[text()="Delete"]')


class CampaignPageLocator(BasePageLocators):
    CREATE_CAMPAIGN = (By.XPATH, '//a[@href="/campaign/new"]')
    CREATE_CAMPAIGN1 = (By.XPATH, '//div[text()="Create campaign"]')
    STORE_OBJECTIVE = (By.XPATH, '//div[contains(@class, "_storevisits")]')
    INPUT_LINK = (By.XPATH, '//input[@placeholder="Enter URL of your business page"]')
    INPUT_NAME = (By.XPATH,
                  '//div[contains(@class,"base-settings__campaign-name-wrap")]'
                  '//input[@class="input__inp js-form-element"]')
    CLEAR_FIELD = (By.XPATH,
                   '//div[contains(@class,"base-settings__campaign-name-wrap")]'
                   '//div[contains(@class,"input__clear ")]')
    DAILY_BUDGET = (By.XPATH, '//input[@data-test="budget-per_day"]')
    TOTAL_BUDGET = (By.XPATH, '//input[@data-test="budget-total"]')
    MULTIFORMAT = (By.XPATH, '//span[text()="Multiformat"]')
    PATTERN_TAB = (By.XPATH, '//div[@data-pattern-id="64"]')
    IMG1 = (By.XPATH, '//input[@data-test="image_1080x607"]')
    TITLE_INPUT = (By.XPATH, '//input[@placeholder="Enter ad title"]')
    TEXT_INPUT = (By.XPATH, '//textarea[@placeholder="Enter ad text"]')
    BUTTON_SAVE_AD = (By.XPATH, '//div[text()="Save ad"]')
    BUTTON_CREATE_CAMPAIGN = (By.XPATH, '//div[text()="Create a campaign"]')

    SETTINGS = (By.XPATH,
                '//div[contains(@class, "settingsCell-module-settingsIcon")]')
    REMOVE = (By.XPATH, '//li[@title="Remove"]')


