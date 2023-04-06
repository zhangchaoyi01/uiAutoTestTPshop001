import os
import time
from time import sleep
import sys
from selenium.webdriver.support.wait import WebDriverWait
from config import BASE_PATH
from tools.get_logging import GetLogging

log = GetLogging.get_logger()


class Base:
    def __init__(self, driver):
        log.info("正在初始化driver：%s" % driver)
        self.driver = driver

    def base_find(self, loc, timeout=30, poll=0.5):
        """
            元素定位
        :param loc: 元素定位信息，格式为：元组
        :param timeout: 显示等待时间，查找元素超时时间，默认30s
        :param poll: 查找元素评率，默认0.5
        :return: 定位到的元素
        """
        log.info("正在定位[%s:%s]" % (loc[0], loc[1]))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))  # 匿名函数lambda

    def base_input(self, loc, value):
        """
            输入
        :param loc: 元素定位信息
        :param value: 输入内容
        """
        el = self.base_find(loc)
        log.info("正在对[%s:%s]输入框进行清空" % (loc[0], loc[1]))
        el.clear()
        log.info("正在对[%s:%s]输入框输入内容：%s" % (loc[0], loc[1], value))
        el.send_keys(value)

    def base_click(self, loc):
        """
            点击
        :param loc: 元素定位信息
        """
        sleep(1)
        log.info("正在对[%s:%s]元素进行点击" % (loc[0], loc[1]))
        self.base_find(loc).click()

    def base_get_text(self, loc):
        """
            获取文本
        :param loc: 元素定位信息
        :return: 获取到的文本值
        """
        text = self.base_find(loc).text
        log.info("正在获取%s元素文本：%s" % (loc, text))
        return text

    def base_get_img(self):
        # 获取当前日期
        new_time = time.strftime("%Y-%m-%d_%H-%M-%S")
        # 获取报错信息，信息为元组
        exec_info = sys.exc_info()
        # 获取本地项目路径
        file_path = BASE_PATH + os.sep + "image" + os.sep
        # 注意：exec_info为元组，格式化输入时要下标获取其中的错误信息
        log.error("正在进行截图操作!")
        self.driver.get_screenshot_as_file(file_path + "%s-%s.png" % (new_time, exec_info[1]))

