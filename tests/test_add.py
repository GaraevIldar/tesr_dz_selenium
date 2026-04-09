from selenium import webdriver

from utilities.data_provider import DataProvider
from page_object.page_web_tables import WebTables

positive_data_provider = DataProvider("add","data_add_positive_test.json")
driver = webdriver.Chrome()
page = WebTables(driver)

def test_add_positive():
    try:
        test_data = positive_data_provider.get_test_case("TC-1_AddObject")["form_data"]
        url = positive_data_provider.get_test_case("TC-1_AddObject")["url"]

        driver.get(url)

        page.add_object(test_data)

        assert test_data['firstName'] in driver.page_source

    finally:
        driver.quit()
