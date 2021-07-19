from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element

ele = Element('base')

# 登录页面
class LoginPage(BasePage):

    def input_username(self, content):
        """ 输入用户名 """
        return self.input_text(path='登录用户名', content=content)

    def input_password(self, content):
        """ 输入密码 """
        return self.input_text(path='登录密码', content=content)

    def click_login_btn(self):
        """ 点击登录按钮 """
        self.click_btn(path='登录按钮')

    def verify_name(self, name):
        """ 验证操作员名称与config中的VERIFY值是否相等
        :param name :右上角的管理员名称
        :return: True or False
        """
        if self.text((By.XPATH, ele['操作员名称'])) == name:
            return True
        return False
