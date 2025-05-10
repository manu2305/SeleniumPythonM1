import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup2")
class Test_admin:
    def test_tc_01(self):
        time.sleep(5)
        expected_output=self.driver.find_element(By.XPATH, "//span[text()='Admin']")
        assert expected_output.is_displayed(), "admin is not displayed"
        print("admin is displayed")
    def test_tc_02(self):
        print("tc_02")

    def test_tc_03(self):
        print("tc_02")

    def test_tc_04(self):
        print("tc_02")

    def test_tc_05(self):
        print("tc_02")