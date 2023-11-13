from selenium import webdriver
import pytest

driver: webdriver.Remote

@pytest.fixture()
def driver():
  global driver
  driver = webdriver.Chrome()
  driver.implicitly_wait(5)
  driver.maximize_window()
  driver.get("https://www.saucedemo.com/v1/")
  yield driver
  driver.quit()
