from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.data_provider import DataProvider

positive_data_provider = DataProvider("update","data_update_positive_test.json")

def test_update_positive():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        test_date = positive_data_provider.get_test_case("TC-1_UpdateObject")

        driver.get(test_date["url"])

        driver.find_element(By.ID, "edit-record-1").click()

        first_name = driver.find_element(By.ID, "firstName")
        first_name.clear()
        first_name.send_keys(test_date["first_name"])

        driver.find_element(By.ID, "submit").click()

        driver.find_element(By.CLASS_NAME, "btn-close").click()

        assert test_date["first_name"] in driver.page_source
        assert "Cierra" not in driver.page_source

    finally:
        driver.quit()