import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Resources.TestData import TestData
from Resources.Locators import Locators
from Tests import page


# Base Class for the tests
class TestBaseClass(unittest.TestCase):

    def setUp(self):
        self.service = Service(TestData.CHROME_EXECUTABLE_PATH)
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)
        # self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
        # self.driver = webdriver.Firefox("C:/auto/drivers")
        self.driver.maximize_window()

    def tearDown(self):
        # To do the cleanup after test has executed.
        self.driver.close()
        self.driver.quit()


class QARecruitTest(TestBaseClass):

    def setUp(self):
        super().setUp()

    def test_page_TC01_load_home_page(self):
        """
        User is able to open Norhmill's Recruitment Web Page
        """
        self.main_page = page.MainPage(self.driver)
        self.assertTrue(self.main_page.is_title_matches(TestData.HOME_PAGE_TITLE),
                        "Test Failed. It's not correct website")

    def test_page_TC02_check_if_logo_exist_on_home_page(self):
        """
        Check if Norhmill's Logo exists on main Recruitment Web Page
        """
        self.main_page = page.MainPage(self.driver)
        self.assertTrue(self.main_page.is_logo_exists(),
                        "The Logo doesn't exist on website")

    def test_links_TC01_check_northmill_logo_link(self):
        """
        Check if User is able to open Norhmill's Home Site
        """
        self.main_page = page.MainPage(self.driver)
        self.main_page.click(Locators.LOGO)
        self.assertTrue(self.main_page.is_url_matches(TestData.NORTHMILL_WEBPAGE_LINK),
                        "Test Failed. It's not correct website")

    def test_form_TC01_enter_valid_name(self):
        """
        When User types in the Name field his name, and the lenght of it is equal "2",
        then Validation error have Not to be displayed.
        """

        self.main_page = page.MainPage(self.driver)
        self.main_page.form_enter_name(TestData.NAME_INPUT_DATA_VALID_01)
        self.assertTrue(self.main_page.assert_element_text(Locators.NAME_INPUT, TestData.NAME_INPUT_DATA_VALID_01),
                        "Test Failed. The Name is Not entered correctly")
        self.assertTrue(self.main_page.is_not_visible(Locators.NAME_INPUT_ERROR),
                        "Test Failed. The Name Validation Method Fails")

    def test_form_TC04_enter_valid_name(self):
        """
        When User types in the Name field his name, and the lenght of it is more than "2",
        then Validation error have Not to be displayed.
        """
        self.main_page = page.MainPage(self.driver)
        self.main_page.form_enter_name(TestData.NAME_INPUT_DATA_VALID_02)
        self.assertTrue(self.main_page.assert_element_text(Locators.NAME_INPUT, TestData.NAME_INPUT_DATA_VALID_02),
                        "Test Failed. The Name is Not entered correctly")
        self.assertTrue(self.main_page.is_not_visible(Locators.NAME_INPUT_ERROR),
                        "Test Failed. The Name Validation Method Fails")

    def test_form_TC05_enter_invalid_name(self):
        """
        When User types in the Name field his name, and the lenght of it is less than "2",
        then Validation error have Not to be displayed.
        """
        self.main_page = page.MainPage(self.driver)
        self.main_page.form_enter_name(TestData.NAME_INPUT_DATA_INVALID)
        self.assertTrue(self.main_page.assert_element_text(Locators.NAME_INPUT, TestData.NAME_INPUT_DATA_INVALID),
                        "Test Failed. The Name is Not entered correctly")
        self.assertTrue(self.main_page.is_visible(Locators.NAME_INPUT_ERROR),
                        "Test Failed. The Name Validation Method Fails")

    def test_form_TC06_enter_valid_email(self):
        """
        When User types in the Email field his email, and it's ok,
        then Validation error have Not to be displayed.
        """
        self.main_page = page.MainPage(self.driver)
        self.main_page.form_enter_email(TestData.EMAIL_INPUT_DATA_VALID)
        self.assertTrue(self.main_page.assert_element_text(Locators.EMAIL_INPUT, TestData.EMAIL_INPUT_DATA_VALID),
                        "Test Failed. The Email is Not entered correctly")
        self.assertTrue(self.main_page.is_not_visible(Locators.EMAIL_INPUT_ERROR),
                        "Test Failed. The Email Validation Method Fails")

    def test_form_TC07_enter_invalid_email(self):
        """
        When User types in the Email field his email, and it's not ok,
        then Validation error have Not to be displayed.
        """
        self.main_page = page.MainPage(self.driver)
        self.main_page.form_enter_email(TestData.EMAIL_INPUT_DATA_INVALID)
        self.assertTrue(self.main_page.assert_element_text(Locators.EMAIL_INPUT, TestData.EMAIL_INPUT_DATA_INVALID),
                        "Test Failed. The Email is Not entered correctly")
        self.assertTrue(self.main_page.is_visible(Locators.EMAIL_INPUT_ERROR),
                        "Test Failed. The Email Validation Method Fails")

    def test_form_TC08_enter_years_experience_as_number(self):
        """
        When User types in the Experience in Years field the positive number,
        then the Validation Error Text have Not to be displayed at the bottom
        """
        self.main_page = page.MainPage(self.driver)
        self.main_page.form_enter_experience(TestData.EXPERIENCE_INPUT_DATA_VALID)
        self.assertTrue(self.main_page.assert_element_text(Locators.EXPERIENCE_INPUT,
                                                           TestData.EXPERIENCE_INPUT_DATA_VALID),
                        "Test Failed. Experience is Not entered correctly")
        self.assertTrue(self.main_page.is_not_visible(Locators.EXPERIENCE_INPUT_ERROR),
                        "Test Failed. Experience in Years Validation Error")

    def test_form_TC09_enter_years_experience_as_negative_number(self):
        """
        When User types in the Experience in Years field the negative number,
        then the Validation Error Text have Not to be displayed at the bottom
        """
        self.main_page = page.MainPage(self.driver)
        self.main_page.form_enter_experience(TestData.EXPERIENCE_INPUT_DATA_INVALID_01)
        self.assertTrue(self.main_page.assert_element_text(Locators.EXPERIENCE_INPUT,
                                                           TestData.EXPERIENCE_INPUT_DATA_INVALID_01),
                        "Test Failed. Experience is Not entered correctly")
        self.assertTrue(self.main_page.is_visible(Locators.EXPERIENCE_INPUT_ERROR),
                        "Test Failed. Experience in Years Validation Error")

    def test_form_TC10_enter_years_experience_as_letter(self):
        """
        When User types in the Experience in Years field the letter or letters,
        then the Validation Error Text have to be displayed at the bottom
        """
        self.main_page = page.MainPage(self.driver)
        self.main_page.form_enter_experience(TestData.EXPERIENCE_INPUT_DATA_INVALID_02)
        self.assertTrue(self.main_page.assert_element_text(Locators.EXPERIENCE_INPUT,
                                                           TestData.EXPERIENCE_INPUT_DATA_INVALID_02),
                        "Test Failed. Experience is Not entered correctly")
        self.assertTrue(self.main_page.is_visible(Locators.EXPERIENCE_INPUT_ERROR),
                        "Test Failed. Experience in Years Validation Error")

    # def test_form_TC11_select_role_position(self):
    #     main_page = page.MainPage(self.driver)
    #     self.assertTrue(main_page.is_select_valid(),
    #                     "Test Failed. Role Dropdown List Validation Error")

    # def test_checkbox_exist_pass_01(self):
    #     main_page = page.MainPage(self.driver)
    #     self.assertTrue(main_page.checkbox_find_click_and_check('formTermsAndConditionsCheckbox'),
    #                     "Test Failed. Agree checkbox doesn't exist.")

    # def tearDown(self):
    #     self.driver.back()
    #     # print("Navigating back in tearDown method")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #     # print("Browser closed in tearDownClass method")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Julia/Desktop/PycharmProjects/Northmill'
                                                                  '/reports'))
