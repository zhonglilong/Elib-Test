# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element
import time

ele = Element('base')


# 运营-订购处理
class OrderProcessPage(BasePage):

    def model(self):
        """ 点击运营模块 """
        self.click_btn(path='模块', param='运营')

    def menu(self):
        """ 点击菜单: 订购出库 """
        self.click_btn(path='菜单', param='订购出库')

    def sub_menu(self):
        """ 点击子菜单: 订购处理"""
        self.click_btn(path='子菜单', param=[8, '订购处理'])

    def click_filter_list(self, num, name):
        """ 获取单选列表，点击单选列表指定的值
        :param num: 定位筛选项
        :param name: 选择的馆名 / 状态 / 图书信息
        """
        self.input_text(path='筛选项', param=["1", num], content=name, itype="clickinput")
        time.sleep(1)
        self.click_btn(path='筛选-单选列表', param=name)
        # self.chains().click(self.find_el((By.XPATH, ele['筛选-单选列表'].format(name)))).perform()

    def click_filter_input(self, param, content):
        """ 获取输入框，输入值进行搜索 """
        self.input_text(path='筛选-输入框', param=param, content=content, itype="clearinput")

    def click_filter_date(self, param, content):
        """ 获取输入框，输入值进行搜索 """
        self.input_text(path='筛选-输入框', param=param, content=content)