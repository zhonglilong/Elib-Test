#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
from page.menu2_catalog.sub3_statistics.page1_book_label_printing import BookLabelPrintingPage
from utils.driver_utils import DriverUtils
from utils.common_utils import ramdon_val
from utils.time_utils import TimeUtils
import time
from base.base_action import BaseAction


# 采访-图书预订处理-预订单管理 测试用例
class TestBookLabelPrinting:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = BookLabelPrintingPage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    # 一：查询区
    @pytest.mark.yun
    def test_select_call_number(self):
        """ 测试 根据索书号查询书籍信息  """
        call_number = '20'
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep(1)
        self.page.click_filter_input(path='筛选-输入框', content=call_number, param='请输入索书号')
        TimeUtils().sleep(1)
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep(2)
        target_title = self.page.check_state_param(path='随机一行中随机一列的值', param=[1, 10])
        assert call_number in target_title

    @pytest.mark.yun
    def test_select_date(self):
        ''' 测试 查询入库时间 功能 '''
        self.page.click_btn(path='查询按钮', param='查询')
        start_time = TimeUtils().long_ago_time(month_num=1, fulltime=True)
        self.page.click_filter_input(path='筛选-输入框', param='开始日期', content=start_time)
        TimeUtils().sleep(2)
        end_time = TimeUtils().today(istime=True)
        self.page.click_filter_input(path='筛选-输入框', param='结束日期', content=end_time)
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep(2)
        target_time = self.page.check_state_param(path='随机一行中随机一列的值', param=[1, 12])
        assert TimeUtils().check_time_state(start_time, end_time, target_time, same_time=True)

    @pytest.mark.yun
    def test_select_bar_code(self):
        """ 测试 查询条形码 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.input_bar_code(path='筛选-输入框', param='请输入起始条形码', content='TD2021080601')
        self.page.input_bar_code(path='筛选-输入框', param='请输入结束条形码', content='TD2021080603')
        TimeUtils().sleep(2)
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep(2)
        assert self.page.sub_menu_alert()

    @pytest.mark.yun
    def test_select_operator(self):
        ''' 测试 查询操作人 功能'''
        operator = '小白'
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_btn(path='查询按钮', param="查询")
        self.page.click_operator_list(num=3, name=operator)
        self.page.click_btn(path='查询按钮', param="查询")
        TimeUtils().sleep(2)
        target_title = self.page.check_state_param(path='随机一行中随机一列的值', param=[1, 13])
        assert operator == target_title

    @pytest.mark.yun
    def test_select_book_type(self):
        ''' 测试 查询图书类型 功能'''
        book_type = 'aa|图书'
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_btn(path='查询按钮', param="查询")
        self.page.click_operator_list(num=4, name=book_type)
        self.page.click_btn(path='查询按钮', param="查询")
        TimeUtils().sleep(1)
        target_title = self.page.check_state_param(path='随机一行中随机一列的值', param=[1, 11])
        TimeUtils().sleep(1)
        assert book_type == target_title

    #二：其它
    @pytest.mark.yun
    def test_print_label(self):
        '''测试 打印书标按钮 '''
        self.page.click_btn(path='右上按钮', param='1')
        TimeUtils().sleep(1)
        assert self.page.check_pop_up_window(path='书标打印-弹出窗口', param='dialog')
        TimeUtils().sleep(2)
        self.page.click_btn(path='弹出窗口-叉', param='dialog')

    @pytest.mark.yun
    def test_make_up_print(self):
        '''测试 补缺打印按钮 '''
        self.page.click_btn(path='右上按钮', param='2')
        TimeUtils().sleep(1)
        assert self.page.check_pop_up_window(path='书标打印-弹出窗口', param='补缺打印')
        TimeUtils().sleep(1)
        self.page.click_btn(path='弹出窗口-叉', param='补缺打印')
