# -*- coding:utf-8 -*-
import pytest
import time
from page.menu1_interview.sub5_funds.page01_funds_management import FundsManagementPage
from utils.driver_utils import DriverUtils
from base.config import *


# 采访--采访统计--预订分类统计 测试用例
class TestFundsManagement:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = FundsManagementPage(drivers)

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

    @pytest.mark.parametrize("name", ["全部"])
    @pytest.mark.skx
    def test_select_advanced_order(self, name):
        """ 测试 操作者 查询 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_filter_list(4, name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.skx
    def test_select_date(self):
        """ 测试 筛选日期 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.input_filter_date(start=TimeUtils().today(), end=TimeUtils().today())
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("text, num", [("资金+1", 55), ("资金+2", 33)])
    @pytest.mark.skx
    def test_add(self, text, num):
        """ 测试 新增、删除 功能
        """
        self.page.click_btn(path='右上按钮', param='1')
        time.sleep(1)
        self.page.input_text(path='新增/编辑-输入框', content=text, param='资金名称', itype="clickinput")
        time.sleep(1)
        self.page.input_text(path='新增/编辑-输入框', content=num, param='金额', itype="clickinput")
        self.page.click_btn(path='侧边弹窗底部按钮', param='保存')
        self.page.click_btn(path='表格第一条数据')
        self.page.click_btn(path='右上按钮', param='2')
        self.page.click_btn(path='删除确定/取消', param='2')
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("text, num", [("编辑后资金+1", 550), ("编辑后资金+2", 330)])
    @pytest.mark.skx
    def test_update(self, text, num):
        """ 测试 编辑 功能 """
        time.sleep(1)
        self.page.click_btn(path='查询按钮', param='查询')
        time.sleep(1)
        self.page.double_click_order()
        time.sleep(1)
        self.page.input_text(path='新增/编辑-输入框', content=text, param='资金名称', itype="clearallinput")
        time.sleep(1)
        self.page.input_text(path='新增/编辑-输入框', content=num, param='金额', itype="clearallinput")
        self.page.click_btn(path='侧边弹窗底部按钮', param='保存')
        assert self.page.sub_menu_alert()
