from time import sleep
from tools.get_logging import GetLogging
import page
from base.base import Base

log = GetLogging.get_logger()


class PageLogin(Base):

    # 1.输入用户名
    def page_input_username(self, username):
        self.base_input(page.username, username)

    # 2.输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.password, pwd)

    # 3.输入验证码
    def page_input_code(self, code):
        self.base_input(page.verify_code, code)

    # 4.点击登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    def page_error_info(self):
        return self.base_get_text(page.error_info)

    def page_click_error_btn(self):
        sleep(1)
        self.base_click(page.close_error)

    # 5.组合业务
    def login(self, username, pwd, code):
        log.info("正在调用TPshop登录业务方法，用户名：%s，密码：%s，验证码：%s" % (username, pwd, code))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_code(code)
        self.page_click_login_btn()
