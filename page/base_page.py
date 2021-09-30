# -*- coding:utf-8 -*-
import logging
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from base.base_element import Element
from utils.time_utils import TimeUtils
from utils.common_utils import check_param

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
        if itype == "input":
            return self.input((
                By.XPATH, check_param(path=path, param=param)
            ), content)
        elif itype == "clickinput":
            return self.clickinput((
                By.XPATH, check_param(path=path, param=param)
            ), content)
        elif itype == "clickinputs":
            return self.clickinputs((
                By.XPATH, check_param(path=path, param=param)
            ), content)
        elif itype == "clearinput":
            return self.clearinput((
                By.XPATH, check_param(path=path, param=param)
            ), content)
        else:
            logging.error("No Such input Type：" + itype)

    def click_btn(self, path, param=None, ctype="click"):
        """ 点击按钮
        :param path: yaml文件中的 xpath名称
        :param param: xpath 参数（可以是str，list）
        :param ctype:传递字符串，区分点击类型，默认单击，分为单击（click）和双击（clicks）
        :return: self
        """
        # 判断 param 不为空
        if ctype == "click":
            return self.click((
                By.XPATH, check_param(path=path, param=param)
            ))
        elif ctype == "clicks":
            return self.clicks((
                By.XPATH, check_param(path=path, param=param)
            ))
        elif ctype == "moveclick":
            return self.moveclick((
                By.XPATH, check_param(path=path, param=param)
            ))
        else:
            logging.error("No Such Click Type：" + ctype)

    def output_text(self, path, param=None, label=None, otype="text"):
        """ 输出定位组件的文本
        :param label: 要获取的元素的值
        :param otype: 传递字符串，区分获取文本类型，默认直接获取text，attribute获取元素的值
        :param path: yaml文件中的 xpath名称
        :param param: xpath 参数（可以是str，list）
        :return: 输出获取文本或None
        """
        if otype == "text":
            return self.text((
                By.XPATH, check_param(path=path, param=param)
            ))
        elif otype == "attribute" and label is not None:
            return self.attribute((
                By.XPATH, check_param(path=path, param=param)
            ), label=label)
        else:
            logging.info("请检查参数是否正确")

    def sub_menu_alert(self):
        """ 判断是否有红色提示框，没有返回Ture，有返回false
        :return: True or False
        """
        TimeUtils().sleep(1)
        return self.check_element((By.XPATH, ele['提示框']), atype='redAlert')

    def alert_exist(self, atype):
        """ 判断是否有提示框，有的话输出内容
        :param atype: 要获取的提示框颜色，目前只可以选yellowAlert，greenAlert
        :return: 文本(str)
        """
        TimeUtils().sleep(1)
        if self.check_element((By.XPATH, ele['提示框']), atype=atype):
            return self.output_text(path='提示框文本', otype='text')

    def pop_window_to_judge(self):
        """ 判断是否有弹窗
        :return: True or False
        """
        TimeUtils().sleep(1)
        return self.check_element((By.XPATH, ele['弹窗']), atype='pop')

    def element_exist(self, path, param=None):
        """ 判断element是否存在
        :return: True or False
        """
        TimeUtils().sleep(1)
        return self.check_element((
            By.XPATH, check_param(path=path, param=param)
        ), atype='element')

    def dialog_exist(self, param):
        """ 判断是否有弹窗，用于判断拼音生成多音字选择的弹窗 和 图书推荐
        :return: True or False
        """
        TimeUtils().sleep(1)
        return self.check_element((
            By.XPATH, check_param(path='编目-拼音/推荐/分编弹窗', param=param)
        ), atype='dialog')

    def total_form_columns(self, feature):
        """ 获取表单的列数 """
        return len(self.find_els(feature))

    def choose_target_title(self, feature):
        '''获取名字，表格里面的直接返回，详情里面的处理一下再返回'''
        result_title = self.text(feature)
        special_symbol = '【'
        if special_symbol in result_title:
            return result_title[5:-1]
        else:
            return result_title

    def order_status(self, feature):
        '''获取属性'''
        result = self.element_css_style(feature)
        return result

    def orders_status(self, feature):
        '''获取属性'''
        result = self.element_sle_style(feature)
        return result

    def orders_status_title(self, feature):
        '''获取属性'''
        result = self.element_tle_style(feature)
        return result

    def pagenum(self):
        """ 获取当前分页参数 """
        ele_list = list()
        ele = self.find_els((By.XPATH, check_param(path='分页')))
        for e in ele:
            ele_list.append(e.text)
        return ele_list