# C:/test1
# -*- coding: utf-8 -*-
# @time : 
# Author : 小白
import time
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element
from utils.time_utils import TimeUtils

ele = Element('base')

# 采访-征图书验收处理-验收单管理
class ReceivingReportPage(BasePage):

    def model(self):
        """ 点击采访模块 """
        self.click_btn(path='模块', param='采访')

    def menu(self):
        """ 点击菜单: 图书验收处理 """
        self.click_btn(path='菜单', param='图书验收处理')

    def sub_menu(self):
        """ 点击子菜单: 验收单"""
        self.click_btn(path='子菜单', param=[2, '验收单管理'])

    def order(self):
        """ 获取验收单数量
        获取到trs（有数据时）返回数据的数量，没有获取到（没数据时）返回0
        :return: number
        """
        try:
            trs = self.find_els((By.XPATH, ele['表格数据']))
            return len(trs) / 2
        except: return 0

    def check_order(self):
        """ 勾选验收单 """
        if self.order() > 0:
            # value = ele['表格数据'] + "[" + str(self.order()) + "]/td[1]/div/label"
            self.click_btn(path='采访-表格数据勾选', param=self.order())

    def click_filter_list(self, name):
        """获取单选列表，点击单选列表最后一个值"""
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

    def click_filter_input(self, param, content):
        """ 获取输入框，输入值进行搜索 """
        self.input_text(path='筛选-输入框', param=param, content=content, itype="clearinput")

    def click_filter_date(self, param, content):
        """ 获取输入框，输入值进行搜索 """
        self.input_text(path='筛选-输入框', param=param, content=content)

    def click_filter_lists(self, num, name):
        """ 获取单选列表，点击单选列表指定的值
        :param num: 定位筛选项
        :param name: 选择的馆名 / 状态 / 图书信息

        """
        self.input_text(path='筛选项', param=["1", num], content=name, itype="clickinput")
        time.sleep(1)
        self.chains().click(self.find_el((By.XPATH, ele['筛选-单选列表'].format(name)))).perform()

    def double_click_order(self):
        """ 双击数据 """
        if self.order() > 0:
            # value = ele['表格数据'] + "[" + str(self.order()) + "]/td[4]"
            self.click_btn(path='采访-表格数据', param=self.order(), ctype="clicks")
            # self.chains().double_click(self.find_el((By.XPATH, value))).perform()

    def click_receipt_Details(self):
        """点击验收单第一条数据的操作详情按钮"""
        if self.order() > 0:
            TimeUtils().sleep(2)
            self.click_btn(path='查询按钮', param='查询')
            TimeUtils().sleep(2)
            self.click_btn(path='表格第一条数据操作列', ctype='moveClick')
            TimeUtils().sleep(2)
            self.click_btn(path='操作列选项', param='详情')

    def click_compile_Details(self):
        """点击验收单第一条数据的操作编辑按钮"""
        if self.order() > 0:
            TimeUtils().sleep(2)
            self.click_btn(path='查询按钮', param='查询')
            TimeUtils().sleep(2)
            self.click_btn(path='表格第一条数据操作列', ctype='moveClick')
            TimeUtils().sleep(2)
            self.click_btn(path='操作列选项', param='编辑')
