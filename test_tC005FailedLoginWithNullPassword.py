# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTC005FailedLoginWithNullPassword():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC005FailedLoginWithNullPassword(self):
    # Test name: TC005_Failed Login With Null Password
    # Step # | name | target | value
    # 1 | open | https://www.saucedemo.com/ | 
    self.driver.get("https://www.saucedemo.com/")
    # 2 | setWindowSize | 734x852 | 
    self.driver.set_window_size(734, 852)
    # 3 | click | css=*[data-test="username"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    # 4 | type | css=*[data-test="username"] | standard_user
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    # 5 | click | css=*[data-test="password"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    # 6 | click | css=*[data-test="login-button"] | 
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    # 7 | assertText | css=*[data-test="error"] | Epic sadface: Password is required
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Password is required"
    # 8 | close |  | 
    self.driver.close()
  