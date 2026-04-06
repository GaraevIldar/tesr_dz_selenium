from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tenacity import sleep_using_event

from utilities.data_provider import DataProvider

positive_data_provider = DataProvider("add","data_add_positive_test.json")

def test_add_positive():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        test_data = positive_data_provider.get_test_case("TC-1_AddObject")

        driver.get(test_data["url"])

        driver.find_element(By.ID, "addNewRecordButton").click()

        driver.find_element(By.ID, "firstName").send_keys(test_data["first_name"])
        driver.find_element(By.ID, "lastName").send_keys(test_data["last_name"])
        driver.find_element(By.ID, "userEmail").send_keys(test_data["email"])
        driver.find_element(By.ID, "age").send_keys(test_data["age"])
        driver.find_element(By.ID, "salary").send_keys(test_data["salary"])
        driver.find_element(By.ID, "department").send_keys(test_data["department"])

        driver.find_element(By.ID, "submit").click()

        row = wait.until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()='{test_data['first_name']}']"))
        )

        assert row is not None

    finally:
        driver.quit()
