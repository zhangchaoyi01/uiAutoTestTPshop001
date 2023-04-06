from selenium.webdriver.common.by import By
"""
CSS定位方法：效率高（能用CSS不用XPATH）
    ID：#username
    
    class选择器：如：.telA <选择class属性值为telA的所有元素>  根据元素class属性来选择
    
    元素选择器：如：input <选择所有input元素>  根据元素的标签名选择
    
    层级选择器：如：p>input <返回所有p元素下所有的input元素>  格式：element>element 
              说明：根据元素的父子关系来选择   
              提示：> 可以用空格代替 如：p input 或者 p [type='password']
    
    属性选择器：格式：[attribute=value] 如：[type="password"] <选择所有type属性值为password的值>
              说明：根据元素的属性名和值来选择
    
    1. input[type^='p']     说明：type属性以p字母开头的元素
    2. input[type$='d']     说明：type属性以d字母结束的元素
    3. input[type*='w']     说明：type属性包含w字母的元素
"""


"""-----------------------------------------login_page_element------------------------------------------"""
# TPshop商城前端地址
url = "http://www.tpshop.com"

# TPshop后台地址
url_back = "http://www.tpshop.com/index.php/Admin/Index/index"

# 用户名
username = (By.ID, "username")
# 密码
password = (By.ID, "password")
# 验证码
verify_code = (By.ID, "verify_code")
# 登录按钮
login_btn = (By.CLASS_NAME, "J-login-submit")
# 获取错误弹窗信息
error_info = (By.CSS_SELECTOR, ".layui-layer-content")
# 关闭错误弹窗
close_error = (By.CSS_SELECTOR, ".layui-layer-btn0")





"""-----------------------------------------index_page_element------------------------------------------"""
# 点击登录
login_link = (By.LINK_TEXT, "登录")
# 搜索框
search_input = (By.ID, "q")
# 搜索按钮
search_btn = (By.CSS_SELECTOR, "[type='submit']")
# 购物车
my_cart = (By.ID, "hd-my-cart")




"""-----------------------------------------home_page_element------------------------------------------"""

my_shop = (By.LINK_TEXT, "我的商城")
logout = (By.XPATH, "//div/a[2][@target='_self']")


