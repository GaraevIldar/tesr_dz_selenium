from selenium import webdriver

from page_object.page_web_tables import WebTables
from tests.test_add import positive_data_provider
from utilities.data_provider import DataProvider



positive_data_provider = DataProvider("delete","data_delete_positive_test.json")
driver = webdriver.Chrome()
page = WebTables(driver)

def test_delete_positive():

    driver.maximize_window()

    try:
        test_data = positive_data_provider.get_test_case("TC-1_DeleteObject")

        driver.get(test_data["url"])

        page.delete_object("delete-record-1")

        assert "Cierra" not in driver.page_source

    finally:
        driver.quit()
