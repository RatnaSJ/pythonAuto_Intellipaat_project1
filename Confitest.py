
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://intellipaat.com/'


@pytest.fixture
def driver_initialisation():

    driver.get(url)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    yield driver
    driver.quit()