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

# 采访-征图书验收处理-预订验收
class BookingAcceptancePage(BasePage):

    def model(self):
        """ 点击采访模块 """
        self.click_btn(path='模块', param='采访')

    def menu(self):
        """ 点击菜单: 图书验收处理 """
        self.click_btn(path='菜单', param='图书验收处理')

    def sub_menu(self):
        """ 点击子菜单: 预订验收"""
        self.click_btn(path='子菜单', param=[2, '预订验收'])

    def order(self):
        """ 获取预订书目信息数量
        获取到trs（有数据时）返回数据的数量，没有获取到（没数据时）返回0
        :return: number
        """
        try:
            trs = self.find_els((By.XPATH, ele['表格数据']))
            return len(trs)
        except: return 0

    def click_filter_list(self, name):
        """ 获取预订单单选列表，点击预订单列表其中的预订单名称 """
        # 点击筛选列表，弹出筛选项
        self.click_btn(path='筛选项', param=["1", "1"])
        # 定位筛选项，根据传入的名字点击
        # value = ele['筛选-单选列表'].format(name)
        self.click_btn(path='筛选-单选列表', param=name)

    def click_filter_lists(self, num, name):
        """ 获取单选列表，点击单选列表指定的值
        :param num: 定位筛选项
        :param name: 选择的馆名 / 状态 / 图书信息
        """
        self.input_text(path='筛选项', param=["1", num], content=name, itype="clickinput")
        time.sleep(1)
        self.chains().click(self.find_el((By.XPATH, ele['筛选-单选列表'].format(name)))).perform()

    def click_filter_input(self, param, content):
        """ 获取输入框，输入值进行搜索 """
        self.input_text(path='筛选-输入框', param=param, content=content, itype="clearinput")

    def check_order(self):
        """ 勾选书目信息 """
        if self.order() > 0:
            # value = ele['表格数据'] + "[" + str(self.order()) + "]/td[1]/div/label"
            self.click_btn(path='采访-表格数据勾选', param=self.order())

    def click_check_accept(self):
        """ 批量验收 """
        # 点击批量验收
        self.click_btn(path='右上按钮', param="1")
        # 点击弹窗确定按钮
        self.click_btn(path='验收确定/取消', param="验收")

    def click_all_accept(self):
        """ 全部验收 """
        if self.order() > 0:
            # 点击全部验收
            self.click_btn(path='右上按钮', param="2")
            # 点击弹窗确定按钮
            self.click_btn(path='验收确定/取消', param="验收")

    def click_simple_template(self):
        """ 查看简单模板 """
        # 点击编目按钮
        self.click_btn(path='右上按钮', param="3")
        # 点击简单编目模板
        self.click_btn(path='编目-简单模板/MARC编目', param="1")

    def click_marc_catalog(self):
        """ 查看MARC编目 """
        self.click_btn(path='右上按钮', param="3")
        # 点击MARC编目
        self.click_btn(path='编目-简单模板/MARC编目', param="2")