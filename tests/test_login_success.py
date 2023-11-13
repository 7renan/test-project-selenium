import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_login_success(driver):
  login_page = LoginPage()
  login_page.login("standard_user", "secret_sauce")
  assert driver.find_element(By.XPATH, "//div[@class='product_label' and text()='Products']").is_displayed()