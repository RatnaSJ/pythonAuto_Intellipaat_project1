
import time

import json5
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from log_config import configure_logger
from Utilities.SignupUtility import SignupPage


def signup_user_data(driver, logger, user_data):
    try:
        signup_page = SignupPage(driver)
        signup_page.click_home_login_button()
        signup_page.click_sign_up_link()
        signup_page.enter_first_name(user_data["firstname"])
        signup_page.enter_last_name(user_data["lastname"])
        signup_page.enter_email_address(user_data["emailaddress"])
        signup_page.enter_signup_password(user_data["password"])
        signup_page.enter_phone_num(user_data["phone"])
        signup_page.select_country("+91")
        signup_page.click_register_button()
        signup_page.click_logged_in_user_btn()
        signup_page.click_log_out_btn()

        # After clicking register button wait for confirmation
        wait = WebDriverWait(driver, 20)
        confirmation_element = wait.until(EC.presence_of_element_located
                                          ((By.XPATH, '//*[text()="Upskill Yourself"]')))

        # Assert that the confirmation element is displayed, indicating successful signup
        assert confirmation_element.is_displayed(), "Signup was not successful"
        logger.info(f"User {user_data['emailaddress']} registration completed successfully")

    except Exception as e:
        logger.error(f"Error during signup for user {user_data['emailaddress']}: {str(e)}")


def main():
    logger = configure_logger('test.log')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://intellipaat.com/')
    driver.maximize_window()

    try:
        with open("SignupUser.json5", "r") as jsonobj:
            user_data = json5.load(jsonobj)
            # loop through users and signup
            for user in user_data["signup_list"]:
                driver.delete_all_cookies() # clear cookies for fresh session
                signup_user_data(driver, logger, user)
                time.sleep(5)

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

    finally:
        driver.quit()
        logger.info("Test execution completed")


if __name__ == "__main__":
    main()
