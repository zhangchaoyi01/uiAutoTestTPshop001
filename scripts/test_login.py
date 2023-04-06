import unittest
from time import sleep
from parameterized import parameterized
import page
from base.base import Base
from page.page_home import PageHome
from page.page_index import PageIndex
from page.page_login import PageLogin
from tools.get_driver import GetDriver
from tools.read_json import get_data
from tools.get_logging import GetLogging

log = GetLogging.get_logger()


class TestLogin(unittest.TestCase):

    # 初始化
    @classmethod
    def setUpClass(cls):  # 没有参数化使用类方法和函数方法没有区别，使用参数化建议使用类方法
        # 1.获取driver
        driver = GetDriver.get_web_driver(page.url)
        # 2.通过统一入口类获取PageLogin对象
        # cls.page_login = PageIn(driver).page_get_PageLogin()
        cls.page_login = PageLogin(driver)
        cls.page_index = PageIndex(driver)
        cls.page_home = PageHome(driver)
        cls.base = Base(driver)
        # 点击首页登录链接
        cls.page_index.page_login_link()

    # 结束
    @classmethod
    def tearDownClass(cls):
        # 调用关闭driver
        sleep(2)
        GetDriver.quit_web_driver()

    @parameterized.expand(get_data())
    # @parameterized.expand(read_yaml("login.yaml"))
    def test_login(self, username, pwd, code, expect_result, success):
        """登录测试"""
        # 调用业务组合方法实现业务逻辑
        self.page_login.login(username, pwd, code)
        # 断言
        if success:
            try:
                self.assertIn(expect_result, self.page_home.page_is_home())
            except AssertionError as e:
                log.error("断言错误，错误信息：%s" % e)
                self.base.base_get_img()
                raise
        else:
            msg = self.page_login.page_error_info()
            try:
                # 有时候不能截图，是断言方法的问题，换一个断言方法就可以了，比如：assertEqual
                self.assertIn(expect_result, msg)
            except AssertionError as e:
                log.error("断言错误，错误信息：%s" % e)
                self.base.base_get_img()
                raise
            finally:
                self.page_login.page_click_error_btn()
