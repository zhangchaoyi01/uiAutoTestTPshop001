from page.page_login import PageLogin


class PageIn:

    def __init__(self, driver):
        self.driver = driver

    def page_get_PageLogin(self):
        return PageLogin(self.driver)
