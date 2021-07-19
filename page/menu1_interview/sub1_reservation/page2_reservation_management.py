# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element

ele = Element('base')

# 采访-预订单管理
class ReservationManagementPage(BasePage):

    def model(self):
        """ 点击采访模块 """
        self.click_btn(path='模块', param='采访')

    def menu(self):
        """ 点击菜单: 图书预订处理 """
        self.click_btn(path='菜单', param='图书预订处理')

    def sub_menu(self):
        """ 点击子菜单: 预订单管理 """
        self.click_btn(path='子菜单', param=[1, '预订单管理'])

    def click_filter_list(self, name):
        """ 获取单选列表，根据传入的名字点击对应单选列表 """
        # 点击筛选列表，弹出筛选项
        self.click_btn(path='筛选项', param='1')
        # 定位筛选项，获取筛选项数量，点击传入的名字
        value = ele['筛选-单选列表'].format(name)
        self.click((By.XPATH, value))

    def input_filter_date(self, start, end):
        """ 获取 开始日期 和 结束日期，输入值
        :param start: 开始日期
        :param end: 结束日期
        """
        self.input_text(path='筛选-输入框', param='开始日期', content=start)
        self.input_text(path='筛选-输入框', param='结束日期', content=end)