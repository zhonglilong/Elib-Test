# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element
from base.log_config import Logging

ele = Element('base')

# 采访-征订目录预订
class DirectoryReservationPage(BasePage):

    def click_sub_menu_list(self, num):
        """ 点击详情链接
        :param num: 链接所处列数
        :return:
        """
        value = ele['征订目录-详情页面'].format(num)
        self.click((By.XPATH, value))

    def click_sub_menu_filter(self, num):
        """ 点击筛选项
        :param num: 根据xpath获取当前页面所有筛选项，所需点击div排第几就填几
        :return:
        """
        value = ele['筛选项'].format(num)
        self.click((By.XPATH, value))

    def click_sub_menu_filter_list(self):
        """ 获取单选列表，点击单选列表最后一个值
        :return:
        """
        value = ele['筛选-单选列表']
        lis = self.find_els((By.XPATH, value))
        value2 = ele['筛选-单选列表']+"["+str(len(lis))+"]/span"
        self.click((By.XPATH, value2))

    def input_sub_menu_filter_date(self, start, end):
        """ 获取 开始日期 和 结束日期，输入值
        :param start: 开始日期
        :param end: 结束日期
        :return:
        """
        value = ele['筛选-开始日期']
        value2 = ele['筛选-结束日期']
        self.input((By.XPATH, value), start)
        self.input((By.XPATH, value2), end)

    def click_sub_menu_filter_input(self, name):
        """ 获取 征订目录 输入框，输入值
        :param name: 查询的征订目录名称
        :return:
        """
        value = ele['筛选-征订目录']
        self.input((By.XPATH, value), name)

    def click_sub_menu_add_btn(self):
        pass