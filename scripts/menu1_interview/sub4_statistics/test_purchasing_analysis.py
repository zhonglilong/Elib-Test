# -*- coding:utf-8 -*-
import pytest
import time
from page.menu1_interview.sub4_statistics.page5_Purchasing_analysis import PurchasingAnalysisPage
from utils.driver_utils import DriverUtils
from base.config import *


# 采访--采访统计--预订分类统计 测试用例
class TestAdvanceClassification:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = PurchasingAnalysisPage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    @pytest.mark.skx
    def test_select(self, logger):
        """ 测试 查询 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("name", ["全部", "图书馆"])
    @pytest.mark.skx
    def test_select_houses(self, name):
        """ 测试 筛选成员馆 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_filter_list(1, name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("name", ["全部", "书店"])
    @pytest.mark.skx
    def test_select_advanced_order(self, name):
        """ 测试 筛选预订单 查询 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_filter_list(2, name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("year", [TimeUtils().current_year(), TimeUtils().current_year()-1])
    @pytest.mark.skx
    def test_select_date(self, year):
        """ 测试 筛选年份（今年、前年） 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.input_filter_year(year)
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

