# -*- coding:utf-8 -*-
import pytest
import time
from page.menu1_interview.sub4_statistics.page4_check_classification import CheckClassificationPage
from base.config import *
from utils.driver_utils import DriverUtils


# 采访--采访统计--预订分类统计 测试用例
class TestAdvanceClassification:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = CheckClassificationPage(drivers)

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

    @pytest.mark.parametrize("name", ["图书馆"])
    @pytest.mark.skx
    def test_select_houses(self, name):
        """ 测试 筛选成员馆 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_filter_list(1, name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("name", ["全部"])
    @pytest.mark.skx
    def test_select_advanced_order(self, name):
        """ 测试 筛选验收单 查询 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_close_all("验收单", 2)
        time.sleep(0.5)
        self.page.click_filter_list(2, name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.skx
    def test_select_date(self):
        """ 测试 筛选验收日期 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.input_filter_date(start=TimeUtils().today(), end=TimeUtils().today())
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

