
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element
import utils.ocr_utils as ocr

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

    def account_status_of_judge(self):
        """判断账号是否在被使用"""
        if self.pop_window_to_judge():
            self.click_btn(path='确定按钮')

    def verify_name(self):
        return self.text((By.XPATH, ele['操作员名称']))

    def input_ocr(self):
        if self.check_element((By.XPATH, ele['验证码']), atype="img") is True:
            self.screenshot("full_img.png", (By.XPATH, "//*[@placeholder='验证码']/following-sibling::span/span/img"))
            return self.input_text(ele['验证码'], ocr.picture_to_text())
