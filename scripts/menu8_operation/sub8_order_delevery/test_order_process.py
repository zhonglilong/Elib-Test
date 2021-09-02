# -*- coding:utf-8 -*-
import time

import pytest
import allure
from page.menu8_operation.sub8_order_delivery.page4_order_process import OrderProcessPage
from utils.driver_utils import DriverUtils
from utils.time_utils import TimeUtils


# 运营-订购处理 测试用例
class TestOrderProcess:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = OrderProcessPage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    @pytest.mark.yun
    def test_select(self, logger):
        """ 测试 查询 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @pytest.mark.yun
    @pytest.mark.parametrize("libname", ["拓迪科技", "广寒"])
    def test_select_lib(self, libname):
        """ 测试 成员馆查询 功能 """
        self.page.click_filter_list(1, libname)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.yun
    @pytest.mark.parametrize("ordername", ["0830", "1234"])
    def test_select_ordername(self, ordername):
        """ 测试 订购批次查询 功能 """
        self.page.click_filter_input("请输入批次", ordername)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.yun
    @pytest.mark.parametrize("ordertype", ["全部", "未确认", "已确认", "出货中", "部分订购", "全部订购"])
    def test_select_ordertype(self, ordertype):
        """ 测试 筛选订单状态 功能 """
        self.page.click_filter_list(3, ordertype)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.zll
    @pytest.mark.parametrize("isbn, ztm, cbs, cbrq", [(9787, "故宫怪兽", "中国", 2019), (5410, "秘密花园", "上海", 2018)])
    def test_select_bookmsg(self, isbn, ztm, cbs, cbrq):
        bookmsg = {"isbn": "ISBN", "ztm": "正题名", "cbs": "出版社", "cbrq": "出版日期"}
        for k, v in bookmsg.items():
            self.page.click_filter_list(4, str(v))
            time.sleep(1)
            if k is "isbn":
                self.page.click_filter_input("请输入搜索关键词", isbn)
            elif k is "ztm":
                self.page.click_filter_input("请输入搜索关键词", ztm)
            elif k is "cbs":
                self.page.click_filter_input("请输入搜索关键词", cbs)
            elif k is "cbrq":
                self.page.click_filter_input("请输入搜索关键词", cbrq)
            self.page.click_btn(path='查询按钮', param="查询")
            assert self.page.sub_menu_alert()








