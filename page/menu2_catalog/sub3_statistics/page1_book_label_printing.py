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
from utils.common_utils import check_param

ele = Element('base')

class BookLabelPrintingPage(BasePage):
    def model(self):
        """ 点击采访模块 """
        self.click_btn(path='模块', param='编目')

    def menu(self):
        """ 点击菜单: 编目统计 """
        self.click_btn(path='菜单', param='编目统计')

    def sub_menu(self):
        """ 点击子菜单: 书标打印"""
        self.click_btn(path='子菜单', param=[3, '书标打印'])

    def order(self):
        """ 获取书籍数量
        获取到trs（有数据时）返回数据的数量，没有获取到（没数据时）返回0
        :return: number
        """
        try:
            trs = self.find_els((By.XPATH, ele['表格数据']))
            return len(trs) / 2
        except: return 0

    def click_filter_input(self, path, param, content):
        """ 获取输入框，输入值进行搜索 """
        self.input_text(path=path, param=param, content=content, itype="clickinputs")

    def check_state_param(self, path, param):
        '''通过确认查询出的数据的目标列的值，确认是否搜索正确。'''
        return self.choose_target_title((By.XPATH, check_param(path=path, param=param)))

    def input_bar_code(self, path, param, content):
        """ 输入条形码的起始值和结束值 """
        self.input_text(path=path, param=param, content=content, itype="clickinputs")
        self.input_text(path=path, param=param, content=content, itype="clickinputs")

    def click_operator_list(self, num, name):
        """ 获取单选列表，点击单选列表指定的值
        :param num: 定位筛选项
        :param name: 选择的操作人
        """
        self.input_text(path='筛选项', param=["2", num], content=name, itype="clickinput")
        time.sleep(1)
        self.chains().click(self.find_el((By.XPATH, ele['筛选-单选列表'].format(name)))).perform()

    def check_pop_up_window(self, path, param):
        '''
        根据弹出的新窗口的标题判断
        :return:
        '''
        return self.check_element((
            By.XPATH, check_param(path=path, param=param)
        ), atype='dialog')
