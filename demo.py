from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from config import BASE_PATH
import sys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://www.tpshop.com")

driver.find_element(By.LINK_TEXT, "登录").click()
driver.find_element(By.ID, "username").send_keys("17600682222")
driver.find_element(By.ID, "password").send_keys("123123")
driver.find_element(By.ID, "verify_code").send_keys(8888)
driver.find_element(By.CLASS_NAME, "J-login-submit").click()


new_time = time.strftime("%Y-%m-%d_%H-%M-%S")
exec_info = sys.exc_info()
file_path = BASE_PATH + os.sep + "image" + os.sep
driver.get_screenshot_as_file(file_path + "%s-%s.png" % (new_time, exec_info[1]))



# base_get_image()
