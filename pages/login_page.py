import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests import conftest


class LoginPage:
  def __init__(self) -> None:
    self.driver = conftest.driver
  
  def login(self, username, password):
    self.driver.find_element(By.ID, "user-name").send_keys(username)
    self.driver.find_element(By.ID, "password").send_keys(password)
    self.driver.find_element(By.ID, "login-button").click()
    time.sleep(3)