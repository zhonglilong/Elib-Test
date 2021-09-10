# -*- coding:utf-8 -*-
import time
import random

from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element

ele = Element('base')


# 运营-荐购设置
class RecommendSet(BasePage):

    def login(self):
        """ 仅用于单列执行时应对登录 """
        if self.find_els((By.XPATH, ele['登录密码'])):
            self.input_text(path='登录用户名', content="autotest")
            self.input_text(path='登录密码', content="Td123456")
            self.click_btn(path='登录按钮')

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
        self.input_text(path='筛选项', param=["1", cont], content=name, itype="clickinput")
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
        self.input_text(path='新增/编辑-输入', param=name, content=value, itype="clickinput")
        self.chains().click(self.find_el((By.XPATH, ele['筛选-单选列表'].format(value)))).perform()

    def side_clicks_filter_list(self, name, value):
        """ 获取侧边栏选项框，点击复选列表输入查询的值并点击 """
        # 定位筛选项，根据传入的名字点击
        for i in value:
            # self.click_input((By.XPATH, ele['新增/编辑-输入'].format(name) + '//div[@class="el-select__tags"]'), i)
            self.input_text(path='运营-新增/编辑-输入', param=name, content=i, itype="clickinput")
            time.sleep(2)
            self.chains().click(self.find_el((By.XPATH, ele['筛选-单选列表'].format(i)))).perform()
            time.sleep(2)

    def side_click_filter_button(self, name, value):
        """ 获取侧边栏单选按钮，通过传入的值进行选择点击 """
        # 定位筛选项，根据传入的名字点击
        self.chains().click(self.find_el((By.XPATH, ele['新增/编辑-单选按钮'].format(name, value)))).perform()

    def select_data(self, import1, import2):
        """  查询数据 """
        if import1 == import2:
            self.click_btn(path='查询按钮', param='查询')
        elif isinstance(import1, list):
            for i, j in import1, import2:
                self.click_filter_list(name=i, cont=j)
            self.click_btn(path='查询按钮', param='查询')
        else:
            self.click_filter_list(name=import1, cont=import2)
            self.click_btn(path='查询按钮', param='查询')
        assert self.sub_menu_alert()

    def data_configuration(self, id, userd, tableName):
        """  新增数据 """
        if isinstance(id, list):
            self.click_btn(path='复选框叉', param='成员馆')
            self.side_clicks_filter_list(name='成员馆', value=id)
        else:
            self.click_btn(path='复选框叉', param='成员馆')
            self.side_click_filter_list(name='成员馆', value=id)
        self.side_click_filter_button(name='是否启用', value=userd)
        self.side_click_filter_list(name='书库名称', value=tableName)
        self.click_btn(path='侧边弹窗底部按钮', param='保存')
        if isinstance(id, list):
            self.select_data(id[0], '1')
        else:
            self.select_data(id, '1')
        assert self.sub_menu_alert() and self.order()

    def data_update(self, id, newid, userd, tableName):
        """  编辑数据 """
        self.click_filter_list(name=id, cont='1')
        self.click_btn(path='查询按钮', param='查询')
        time.sleep(1)
        if random.choice([1, 0]) == 1:
            self.click_btn(path='表格第一条数据', ctype="clicks")
        else:
            self.click_select_list(name='编辑')
        self.click_btn(path='复选框叉', param='成员馆')
        time.sleep(2)
        if isinstance(newid, list):
            self.side_clicks_filter_list(name='成员馆', value=newid)
        else:
            self.side_click_filter_list(name='成员馆', value=newid)
        self.side_click_filter_button(name='是否启用', value=userd)
        self.side_click_filter_list(name='书库名称', value=tableName)
        self.click_btn(path='侧边弹窗底部按钮', param='保存', ctype='click')
        self.click_filter_list(name=id, cont='1')
        self.click_btn(path='查询按钮', param='查询')
        assert self.sub_menu_alert() and self.order()

    def data_del(self, id):
        time.sleep(2)
        self.click_filter_list(name=id, cont='1')
        self.click_btn(path='查询按钮', param='查询')
        time.sleep(1)
        self.click_select_list(name='删除')
        assert self.pop_window_to_judge()
        self.click_btn(path='删除确定/取消', param='1')
        time.sleep(1)
        self.click_btn(path='右上按钮', param='2')
        self.click_btn(path='删除确定/取消', param='2')
        self.click_btn(path='查询按钮', param='查询')
        assert self.sub_menu_alert() and self.order() == 0