# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element
from utils.common_utils import check_param
import logging, time

ele = Element('base')


# 编目-编目管理
class CatalogingManagementPage(BasePage):

    def model(self):
        """ 点击编目模块 """
        self.click_btn(path='模块', param='编目')

    def menu(self):
        """ 点击菜单: 文献编目 """
        self.click_btn(path='菜单', param='文献编目')

    def sub_menu(self):
        """ 点击子菜单: 编目管理"""
        self.click_btn(path='子菜单', param=[1, '编目管理'])

    def click_filter_list(self, num, name):
        """ 获取单选列表，点击单选列表指定的值
        :param num: 定位筛选项
        :param name: 选择的馆名 / 状态 / 图书信息
        """
        self.input_text(path='编目-筛选项', param=num, content=name, itype="clickinput")
        time.sleep(1)
        self.click_btn(path='筛选-单选列表', param=name)

    def verify_filter(self, num, label):
        """ 验证 成员馆 的值获取的是否正确，需要点击一下，焦点在单选列表上 placeholder 属性的值才会改变
        :param label: 需要获取值的元素
        :param num: 定位筛选项
        :return: 返回获取元素的值
        """
        self.click_btn(path='编目-筛选项', param=num)
        time.sleep(1)
        return self.output_text(path='编目-筛选项输入框', param=num, label=label, otype='attribute')

    def click_filter_input(self, param, content):
        """ 获取输入框，输入值进行搜索 """
        self.input_text(path='筛选-输入框', param=param, content=content, itype="clearinput")

    def click_filter_inputs(self):
        """ 获取多个输入框 """
        return self.find_els((By.XPATH, check_param(path='筛选-输入框', param='请输入搜索关键词')))

    def verify_filter_num(self, num):
        """ 获取筛选项的数量 """
        return len(self.find_els((By.XPATH, check_param(path='编目-筛选项数量', param=num))))

    def add_or_remove_filter(self, otype):
        if otype == "add":
            self.click_btn(path='编目-加减筛选项按钮', param='el-icon-circle-plus')
        elif otype == "remove":
            self.click_btn(path='编目-加减筛选项按钮', param='el-icon-remove')

    def verify_filter_items(self):
        if self.output_text(path='筛选项', param=['1', '5']) == '更多筛选':
            self.click_btn(path='筛选项', param=['1', '5'])
            time.sleep(1)

    def verify_checkbox(self, param):
        return self.select((By.XPATH, check_param(path='编目-勾选框', param=param)))

    def verify_staff(self):
        ele_list = list()
        elements = self.find_els((By.XPATH, check_param(path='编目-表格-创建人')))
        for element in elements:
            ele_list.append(element.text)
        return ele_list

    # def verify_filter_display(self, path, param=None):
    #     return self.display((By.XPATH, check_param(path=path, param=param)))