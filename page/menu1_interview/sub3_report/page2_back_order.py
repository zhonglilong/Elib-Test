# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element
import logging

ele = Element('base')


# 采访-预订单页面
class BackOrderPage(BasePage):

    def model(self):
        """ 点击采访模块 """
        self.click_btn(path='模块', param='采访')

    def menu(self):
        """ 点击菜单: 采访报表 """
        self.click_btn(path='菜单', param='采访报表')

    def sub_menu(self):
        """ 点击子菜单: 预订单"""
        self.click_btn(path='子菜单', param=[3, '退订单'])

    def order(self):
        """ 获取退订单数量
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

    def input_filter_date(self, start, end):
        """ 获取 开始日期 和 结束日期，输入值
        :param start: 开始日期
        :param end: 结束日期
        """
        self.input_text(path='筛选-输入框', param='开始日期', content=start)
        self.input_text(path='筛选-输入框', param='结束日期', content=end)

    def click_close_all(self, text, num):
        """
        获取复选项框内已选项的叉
        """
        self.click_btn(path='已选项叉', param=[text, num])



