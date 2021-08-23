# -*- coding:utf-8 -*-
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