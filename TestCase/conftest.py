import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def setup1(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    request.cls.driver=driver
    yield
    driver.quit()

@pytest.fixture
def setup2(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    request.cls.driver=driver
    yield
    driver.find_element(By.CLASS_NAME,"oxd-userdropdown-tab").click()
    driver.find_element(By.XPATH,"//a[text()='Logout']").click()
    driver.quit()