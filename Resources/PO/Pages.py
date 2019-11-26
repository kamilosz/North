
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from Resources.Locators import Locators
from Resources.TestData import TestData


class BasePage(object):
    """Base class for every page"""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver

    # This functions checks if web element is selected
    def is_selected(self, by_locator, state):
        return WebDriverWait(self.driver, 10).until(EC.element_located_selection_state_to_be(by_locator, state))

    # This function checks if current URL is that expected
    def is_url_matches(self, url_text):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url_text))

    # This function checks if provided text appears in page title
    def is_title_matches(self, title):
        return WebDriverWait(self.driver, 10).until(EC.title_is(title))

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # this function asserts comparison of a web element's contains text with passed in text.
    def get_element_text_content(self, by_locator):
        try:
            web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        except NoSuchElementException:
            return False
        return web_element.get_attribute("textContent")

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value(by_locator, element_text))

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function reads value of web element .
    def get_value_of_element(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        except NoSuchElementException:
            return False
        return element.get_attribute("value")

    # this function reads value of dropdown list's selection .
    def get_value_of_list_selection(self, by_locator):
        try:
            select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)))
        except NoSuchElementException:
            return False
        return select.first_selected_option.get_attribute("value")

    # this function performs a select from the list of the passed in position name,
    # in a web element whose locator is passed to it.
    def select_from_list(self, by_locator, position_value):
        try:
            return Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))) \
                .select_by_value(position_value)
        except NoSuchElementException:
            return False

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # boolean value.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its invisibility.
    def is_not_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        return bool(element)

    # this function check the validation error message visibility
    def validation_err_msg(self, by_locator, state):
        try:
            element = self.driver.find_element(*by_locator)
        except NoSuchElementException:
            return False
        if not state and (element.get_attribute("style") == "visibility: hidden;"):
            return True
        elif state and (element.get_attribute("style") == "visibility: visible;"):
            return True
        else:
            return False

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    # This function checks if Northmill`s logo appears on page
    def is_logo_exists(self):
        try:
            self.driver.find_element(*Locators.LOGO)
        except NoSuchElementException:
            return False
        image = self.driver.find_element(*Locators.LOGO)
        image_src = image.get_attribute("src")
        return "data:image/png;base64" in image_src


class MainPage(BasePage):
    """Recruitment Home Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def form_enter_name(self, test_data):
        self.enter_text(Locators.NAME_INPUT, test_data)

    def form_enter_email(self, test_data):
        self.enter_text(Locators.EMAIL_INPUT, test_data)

    def form_enter_experience(self, test_data):
        self.enter_text(Locators.EXPERIENCE_INPUT, test_data)

    def list_select_position(self, test_data):
        self.select_from_list(Locators.POSITION_SELECT, test_data)

    def form_enter_about(self, test_data):
        self.enter_text(Locators.ABOUT_YOU_AREA, test_data)

    def hit_submit(self):
        self.click(Locators.SUBMIT_BUTTON)

    def hit_clear(self):
        self.click(Locators.CLEAR_BUTTON)

    def hit_terms_checkbox(self):
        self.click(Locators.TERMS_CHECKBOX)

    def hit_terms_link(self):
        self.click(Locators.TERMS_LINK)

