import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests import conftest

from pages.base_page import BasePage


class LoginPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    self.username_field = (By.ID, "user-name")
    self.password_field = (By.ID, "password")
    self.login_button = (By.ID, "login-button")
  
  def login_success(self, username, password):
    self.send_keys(self.username_field, username)
    self.send_keys(self.password_field, password)
    self.click(self.login_button)

  def login_falled(self, username, password):
    self.send_keys(self.username_field, username)
    self.send_keys(self.password_field, password)
    self.click(self.login_button)