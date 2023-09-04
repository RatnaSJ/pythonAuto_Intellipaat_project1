from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class SignupPage:

    def __init__(self, driver):

        self.driver = driver
        self.home_login_button_locator = (By.XPATH, '//a[@class="login-myact"]')
        self.sign_up_link_locator = (By.XPATH, '//a[text()=" Sign Up"]')
        self.first_name_field_locator = (By.XPATH, '//input[@id="reg_sr_firstname"]')
        self.last_name_field_locator = (By.XPATH, '//input[@id="reg_sr_lastname"]')
        self.email_address_field_locator = (By.XPATH, '//input[@id="reg_email"]')
        self.signup_password_locator = (By.XPATH, '//input[@id="reg_password"]')
        self.phone_num_field_locator = (By.XPATH, '//input[@id="reg_sr_phone"]' )
        self.select_country_locator = (By.XPATH, '//select[@id="ip-vk-country-obts"]')
        self.register_button_locator = (By.XPATH, '//input[@type="submit"]')
        self.logged_in_user_btn = (By.XPATH, '//a[@class="loggedinuser-btn"]')
        self.log_out_btn = (By.XPATH, '//a[@id="destroy-sessions"]')

    def click_home_login_button(self):
        self.driver.find_element(*self.home_login_button_locator).click()

    def click_sign_up_link(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.sign_up_link_locator)).click()

    def enter_first_name(self, firstname):
        self.driver.find_element(*self.first_name_field_locator).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(*self.last_name_field_locator).send_keys(lastname)

    def enter_email_address(self, email_address):
        self.driver.find_element(*self.email_address_field_locator).send_keys(email_address)

    def enter_signup_password(self, password):
        self.driver.find_element(*self.signup_password_locator).send_keys(password)

    def enter_phone_num(self, phone_num):
        self.driver.find_element(*self.phone_num_field_locator).send_keys(phone_num)

    def select_country(self, country_code):
        sel = Select(self.driver.find_element(*self.select_country_locator))
        sel.select_by_value(value="+91")

    def click_register_button(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.register_button_locator)).click()

    def click_logged_in_user_btn(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.logged_in_user_btn)).click()

    def click_log_out_btn(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.log_out_btn)).click()
