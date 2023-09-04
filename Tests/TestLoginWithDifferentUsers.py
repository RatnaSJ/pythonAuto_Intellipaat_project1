import time
import json5
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from Confitest import webdriver, driver
from log_config import configure_logger
from Utilities.LoginUtility import LoginPage


def login_user_data(driver, logger, user_data):
    try:
        login_page = LoginPage(driver)
        login_page.click_home_login_button()
        login_page.user_name_field(user_data["emailaddress"])
        login_page.login_password(user_data["password"])
        login_page.click_on_submit_log_in_()
        login_page.click_logged_in_user_btn()
        login_page.click_log_out_btn()

        # After clicking login button wait for confirmation
        wait = WebDriverWait(driver, 20)
        confirmation_element = wait.until(EC.presence_of_element_located
                                          ((By.XPATH, '//*[text()="Upskill Yourself"]')))

        # Assert that the confirmation element is displayed, indicating successful login
        assert confirmation_element.is_displayed(), "Login was not successful"
        logger.info(f"User {user_data['emailaddress']} login completed successfully")

    except Exception as e:
        logger.error(f"error during login for user {user_data['emailaddress']}: {str(e)}")


def main():
    logger = configure_logger('login.log')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://intellipaat.com/')
    driver.maximize_window()

    try:
        with open("SignupUser.json5", "r") as jsonobj:
            user_data = json5.load(jsonobj)
            # loop through users and signup
            for user in user_data["signup_list"]:
                driver.delete_all_cookies()  # clear cookies for fresh session
                login_user_data(driver, logger, user)
                time.sleep(5)

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

    finally:
        driver.quit()
        logger.info("Test execution completed")


if __name__ == "__main__":
    main()













