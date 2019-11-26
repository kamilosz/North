from selenium.webdriver.common.by import By


class Locators(object):
    """Main Page Locators"""
    SUBMIT_BUTTON = (By.ID, 'formSubmitButton')
    CLEAR_BUTTON = (By.ID, 'formClearButton')
    TERMS_CHECKBOX = (By.ID, 'formTermsAndConditionsCheckbox')
    TERMS_LINK = (By.LINK_TEXT, 'Terms and Conditions')
    TERMS_CONTENT = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/h4')
    TERMS_OK_BUTTON = (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/button')
    LOGO = (By.XPATH, "//*[@id='northmillLogo']/img")

    PAGE_HEADER = (By.XPATH, "//*[@id='root']/div/h1")

    NAME_INPUT = (By.ID, "formNameInput")
    EMAIL_INPUT = (By.ID, 'formEmailInput')
    EXPERIENCE_INPUT = (By.XPATH, '/html/body/div/div/form/div[3]/div/input')
    POSITION_SELECT = (By.ID, 'formRoleSelect')
    ABOUT_YOU_AREA = (By.ID, 'formAboutYouTextArea')

    """An error text elements"""
    NAME_INPUT_ERROR = (By.XPATH, "//*[@id='" + NAME_INPUT[1] + "']/following-sibling::span[""@class='help-block']")
    EMAIL_INPUT_ERROR = (By.XPATH, "//*[@id='" + EMAIL_INPUT[1] + "']/following-sibling::span[""@class='help-block']")
    EXPERIENCE_INPUT_ERROR = (By.XPATH, "" + EXPERIENCE_INPUT[1] + "/following-sibling::span[""@class='help-block']")
    POSITION_SELECT_ERROR = (By.XPATH, "//*[@id='" + POSITION_SELECT[1] + "']/following-sibling::span[""@class='help"
                                                                          "-block']")
    TERMS_CHECKBOX_ERROR = (By.XPATH, '/html/body/div/div/form/div[6]/div/span')
