class TestData:
    CHROME_EXECUTABLE_PATH = "C:/auto/drivers/chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "C:/auto/drivers/geckodriver.exe"
    NORTHMILL_WEBPAGE_LINK = 'https://www.northmill.com/'
    BASE_URL = "http://qa-recruitment-form.s3-website-eu-west-1.amazonaws.com"
    HOME_PAGE_TITLE = "Test this form!"
    NAME_INPUT_DATA_VALID_01 = "ab"
    NAME_INPUT_DATA_VALID_02 = "abc"
    NAME_INPUT_DATA_INVALID = "a"
    EMAIL_INPUT_DATA_VALID = "abc@abc.com"
    EMAIL_INPUT_DATA_INVALID = "ABC@"
    EXPERIENCE_INPUT_DATA_VALID = "3"
    EXPERIENCE_INPUT_DATA_INVALID_01 = "-3"
    EXPERIENCE_INPUT_DATA_INVALID_02 = "eee"
