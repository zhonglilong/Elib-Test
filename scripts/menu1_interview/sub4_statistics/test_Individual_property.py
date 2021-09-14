# -*- coding:utf-8 -*-
import pytest
import time
from page.menu1_interview.sub4_statistics.page1_Individual_property import IndividualPropertyPage
from utils.driver_utils import DriverUtils
from base.config import *


# 采访-采访统计-个别财产 测试用例
class TestIndividualProperty:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = IndividualPropertyPage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    @pytest.mark.skx1
    def test_select(self, logger):
        """ 测试 查询 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("name", ["图书馆"])
    @pytest.mark.skx1
    def test_select_houses(self, name):
        """ 测试 筛选财产馆 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_filter_list(1, name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("name", ["全部"])
    @pytest.mark.skx1
    def test_select_advanced_orderr(self, name):
        """ 测试 筛选财产藏址按“全部”查询 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_close_all("财产藏址", 2)
        time.sleep(1)
        self.page.click_filter_list(2, name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("name", ["全部", "编目", "在馆", "借出"])
    @pytest.mark.skx1
    def test_select_booksellers(self, name):
        """ 测试 筛选馆藏状态 ：“全部、编目、在馆、借出” 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        time.sleep(0.5)
        self.page.click_close_all('财产藏址', 3)
        self.page.click_filter_list(3, name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("name", ["全部"])
    @pytest.mark.skx1
    def test_select_book_peoples(self, name):
        """ 测试 入库人  功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_close_all('入库人', 4)
        time.sleep(0.5)
        self.page.click_filter_list(4, name=name)
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @pytest.mark.skx1
    def test_select_date(self):
        """ 测试 筛选入库日期 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.input_filter_date(start=TimeUtils().today(), end=TimeUtils().today())
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("start, end", [("s4", "s9"), ("s1", "s9")])
    @pytest.mark.skx1
    def test_select_items(self, start, end):
        """ 测试 筛选条形码 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        time.sleep(0.5)  # 等待0.5秒在点击查询
        self.page.input_filter_items(start, end)
        time.sleep(0.5)  # 等待0.5秒在点击查询
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

