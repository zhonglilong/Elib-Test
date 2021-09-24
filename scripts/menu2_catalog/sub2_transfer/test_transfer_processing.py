#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
from page.menu2_catalog.sub2_transfer.page1_transfer_processing import TransferProcessingPage
from utils.driver_utils import DriverUtils
from utils.common_utils import ramdon_val
from utils.time_utils import TimeUtils
import time
from base.base_action import BaseAction


# 编目-文献移送-移送处理 测试用例
class TestTransferProcessing:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = TransferProcessingPage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    # 一：查询区
    @pytest.mark.run(order=1)
    @pytest.mark.yun
    @pytest.mark.parametrize("ysdm, ysmc, ss",
                             [(1, "直接", "京东"),
                              (2, "间接", "新华")])
    def test_select_three_conditions(self, ysdm, ysmc, ss):
        """ 测试 条件筛选验收单 """
        acceptmsg = {"ysdm": "验收代码", "ysmc": "预算名称", "ss":"书商"}
        for k, v in acceptmsg.items():
            self.page.click_filter_firstlist(1, str(v))
            time.sleep(1)
            if k is "ysdm":
                self.page.click_filter_firstinput("请输入搜索关键词", ysdm)
            elif k is "ysmc":
                self.page.click_filter_firstinput("请输入搜索关键词", ysmc)
            elif k is "ss":
                self.page.click_filter_firstinput("请输入搜索关键词", ss)
            self.page.click_btn(path='查询按钮', param="查询")
            assert self.page.sub_menu_alert()

    @pytest.mark.run(order=2)
    @pytest.mark.yun
    def test_select_operator(self):
        """ 测试 查询操作人 功能"""
        self.page.click_btn(path='查询按钮', param="查询")
        self.page.click_filter_firstlist(num=3, name='小云')
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    #二：修改区
    @pytest.mark.run(order=3)
    @pytest.mark.yun
    def test_change_book_state(self):
        '''测试 修改图书交送状态 功能'''
        TimeUtils().sleep(1)
        self.page.click_btn(path='查询按钮',param='查询')
        TimeUtils().sleep(1)
        self.page.click_btn(path='表格某一行的数据',param='3')
        TimeUtils().sleep(1)
        self.page.click_btn(path='查询按钮',param='图书交送')
        TimeUtils().sleep(1)
        self.page.click_btn(path='删除确定/取消',param='2')
        TimeUtils().sleep(1)
        state_name = self.page.check_state_param(path='编目-已交送列',param='3')
        assert state_name == '是'

