# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from base.base_element import Element

ele = Element('base')


# 特色--资源分类 页面
class ResourceClassifyPage(BasePage):

    def model(self):
        """ 点击特色模块 """
        self.click_btn(path='模块', param='特色')

    def menu(self):
        """ 点击菜单: 资源管理 """
        self.click_btn(path='菜单', param='资源管理')

    def sub_menu(self):
        """ 点击子菜单: 资源分类"""
        self.click_btn(path='子菜单', param=[4, '资源分类'])

    def order(self):
        """ 获取预订单数量
        获取到trs（有数据时）返回数据的数量，没有获取到（没数据时）返回0
        :return: number
        """
        try:
            trs = self.find_els((By.XPATH, ele['表格数据']))
            return len(trs) / 2
        except:
            print("此列表暂无数据")
            return 0

    def click_filter_input(self, data):
        """ 获取 征订目录 输入框，输入值
        :param name: 查询的征订目录名称
        """
        self.input_text(path='筛选-输入框', param='请输入', content=data)
