# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from base.base_element import Element

ele = Element('base')

# 页面基类
class BasePage(BaseAction):

    def click_model(self, name):
        """ 点击模块
        :param name :模块名称（如采访、编目...）
        :return: element
        """
        value = ele['模块'].format(name)
        return self.click((By.XPATH, value))

    def click_menu(self, name):
        """ 点击菜单
        :param name :菜单名称（如文献编目、文献移送...）
        :return: element
        """
        value = ele['菜单'].format(name)
        return self.click((By.XPATH, value))

    def click_sub_menu(self, num, name):
        """ 点击子菜单
        :param num :排序（从上往下处于第几个菜单，如1,2,3...）
        :param name :子菜单名称（如回溯建库...）
        :return: element
        """
        value = ele['子菜单'].format(num, name)
        return self.click((By.XPATH, value))

    def click_sub_menu_btn(self, name):
        """ 点击查询按钮（进F12定位看，有些相同按钮有空格）
        :param name: 按钮文本
        :return: element
        """
        value = ele['查询按钮'].format(name)
        return self.click((By.XPATH, value))

    def sub_menu_alert(self):
        """ 判断是否有提示框
        :return: True or False
        """
        return self.isElementPresent((By.XPATH, ele['提示框']))