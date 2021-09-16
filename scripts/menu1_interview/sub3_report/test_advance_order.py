# -*- coding:utf-8 -*-
import pytest
import time
from page.menu1_interview.sub3_report.page1_advance_order import AdvanceOrderPage
from utils.driver_utils import DriverUtils
from utils.time_utils import TimeUtils


# 采访-预订单 测试用例
class TestAdvanceOrder:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = AdvanceOrderPage(drivers)

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
    def test_select_advanced_orderr(self, name):
        """ 测试 筛选预订单按“全部”查询 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_close_all("预订单", 2)
        time.sleep(0.5)
        self.page.click_filter_list(2, name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("name", ["全部"])
    @pytest.mark.skx
    def test_select_booksellers(self, name):
        """ 测试 筛选书商 全部 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_close_all("书商", 3)
        time.sleep(0.5)
        self.page.click_filter_list(3, name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("name", ["全部"])
    @pytest.mark.skx
    def test_select_book_peoples(self, name):
        """ 测试 筛选预订人 全部 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_filter_list(4, name=name)
        time.sleep(0.5)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.skx
    def test_select_date(self):
        """ 测试 筛选预订日期 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.input_filter_date(start=TimeUtils().today(), end=TimeUtils().today())
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("start, end", [(11, 55), (22, 33)])
    @pytest.mark.skx
    def test_select_items(self, start, end):
        """ 测试 筛选订购号 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        time.sleep(0.5)  # 等待0.5秒在点击查询
        self.page.input_filter_items(start, end)
        time.sleep(0.5)  # 等待0.5秒在点击查询
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

