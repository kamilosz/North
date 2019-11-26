import unittest
from selenium import webdriver
from Resources.Locators import Locators
from Resources.PO import Pages
from Resources.TestData import TestData


# Base Class for the tests
class TestBaseClass(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH, options=chrome_options)
        # browser should be loaded in maximized window
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class QARecruitTest(TestBaseClass):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_01_load_home_page(self):
        """
        1. Open the main page in the web browser.
        2. Check if opened webpage it's a Norhmill's Recruitment Web Page
        """
        self.main_page = Pages.MainPage(self.driver)
        self.assertIn(TestData.HOME_PAGE_HEADER_1, self.main_page.get_element_text_content(Locators.PAGE_HEADER),
                      "Test Failed. It's not correct website")

    def test_02_check_required_elements(self):
        """
        1. Open the main page in the web browser.
        2. Check if all required elements are on main page.
        """
        self.main_page = Pages.MainPage(self.driver)
        self.assertTrue(self.main_page.is_logo_exists(),
                        "The Logo doesn't exist on website")
        self.assertTrue(self.main_page.is_visible(Locators.NAME_INPUT),
                        "The Input Name Field doesn't exist on website")
        self.assertTrue(self.main_page.is_visible(Locators.EMAIL_INPUT),
                        "The Input Email Field  doesn't exist on website")
        self.assertTrue(self.main_page.is_visible(Locators.EXPERIENCE_INPUT),
                        "The Input Experience Field  doesn't exist on website")
        self.assertTrue(self.main_page.is_visible(Locators.POSITION_SELECT),
                        "The Select Position List doesn't exist on website")
        self.assertTrue(self.main_page.is_visible(Locators.TERMS_CHECKBOX),
                        "The Terms Checkbox doesn't exist on website")
        self.assertTrue(self.main_page.is_visible(Locators.SUBMIT_BUTTON),
                        "The Submit button doesn't exist on website")
        self.assertTrue(self.main_page.is_visible(Locators.CLEAR_BUTTON),
                        "The Clear button doesn't exist on website")

    def test_03_check_logo_link_on_main_page(self):
        """
        1. Open the main page in the web browser.
        2. Locate the Northmill's logo
        3. Check if the opened site it's an Official Nortmill Home Page
        """
        self.main_page = Pages.MainPage(self.driver)
        self.assertTrue(self.main_page.is_logo_exists(),
                        "The Logo doesn't exist on website")
        self.main_page.click(Locators.LOGO)
        self.assertTrue(self.main_page.is_url_matches(TestData.NORTHMILL_WEBPAGE_LINK),
                        "Test Failed. It's not correct website")

    def test_04_enter_valid_name_01(self):
        """
        1. Open the main page in the web browser.
        2. Locate and Enter in the name field the valid name, "ab"
        3. Check if name was entered correctly
        4. Check if validation text is NOT visible
        """

        self.main_page = Pages.MainPage(self.driver)
        self.main_page.form_enter_name(TestData.NAME_INPUT_DATA_VALID_01)
        self.assertEqual(self.main_page.get_value_of_element(Locators.NAME_INPUT), TestData.NAME_INPUT_DATA_VALID_01,
                         "Test Failed. The Name is Not entered correctly")
        self.assertTrue(self.main_page.validation_err_msg(Locators.NAME_INPUT_ERROR, False),
                        "Test Failed. The Name Validation Method Fails")

    def test_05_enter_valid_name_02(self):
        """
        1. Open the main page in the web browser.
        2. Locate and Enter in the name field the valid name, "abc"
        3. Check if name was entered correctly
        4. Check if validation text is NOT visible
        """
        self.main_page = Pages.MainPage(self.driver)
        self.main_page.form_enter_name(TestData.NAME_INPUT_DATA_VALID_02)
        self.assertEqual(self.main_page.get_value_of_element(Locators.NAME_INPUT), TestData.NAME_INPUT_DATA_VALID_02,
                         "Test Failed. The Name is Not entered correctly")
        self.assertTrue(self.main_page.validation_err_msg(Locators.NAME_INPUT_ERROR, False),
                        "Test Failed. The Name Validation Method Fails")

    def test_06_enter_invalid_name(self):
        """
        1. Open the main page in the web browser.
        2. Locate and Enter in the name field the invalid name, "a"
        3. Check if name was entered correctly
        4. Check if validation text is visible
        """
        self.main_page = Pages.MainPage(self.driver)
        self.main_page.form_enter_name(TestData.NAME_INPUT_DATA_INVALID)
        self.assertEqual(self.main_page.get_value_of_element(Locators.NAME_INPUT), TestData.NAME_INPUT_DATA_INVALID,
                         "Test Failed. The Name is Not entered correctly")
        self.assertTrue(self.main_page.validation_err_msg(Locators.NAME_INPUT_ERROR, True),
                        "Test Failed. The Name Validation Method Fails")

    def test_07_enter_valid_email(self):
        """
        1. Open the main page in the web browser.
        2. Locate and Enter in the email field the valid email, "abc@abc.com"
        3. Check if email was entered correctly
        4. Check if validation text is NOT visible
        """
        self.main_page = Pages.MainPage(self.driver)
        self.main_page.form_enter_email(TestData.EMAIL_INPUT_DATA_VALID)
        self.assertEqual(self.main_page.get_value_of_element(Locators.EMAIL_INPUT), TestData.EMAIL_INPUT_DATA_VALID,
                         "Test Failed. The Email is Not entered correctly")
        self.assertTrue(self.main_page.validation_err_msg(Locators.EMAIL_INPUT_ERROR, False),
                        "Test Failed. The Email Validation Method Fails")

    def test_08_enter_invalid_email(self):
        """
        1. Open the main page in the web browser.
        2. Locate and Enter in the email field the invalid email, "ABC@"
        3. Check if email was entered correctly
        4. Check if validation text is visible
        """
        self.main_page = Pages.MainPage(self.driver)
        self.main_page.form_enter_email(TestData.EMAIL_INPUT_DATA_INVALID)
        self.assertEqual(self.main_page.get_value_of_element(Locators.EMAIL_INPUT), TestData.EMAIL_INPUT_DATA_INVALID,
                         "Test Failed. The Email is Not entered correctly")
        self.assertTrue(self.main_page.validation_err_msg(Locators.EMAIL_INPUT_ERROR, True),
                        "Test Failed. The Email Error Message Validation Validation Fails")

    def test_09_enter_years_experience_as_number(self):
        """
        1. Open the main page in the web browser.
        2. Locate and Enter in the experience field the valid value, "3" 
        3. Check if value was entered correctly
        4. Check if validation text is NOT visible
        """
        self.main_page = Pages.MainPage(self.driver)
        self.main_page.form_enter_experience(TestData.EXPERIENCE_INPUT_DATA_VALID_01)
        self.assertEqual(self.main_page.get_value_of_element(Locators.EXPERIENCE_INPUT),
                         TestData.EXPERIENCE_INPUT_DATA_VALID_01,
                         "Test Failed. Experience is Not entered correctly")
        self.assertTrue(self.main_page.validation_err_msg(Locators.EXPERIENCE_INPUT_ERROR, False),
                        "Test Failed. Experience in Years Error Message Validation Fails")

    def test_10_enter_years_experience_as_negative_number(self):
        """
        1. Open the main page in the web browser.
        2. Locate and Enter in the experience field the invalid value, "-3" 
        3. Check if value was entered correctly
        4. Check if validation text is visible
        """
        self.main_page = Pages.MainPage(self.driver)
        self.main_page.form_enter_experience(TestData.EXPERIENCE_INPUT_DATA_INVALID_01)
        self.assertEqual(self.main_page.get_value_of_element(Locators.EXPERIENCE_INPUT),
                         TestData.EXPERIENCE_INPUT_DATA_INVALID_01,
                         "Test Failed. Experience is Not entered correctly")
        self.assertTrue(self.main_page.validation_err_msg(Locators.EXPERIENCE_INPUT_ERROR, True),
                        "Test Failed. Experience in Years Error Message Validation Fails")

    def test_11_enter_years_experience_as_letter(self):
        """
        1. Open the main page in the web browser.
        2. Locate and Enter in the experience field the invalid value, "eee" 
        3. Check if experience value back to its default, empty
        4. Check if validation text is NOT visible
        """
        self.main_page = Pages.MainPage(self.driver)
        self.main_page.form_enter_experience(TestData.EXPERIENCE_INPUT_DATA_INVALID_02)
        self.assertEqual(self.main_page.get_value_of_element(Locators.EXPERIENCE_INPUT), "",
                         "Test Failed. The Experience doesn't have it's default value")
        self.assertTrue(self.main_page.validation_err_msg(Locators.EXPERIENCE_INPUT_ERROR, False),
                        "Test Failed. Experience in Years Error Message Validation Fails")

    def test_12_select_role_position(self):
        """
        1. Open the main page in the web browser.
        2. Locate and Select the IT position from the list, "Frontend Developer". 
        3. Check if the value was selected correctly
        4. Check if validation text is NOT visible
        """
        self.main_page = Pages.MainPage(self.driver)
        self.main_page.list_select_position(TestData.POSITION_LIST_DATA)
        self.assertEqual(self.main_page.get_value_of_list_selection(Locators.POSITION_SELECT),
                         TestData.POSITION_LIST_DATA,
                         "Test Failed. Position is Not selected correctly")
        self.assertTrue(self.main_page.validation_err_msg(Locators.POSITION_SELECT_ERROR, False),
                        "Test Failed. Position Error Message Validation Fails")

    def test_13_tick_terms_checkbox_on(self):
        """
        1. Open the main page in the web browser.
        2. Locate and tick on the Terms and Condition CheckBox 
        3. Check if checkbex is selected
        4. Check if validation text is NOT visible
        """
        self.main_page = Pages.MainPage(self.driver)
        self.main_page.hit_terms_checkbox()
        self.assertTrue(self.main_page.is_selected(Locators.TERMS_CHECKBOX, True),
                        "Test Failed. Terms Checkbox isn't ticked")
        self.assertTrue(self.main_page.validation_err_msg(Locators.TERMS_CHECKBOX_ERROR, False),
                        "Test Failed. Terms Error Message Validation Fails")

    def test_14_tick_terms_checkbox_off(self):
        """
        1. Open the main page in the web browser.
        2. Locate and tick the Terms and Condition CheckBox 
        3. Check if checkbox is selected
        4. Locate and un-tick the Terms and Condition CheckBox
        5. Check if checkbox is deselected
        6. Check if validation text is visible
        """
        self.main_page = Pages.MainPage(self.driver)

        self.main_page.hit_terms_checkbox()

        self.assertTrue(self.main_page.is_selected(Locators.TERMS_CHECKBOX, True),
                        "Test Failed. Terms Checkbox isn't ticked")

        self.main_page.hit_terms_checkbox()

        self.assertTrue(self.main_page.is_selected(Locators.TERMS_CHECKBOX, False),
                        "Test Failed. Terms Checkbox is ticked")
        self.assertTrue(self.main_page.validation_err_msg(Locators.TERMS_CHECKBOX_ERROR, True),
                        "Test Failed. Terms Error Message Validation Fails")

    def test_15_check_terms_link(self):
        """
        1. Open the main page in the web browser.
        2. Locate and Click on the "Terms and Conditions" Text. 
        3. Check if NEW window with Terms and Conditions appears
        """
        self.main_page = Pages.MainPage(self.driver)

        self.main_page.hit_terms_link()

        self.assertIn(TestData.TERMS_TEXT, self.main_page.get_element_text_content(Locators.TERMS_CONTENT),
                      "Test Failed. The Terms doesn't show")

    def test_16_check_submit_button_success_page(self):
        """
        1. Open the main page in the web browser.
        2. Fill all required elements correctly, and type in experience 3 years
        3. Click on the Submit button
        4. Check if opened webpage it's a Success page
        5. Locate and Click on Northmill's logo
        6. Check if opened webpage it's a Official Northmill's Site
        """
        # initiate the page object
        self.main_page = Pages.MainPage(self.driver)

        # Fill all required fields
        self.main_page.form_enter_name(TestData.NAME_INPUT_DATA_VALID_01)
        self.main_page.form_enter_email(TestData.EMAIL_INPUT_DATA_VALID)
        self.main_page.form_enter_experience(TestData.EXPERIENCE_INPUT_DATA_VALID_01)
        self.main_page.list_select_position(TestData.POSITION_LIST_DATA)
        self.main_page.form_enter_about(TestData.ABOUT_YOU_INPUT)
        self.main_page.click(Locators.TERMS_CHECKBOX)

        # click Submit
        self.main_page.hit_submit()

        # check
        self.assertIn(TestData.SUCCESS_PAGE_HEADER_1, self.main_page.get_element_text_content(Locators.PAGE_HEADER),
                      "Test Failed. It's not correct website")
        self.assertTrue(self.main_page.is_logo_exists(),
                        "The Logo doesn't exist on website")
        self.main_page.click(Locators.LOGO)
        self.assertTrue(self.main_page.is_url_matches(TestData.NORTHMILL_WEBPAGE_LINK),
                        "Test Failed. It's not a correct website")

    def test_17_check_submit_button_failure_page(self):
        """
        1. Open the main page in the web browser.
        2. Fill all required elements correctly, and type in experience 1 year
        3. Click on the Submit button
        4. Check if opened webpage it's a Failure page
        5. Locate and Click on Northmill's logo
        6. Check if opened webpage it's a Official Northmill's Site
        """
        # initiate the page object
        self.main_page = Pages.MainPage(self.driver)

        # Fill all required fields
        self.main_page.form_enter_name(TestData.NAME_INPUT_DATA_VALID_01)
        self.main_page.form_enter_email(TestData.EMAIL_INPUT_DATA_VALID)
        self.main_page.form_enter_experience(TestData.EXPERIENCE_INPUT_DATA_VALID_02)
        self.main_page.list_select_position(TestData.POSITION_LIST_DATA)
        self.main_page.form_enter_about(TestData.ABOUT_YOU_INPUT)
        self.main_page.click(Locators.TERMS_CHECKBOX)

        # click Submit
        self.main_page.hit_submit()

        # check
        self.assertIn(TestData.FAILED_PAGE_HEADER_1, self.main_page.get_element_text_content(Locators.PAGE_HEADER),
                      "Test Failed. It's not correct website")
        self.assertTrue(self.main_page.is_logo_exists(),
                        "The Logo doesn't exist on website")
        self.main_page.click(Locators.LOGO)
        self.assertTrue(self.main_page.is_url_matches(TestData.NORTHMILL_WEBPAGE_LINK),
                        "Test Failed. It's not a correct website")

    def test_18_check_clear_button(self):
        """
        1. Open the main page in the web browser.
        2. Fill all required input elements in various way
        3. Locate and Click the Clear button
        3. Check if all of the values of input web elements return to their defaults values
        """
        # initiate the page object
        self.main_page = Pages.MainPage(self.driver)

        # Fill all fields
        self.main_page.form_enter_name(TestData.NAME_INPUT_DATA_VALID_01)
        self.main_page.form_enter_email(TestData.EMAIL_INPUT_DATA_INVALID)
        self.main_page.form_enter_experience(TestData.EXPERIENCE_INPUT_DATA_INVALID_01)
        self.main_page.list_select_position(TestData.POSITION_LIST_DATA)
        self.main_page.form_enter_about(TestData.ABOUT_YOU_INPUT)
        self.main_page.click(Locators.TERMS_CHECKBOX)

        # click Clear
        self.main_page.hit_clear()

        # Check if all input web elements have defaults values
        self.assertEqual(self.main_page.get_value_of_element(Locators.NAME_INPUT), "",
                         "Test Failed. The Name doesn't have it's default value")
        self.assertEqual(self.main_page.get_value_of_element(Locators.EMAIL_INPUT), "",
                         "Test Failed. The Email doesn't have it's default value")
        self.assertEqual(self.main_page.get_value_of_element(Locators.EXPERIENCE_INPUT), "",
                         "Test Failed. The Experience doesn't have it's default value")
        self.assertEqual(self.main_page.get_value_of_list_selection(Locators.POSITION_SELECT), "",
                         "Test Failed. Position doesn't have it's default value")
        self.assertEqual(self.main_page.get_value_of_element(Locators.ABOUT_YOU_AREA), "",
                         "Test Failed. About You doesn't have it's default value")
        self.assertTrue(self.main_page.is_selected(Locators.TERMS_CHECKBOX, False),
                        "Test Failed. Terms Checkbox doesn't have it's default value")


if __name__ == "__main__":
    unittest.main()
