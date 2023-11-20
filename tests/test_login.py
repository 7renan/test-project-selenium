import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_login_success(driver):
  login_page = LoginPage(driver)
  login_page.login_success("standard_user", "secret_sauce")
  assert driver.find_element(By.XPATH, "//div[@class='product_label' and text()='Products']").is_displayed()

def test_login_falled(driver):
  login_page = LoginPage(driver)
  login_page.login_falled("standard_user", "secret_sauce_falled")
  assert driver.find_element(By.XPATH, "//h3[contains(text(), 'Epic sadface')]").is_displayed()