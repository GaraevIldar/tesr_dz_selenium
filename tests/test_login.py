from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from utilities.data_provider import DataProvider

positive_data_provider = DataProvider("login","data_login_positive_test.json")

def test_login_positive():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:

        test_data = positive_data_provider.get_test_case("TC-1_SuccessLogin")

        driver.get(test_data["url"])

        driver.find_element(By.ID, "username").send_keys(test_data["username"])

        driver.find_element(By.ID, "password").send_keys(test_data["password"])

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        wait.until(EC.url_contains("/secure"))

        assert "/secure" in driver.current_url

    finally:
        driver.quit()