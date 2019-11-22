# from Tests.element import BasePageElement

from Resources.Locators import Locators
from Resources.TestData import TestData
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# class SearchTextElement(BasePageElement):
#     """This class gets the search text from the specified locator"""
#
#     # The locator for search box where search string is entered
#     locator = 'q'
#
# #
class BasePage(object):
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver

    def is_url_matches(self, url_text):
        """Verifies that current URL is that expected """
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url_text))

    def is_title_matches(self, title):
        """Verifies that provided text appears in page title"""
        return WebDriverWait(self.driver, 10).until(EC.title_is(title))

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value(by_locator, element_text))

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_not_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        return bool(element)

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def is_logo_exists(self):
        """Verifies that Northmill logo appears on page"""
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

    """TO DO Check availability by EC of all elements"""

    # # check availbility of these elements
    # def is_name_exists(self):
    #     try:
    #         self.driver.find_element(*Locators.NAME_INPUT)
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # def is_email_exists(self):
    #     try:
    #         self.driver.find_element(*Locators.EMAIL_INPUT)
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # def is_experience_exists(self):
    #     try:
    #         self.driver.find_element(*Locators.EXPERIENCE_INPUT)
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # def is_position_exists(self):
    #     try:
    #         self.driver.find_element(*Locators.POSITION_SELECT)
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # def is_checkbox_exists(self):
    #     try:
    #         self.driver.find_element(*Locators.TERMS_CHECKBOX)
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # def is_submit_button_exists(self):
    #     try:
    #         self.driver.find_element(*Locators.SUBMIT_BUTTON)
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # def is_clear_button_exists(self):
    #     try:
    #         self.driver.find_element(*Locators.CLEAR_BUTTON)
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # # the rest of methods
    #
    # def click_submit_button(self):
    #     """Triggers the search"""
    #     element = self.driver.find_element(*Locators.SUBMIT_BUTTON)
    #     element.click()

    """Check of form validation"""

    def is_name_valid(self, filler):
        name_element = self.driver.find_element(*Locators.NAME_INPUT)
        name_element.clear()
        name_element.send_keys(str(filler))
        name_error_element = self.driver.find_element(Locators.NAME_INPUT_ERROR)
        return name_error_element.get_attribute("style") == "visibility: hidden;"

    def is_email_valid(self, filler):
        email_element = self.driver.find_element(*Locators.EMAIL_INPUT)
        email_element.clear()
        email_element.send_keys(str(filler))
        email_error_element = self.driver.find_element(*Locators.EMAIL_INPUT_ERROR)
        return email_error_element.get_attribute("style") == "visibility: hidden;"

    def is_experience_valid(self, filler):
        experience_element = self.driver.find_element(*Locators.EXPERIENCE_INPUT)
        experience_element.clear()
        experience_element.send_keys(str(filler))
        experience_error_element = self.driver.find_element(*Locators.EXPERIENCE_INPUT_ERROR)
        return experience_error_element.get_attribute("style") == "visibility: hidden;"

    def is_select_valid(self):
        position_select = Select(self.driver.find_element(*Locators.POSITION_SELECT))
        position_select.select_by_index(1)
        position_error_select = self.driver.find_element(*Locators.POSITION_SELECT_ERROR)
        return position_error_select.get_attribute("style") == "visibility: hidden;"

    def is_terms_opening(self):
        self.driver.find_element(*Locators.TERMS_LINK).click()
        terms_dialog_title = self.driver.find_element(*Locators.TERMS_CONTENT)
        return terms_dialog_title.text == "Terms and Conditions"

    def is_checkbox_valid(self):
        self.driver.find_element(*Locators.TERMS_CHECKBOX).click()
        checkbox_error_element = self.driver.find_element(*Locators.TERMS_CHECKBOX_ERROR)
        return checkbox_error_element.get_attribute("style") == "visibility: hidden;"

    def is_text_form_empty(self, name_id):
        element = self.driver.find_element_by_id(name_id)
        return element.get_attribute("value") == ''

    def is_select_empty(self, name_id):
        # try:
        #     select = Select(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
        #         (By.ID, 'data_configuration_edit_data_object_tab_details_lb_use_for_match'))))
        #     return select.first_selected_option.get_attribute("value")
        # except NoSuchElementException, e:
        #     print
        #     "Element not found "
        #     print
        #     e
        element = self.driver.find_element_by_id(name_id)
        return element.get_attribute("value") == ''

    # def is_number_form_empty(self, name_id):
    #     element = self.driver.find_element_by_xpath(("//*[@id='" + name_id + "']/following-sibling::span[@class='help-block']"))
    #     return element.get_attribute("value") == ''

    def text_form_fill_and_check(self, name_id, filler):
        form_element = self.driver.find_element_by_id(name_id)
        form_element.clear()
        form_element.send_keys(str(filler))
        check_form_element = form_element.get_attribute("value")
        error_text_element = self.driver.find_element_by_xpath(("//*[@id='" + name_id + "']/following-sibling::span["
                                                                                        "@class='help-block']"))
        return error_text_element.get_attribute("style") == "visibility: hidden;"

    def checkbox_find_click_and_check(self, name_id):
        form_element = self.driver.find_element_by_id(name_id)
        form_element.click()
        return True
        # else:
        #     return False
        # error_text_element = self.driver.find_element_by_xpath(("//*[@id='" + name_id + "']/following-sibling::span[@class='help-block']"))
        # return error_text_element.get_attribute("style") == "visibility: hidden;"

    def check_req_are_filled_when_submit(self):
        error_text_element = self.driver.find_element_by_xpath(
            ("//*[@id='" + name_id + "']/following-sibling::span[@class='help-block']"))


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
