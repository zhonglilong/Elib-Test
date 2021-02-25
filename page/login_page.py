from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from base.base_element import Element

ele = Element('base')

# 登录页面
class LoginPage(BaseAction):

    # 输入用户名
    def input_username(self, content):
        return self.input((By.XPATH, ele['登录用户名']), content)

    # 输入密码
    def input_password(self, content):
        return self.input((By.XPATH, ele['登录密码']), content)

    # 点击登录按钮
    def click_login_btn(self):
        return self.click((By.XPATH, ele['登录按钮']))

    # 点击编目按钮
    def click_bm_btn(self):
        value = ele['模块'].format("编目")
        return self.click((By.XPATH, value))

    # 点击文献编目按钮
    def click_wxbm_btn(self):
        value = ele['菜单'].format("文献编目")
        return self.click((By.XPATH, value))

    # 点击编目管理按钮
    def click_bmgl_btn(self):
        value = ele['子菜单'].format(1, "编目管理")
        return self.click((By.XPATH, value))

    # 点击查询按钮
    def click_query_btn(self):
        value = ele['查询按钮'].format(" 查询 ")
        return self.click((By.XPATH, value))

    # 获取查询结果
    def get_sub_menu_alert(self):
        return self.isElementPresent((By.XPATH, ele['提示框']))