from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from page_object.page_login import LoginPage
from utilities.data_provider import DataProvider


positive_data_provider = DataProvider("login","data_login_positive_test.json")
driver = webdriver.Chrome()
page = LoginPage(driver)

def test_login_positive():
    wait = WebDriverWait(driver, 10)

    try:
        test_case = positive_data_provider.get_test_case("TC-1_SuccessLogin")

        test_data = test_case["form_data"]
        url = test_case["url"]

        driver.get(url)

        page.login(test_data)

        wait.until(EC.url_contains("/secure"))

        assert "/secure" in driver.current_url

    finally:
        driver.quit()


