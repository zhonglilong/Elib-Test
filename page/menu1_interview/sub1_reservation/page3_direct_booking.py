#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element
import time
from base.base_action import BaseAction
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
import requests

ele = Element('base')

class DirectBookingPage(BasePage):
    def model(self):
        """ 点击采访模块 """
        self.click_btn(path='模块', param='采访')

    def menu(self):
        """ 点击菜单: 图书预订处理 """
        self.click_btn(path='菜单', param='图书预订处理')

    def sub_menu(self):
        """ 点击子菜单: 直接预订"""
        self.click_btn(path='子菜单', param=[1, '直接预订'])

    def order(self):
        """ 获取预订单数量
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
            self.click_btn(path='采访-表格数据勾选', param='1')    #参数为1，就是设置删除顺序第一行数据

    def check_below_delete_order(self):
        """ 勾选数据 """
        if self.order() > 0:
            # value = ele['表格数据'] + "[" + str(self.order()) + "]/td[1]/div/label"
            self.click_btn(path='定位表格的操作列',ctype='click')

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

    def double_click_target_order(self,path,param,ctype):
        '''双击目标数据'''
        if self.order() > 0:
            self.click_btn(path=path,param=param,ctype=ctype)

    def click_filter_list(self, name):
        """ 获取单选列表，点击单选列表最后一个值 """
        # 点击筛选列表，弹出筛选项
        self.click_btn(path='筛选项', param=["1", "1"])
        # 定位筛选项，根据传入的名字点击
        # value = ele['筛选-单选列表'].format(name)
        self.click_btn(path='筛选-单选列表', param=name)

    def click_filter_firstlist(self, num, name):
        """ 获取单选列表，点击单选列表指定的值
        :param num: 定位筛选项
        :param name: 选择的馆名 / 状态 / 图书信息
        """
        self.input_text(path='筛选项', param=["1", num], content=name, itype="clickinput")
        time.sleep(1)
        self.chains().click(self.find_el((By.XPATH, ele['筛选-单选列表'].format(name)))).perform()

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

    def click_filter_firstinput(self, param, content):
        """ 获取输入框，输入值进行搜索 """
        self.input_text(path='筛选-输入框', param=param, content=content, itype="clickinputs")

    def click_select_list(self, name):
        """ 点击按钮，选择选项 """
        # 定位筛选项，根据传入的名字点击
        self.chains().click(self.find_el((By.XPATH, ele['表格第一条数据操作列']))).perform()
        value = ele['操作列选项'].format(name)
        self.chains().click(self.find_el((By.XPATH, value))).perform()

    def verify_button_status(self,path,label):
        '''获取设为工设为默认参数按钮属性'''
        return self.css_status((By.XPATH, ele[path]), label)


