from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.home_login_button_locator = (By.XPATH, '//a[@class="login-myact"]')
        self.user_name_field_locator = (By.XPATH, '//input[@name="log"]')
        self.login_password_field_locator = (By.XPATH, '//input[@name="pwd"]')
        self.submt_Log_In_Btn_locator = (By.XPATH, '//input[@id="lwa_wp-submit"]')
        self.logged_in_user_btn = (By.XPATH, '//a[@class="loggedinuser-btn"]')
        self.log_out_btn = (By.XPATH, '//a[@id="destroy-sessions"]')

    def click_home_login_button(self):
        self.driver.find_element(*self.home_login_button_locator).click()

    def user_name_field(self, emailaddress):
        user_name = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.user_name_field_locator))
        user_name.send_keys(emailaddress)

    def login_password(self, password):
        pass_word = self.driver.find_element(*self.login_password_field_locator)
        pass_word.send_keys(password)

    def click_on_submit_log_in_(self):
        self.driver.find_element(*self.submt_Log_In_Btn_locator).click()

    def click_logged_in_user_btn(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.logged_in_user_btn)).click()

    def click_log_out_btn(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.log_out_btn)).click()








