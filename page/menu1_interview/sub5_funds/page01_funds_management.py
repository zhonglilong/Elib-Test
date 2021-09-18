# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element

ele = Element('base')


# 采访--资金管理页面
class FundsManagementPage(BasePage):

    def model(self):
        """ 点击采访模块 """
        self.click_btn(path='模块', param='采访')

    def menu(self):
        """ 点击菜单: 采访统计 """
        self.click_btn(path='菜单', param='资金管理')

    def sub_menu(self):
        """ 点击子菜单: """
        self.click_btn(path='子菜单', param=[5, '资金管理'])

    def order(self):
        """ 获取预订分类统计数据
        获取到trs（有数据时）返回数据的数量，没有获取到（没数据时）返回0
        :return: number
        """
        try:
            trs = self.find_els((By.XPATH, ele['表格数据']))
            return len(trs) / 2
        except:
            print("此列表暂无数据")
            return 0

    def click_filter_list(self, num, name):
        """ 获取单选列表，点击单选列表第一个值 """
        # 点击筛选列表，弹出筛选项
        self.click_btn(path='筛选项', param=["1", num])
        # 定位筛选项，根据传入的名字点击
        self.click_btn(path='筛选-单选列表', param=name)

    def double_click_order(self):
        """ 双击数据 """
        if self.order() > 0:
            self.click_btn(path='采访-表格数据', param=self.order(), ctype="clicks")

    def input_filter_date(self, start, end):
        """ 获取 开始日期 和 结束日期，输入值
        :param start: 开始日期
        :param end: 结束日期
        """
        self.input_text(path='筛选-输入框', param='起始日期', content=start)
        self.input_text(path='筛选-输入框', param='结束日期', content=end)
