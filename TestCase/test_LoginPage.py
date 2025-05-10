import time

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup1")
class Test_login:

    def test_tc_01(self):
        expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
        assert self.driver.current_url==expected_url,"login not successfull"
        print("login is successfull")
        time.sleep(5)

    def test_tc_02(self):
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME,"password").send_keys("admin")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        assert self.driver.current_url!=expected_url,"login successfull defect is found"
        time.sleep(5)

    def test_tc_03(self):
        print("tc_03")

    def test_tc_04(self):
        print("tc_04")
