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
from utils.common_utils import check_param

ele = Element('base')

class AdvanceOrderPage(BasePage):
    def model(self):
        """ 点击采访模块 """
        self.click_btn(path='模块', param='采访')

    def menu(self):
        """ 点击菜单: 图书预订处理 """
        self.click_btn(path='菜单', param='图书预订处理')

    def sub_menu(self):
        """ 点击子菜单: 预订单管理"""
        self.click_btn(path='子菜单', param=[1, '预订单管理'])

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

    def click_filter_input(self, path, param, content):
        """ 获取输入框，输入值进行搜索 """
        self.input_text(path=path, param=param, content=content, itype="clickinputs")

    def check_state_param(self, path, param):
        '''通过确认查询出的数据的目标列的值，确认是否搜索正确。'''
        return self.choose_target_title((By.XPATH, check_param(path=path, param=param)))

    def click_select_list(self, name):
        """ 点击按钮，选择选项 """
        # 定位筛选项，根据传入的名字点击
        self.chains().click(self.find_el((By.XPATH, ele['表格第一条数据操作列']))).perform()
        value = ele['操作列选项'].format(name)
        self.chains().click(self.find_el((By.XPATH, value))).perform()

    def total_form_exist_columns(self):
        '''定位标题头，返回列数'''
        return self.total_form_columns((By.XPATH, ele['表格标题头']))

    def judge_by_url_and_status_code(self, param):
        '''获取目标url的状态码'''
        target_url = requests.get(param)
        return target_url.status_code == 200

    def find_order_name_param(self,path,param):
        '''有参的找标题名'''
        target_name = ele[path].format(param)
        return self.choose_target_title((By.XPATH,target_name))

    def find_order_name(self,path):
        '''无参的找标题名'''
        return self.choose_target_title((By.XPATH,ele[path]))

    def verify_order_status(self, path, param, label):
        '''获取设为工作预订单列class属性'''
        target_row = ele[path].format(param)
        return self.css_status((By.XPATH, target_row),label)


