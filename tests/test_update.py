from selenium import webdriver
from page_object.page_web_tables import WebTables

from utilities.data_provider import DataProvider

positive_data_provider = DataProvider("update","data_update_positive_test.json")
driver = webdriver.Chrome()
page = WebTables(driver)

def test_update_positive():

    driver.maximize_window()

    try:
        test_case = positive_data_provider.get_test_case("TC-1_UpdateObject")

        test_data = test_case["form_data"]
        url = test_case["url"]

        driver.get(url)

        page.update_object(test_data,"edit-record-1")

        assert test_data["firstName"] in driver.page_source
        assert "Cierra" not in driver.page_source

    finally:
        driver.quit()