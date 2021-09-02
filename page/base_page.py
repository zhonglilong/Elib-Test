# -*- coding:utf-8 -*-
import logging

from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from base.base_element import Element
from utils.time_utils import TimeUtils

ele = Element('base')


# 页面基类
class BasePage(BaseAction):

    def input_text(self, path, content, param=None, itype="input"):
        """ 输入框输入值
        :param path: 传递 yaml文件中的 xpath名称
        :param param: 传递 xpath 参数（可以为None，str，list）
        :param content: 传递字符串，输入的内容
        :param itype: 传递字符串，区分输入类型，默认为input，分为
            直接输入（input）、单击后输入（clickinput）、双击后输入（clickinputs）、清除后输入（clearinput）
        """
        # 判断 param 不为空
        if param is not None:
            # 判断传过来的是不是个list
            if isinstance(param, list):
                value = ele[path].format(*param)
            else:
                value = ele[path].format(str(param))
        else:
            value = ele[path]
        self.input((By.XPATH, value), content=content, itype=itype)

    def click_btn(self, path, param=None, ctype="click"):
        """ 点击按钮
        :param path: yaml文件中的 xpath名称
        :param param: xpath 参数（可以是str，list）
        :param ctype:传递字符串，区分点击类型，默认单击，分为单击（click）和双击（clicks）
        :return: self
        """
        # 判断 param 不为空
        if param is not None:
            # 判断传过来的是不是个list
            if isinstance(param, list):
                value = ele[path].format(*param)
            else:
                value = ele[path].format(str(param))
        else:
            value = ele[path]
        self.click((By.XPATH, value), ctype=ctype)



    # def double_click_btn(self, path, param=None):
    #     """ 双击按钮
    #     :param path: yaml文件中的 xpath名称
    #     :param param: xpath 参数（可以是str，list）
    #     :return:
    #     """
    #     # 判断 param 不为空
    #     if param is not None:
    #         # 判断传过来的是不是个list
    #         if isinstance(param, list):
    #             value = ele[path].format(*param)
    #         else:
    #             value = ele[path].format(str(param))
    #     else:
    #         value = ele[path]
    #     self.clicks((By.XPATH, value))

    def sub_menu_alert(self):
        """ 判断是否有提示框
        :return: True or False
        """
        TimeUtils().sleep(1)
        return self.check_element((By.XPATH, ele['提示框']))

    def pop_window_to_judge(self):
        """ 判断是否有弹窗
        :return: True or False
        """
        TimeUtils().sleep(1)
        return self.isElementPop((By.XPATH, ele['弹窗']))

    def pop_sidewindow_to_judge(self):
        """ 判断是否有侧边弹窗
        :return: True or False
        """
        TimeUtils().sleep(1)
        return self.check_element((By.XPATH, ele['侧边弹窗']))
