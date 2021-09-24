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


class TransferProcessingPage(BasePage):
    def model(self):
        """ 点击采访模块 """
        self.click_btn(path='模块', param='编目')

    def menu(self):
        """ 点击菜单: 文献移送 """
        self.click_btn(path='菜单', param='文献移送')

    def sub_menu(self):
        """ 点击子菜单: 移送处理"""
        self.click_btn(path='子菜单', param=[2, '移送处理'])

    def order(self):
        """ 获取移送图书数量
        获取到trs（有数据时）返回数据的数量，没有获取到（没数据时）返回0
        :return: number
        """
        try:
            trs = self.find_els((By.XPATH, ele['表格数据']))
            return len(trs) / 2
        except:
            return 0

    def click_filter_firstlist(self, num, name):
        """ 获取单选列表，点击单选列表指定的值
        :param num: 定位筛选项
        :param name: 选择的馆名 / 状态 / 图书信息
        """
        self.input_text(path='筛选项', param=["1", num], content=name, itype="clickinput")
        time.sleep(1)
        self.chains().click(self.find_el((By.XPATH, ele['筛选-单选列表'].format(name)))).perform()

    def click_filter_firstinput(self, param, content):
        """ 获取输入框，输入值进行搜索 """
        self.input_text(path='筛选-输入框', param=param, content=content, itype="clickinputs")

    def check_state_param(self, path, param):
        '''有参的找已交送列名'''
        target_name = ele[path].format(param)
        return self.choose_target_title((By.XPATH, target_name))


