import page
from base.base import Base


class PageHome(Base):

    # 获取我的商城文本
    def page_is_home(self):
        return self.base_get_text(page.my_shop)