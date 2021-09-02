# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element
import logging

ele = Element('base')


# 采访-征订目录预订
class DirectoryReservationPage(BasePage):

    def model(self):
        """ 点击采访模块 """
        self.click_btn(path='模块', param='采访')

    def menu(self):
        """ 点击菜单: 图书预订处理 """
        self.click_btn(path='菜单', param='图书预订管理')

    def sub_menu(self):
        """ 点击子菜单: 征订目录预订"""
        self.click_btn(path='子菜单', param=[1, '征订书目预订'])

    def order(self):
        """ 获取征订目录数量
        获取到trs（有数据时）返回数据的数量，没有获取到（没数据时）返回0
        :return: number
        """
        try:
            trs = self.find_els((By.XPATH, ele['表格数据']))
            return len(trs) / 2
        except: return 0

    def check_order(self):
        """ 勾选数据 """
        if self.order() > 0:
            # value = ele['表格数据'] + "[" + str(self.order()) + "]/td[1]/div/label"
            self.click_btn(path='采访-表格数据勾选', param=self.order())

    def click_order_link(self):
        """ 点击详情链接 """
        if self.order() > 0:
            # value = ele['表格数据'] + "[" + str(self.order()) + "]/td[3]/div/span"
            self.click_btn(path='采访-表格数据链接', param=self.order())

    def double_click_order(self):
        """ 双击数据 """
        if self.order() > 0:
            # value = ele['表格数据'] + "[" + str(self.order()) + "]/td[4]"
            self.click_btn(path='采访-表格数据', param=self.order(), ctype="clicks")
            # self.chains().double_click(self.find_el((By.XPATH, value))).perform()

    def click_filter_list(self, name):
        """ 获取单选列表，点击单选列表最后一个值 """
        # 点击筛选列表，弹出筛选项
        self.click_btn(path='筛选项', param=["1", "1"])
        # 定位筛选项，根据传入的名字点击
        # value = ele['筛选-单选列表'].format(name)
        self.click_btn(path='筛选-单选列表', param=name)

    def input_filter_date(self, start, end):
        """ 获取 开始日期 和 结束日期，输入值
        :param start: 开始日期
        :param end: 结束日期
        """
        self.input_text(path='筛选-输入框', param='开始日期', content=start)
        self.input_text(path='筛选-输入框', param='结束日期', content=end)

    def click_filter_input(self, name):
        """ 获取 征订目录 输入框，输入值
        :param name: 查询的征订目录名称
        """
        self.input_text(path='筛选-输入框', param='请输入征订目录', content=name)
