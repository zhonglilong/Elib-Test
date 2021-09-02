# -*- coding:utf-8 -*-
import time

from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element

ele = Element('base')


# 运营-荐购设置
class RecommendSet(BasePage):
    def model(self):
        """ 点击运营模块 """
        self.click_btn(path='模块', param='运营')

    def menu(self):
        """ 点击菜单: 书库维护 """
        self.click_btn(path='菜单', param='书库维护')

    def sub_menu(self):
        """ 点击子菜单: 荐购设置"""
        self.click_btn(path='子菜单', param=[1, '荐购设置'])

    def order(self):
        """ 获取荐购设置数量
        获取到trs（有数据时）返回数据的数量，没有获取到（没数据时）返回0
        :return: number
        """
        try:
            trs = self.find_els((By.XPATH, ele['表格数据']))
            return len(trs) / 2
        except:
            return 0

    def double_click_order(self):
        """ 双击数据 """
        if self.order() > 0:
            value = ele['表格数据'] + "[" + str(self.order()) + "]/td[4]"
            self.chains().double_click(self.find_el((By.XPATH, value))).perform()

    def click_filter_list(self, name, cont):
        """ 获取单选列表，点击单选列表输入查询的值并点击 """
        # 定位筛选项，根据传入的名字点击
        # value = ele['筛选项'].format(["1", cont])
        # self.click_input((By.XPATH, value), name)
        self.input_text(path=ele['筛选项'], param=["1", cont], content=name, itype="clickinput")
        self.chains().click(self.find_el((By.XPATH, ele['筛选-单选列表'].format(name)))).perform()

    def click_select_list(self, name):
        """ 点击按钮，选择选项 """
        # 定位筛选项，根据传入的名字点击
        self.chains().click(self.find_el((By.XPATH, ele['表格第一条数据操作列']))).perform()
        value = ele['操作列选项'].format(name)
        self.chains().click(self.find_el((By.XPATH, value))).perform()

    def side_click_filter_list(self, name, value):
        """ 获取侧边栏选项框，点击单选列表输入查询的值并点击 """
        # 定位筛选项，根据传入的名字点击
        # self.click_input((By.XPATH, ele['新增/编辑-输入'].format(name)), value)
        self.input_text(path=ele['新增/编辑-输入'], param=name, content=value, itype="clickinput")
        self.chains().click(self.find_el((By.XPATH, ele['筛选-单选列表'].format(value)))).perform()

    def side_clicks_filter_list(self, name, value):
        """ 获取侧边栏选项框，点击复选列表输入查询的值并点击 """
        # 定位筛选项，根据传入的名字点击
        for i in value:
            # self.click_input((By.XPATH, ele['新增/编辑-输入'].format(name) + '//div[@class="el-select__tags"]'), i)
            self.input_text(path=ele['新增/编辑-输入'] + '//div[@class="el-select__tags"]', param=name, content=i, itype="clickinput")
            time.sleep(2)
            self.chains().click(self.find_el((By.XPATH, ele['筛选-单选列表'].format(i)))).perform()
            time.sleep(2)

    def side_click_filter_button(self, name, value):
        """ 获取侧边栏单选按钮，通过传入的值进行选择点击 """
        # 定位筛选项，根据传入的名字点击
        self.chains().click(self.find_el((By.XPATH, ele['单选新增/编辑-按钮'].format(name, value)))).perform()
