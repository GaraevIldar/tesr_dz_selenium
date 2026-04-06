from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.test_add import positive_data_provider
from utilities.data_provider import DataProvider



positive_data_provider = DataProvider("delete","data_delete_positive_test.json")

def test_delete_positive():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        test_data = positive_data_provider.get_test_case("TC-1_DeleteObject")

        driver.get(test_data["url"])

        driver.find_element(By.ID, "delete-record-1").click()

        assert "Cierra" not in driver.page_source

    finally:
        driver.quit()
