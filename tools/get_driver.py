from selenium import webdriver
import os
from config import BASE_PATH
import sys
import time


class GetDriver:
    # 1.声明变量
    driver = None

    # 2.获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.get(url)
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    # 3.退出driver
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.driver:
            # 退出操作
            cls.driver.quit()

            # 置空操作 注意：执行完退出方法后，driver在内存中的地址还是存在的，
            # 有地址存在，get_web_driver（）判断就不为空，导致，只有第一次获取的driver能成功，之后永远不会成功
            cls.driver = None
