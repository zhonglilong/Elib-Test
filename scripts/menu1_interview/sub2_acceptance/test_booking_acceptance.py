# C:/test1
# -*- coding: utf-8 -*-
# @time : 
# Author : 小白
import pytest
import time
from utils.driver_utils import DriverUtils
from utils.time_utils import TimeUtils
from page.menu1_interview.sub2_acceptance.page2_booking_acceptance import BookingAcceptancePage

# 采访-图书验收处理-预订验收  测试用例

class TestBookingAcceptance:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = BookingAcceptancePage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    # @pytest.mark.zhl
    @pytest.mark.parametrize("name", ["全部", "妖灵会馆", "老君书阁"])
    def test_select_bookseller(self, name):
        """ 测试 预订单 筛选功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_filter_list(name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    @pytest.mark.parametrize("isbn, ztm, flh, zrz, ftm, fjh, cbs, jg, cb, tm, dgh, tyskh",
                             [("9787", "罗小黑", "J649", "东篱子", "珍藏版", "灵枢篇", "出版社", "52.00", "%", "罗小黑", "%", "%")])
    def test_search_details(self, isbn, ztm, flh, zrz, ftm, fjh, cbs, jg, cb, tm, dgh, tyskh):
        """ 测试 书目信息 搜索功能 """
        ysdDetails = {"isbn": "ISBN", "ztm": "正题名", "flh": "分类号", "zrz": "责任者", "ftm": "副题名", "fjh": "分辑号", "cbs": "出版社"
            , "jg": "价格", " cb": "丛编", "tm": "题名", "dgh": "订购号", "tyskh": "统一书刊号"}
        for k, v in ysdDetails.items():
            self.page.click_filter_lists(2, str(v))
            time.sleep(1)
            if k == "isbn":
                self.page.click_filter_input("请输入搜索关键词", isbn)
            elif k == "ztm":
                self.page.click_filter_input("请输入搜索关键词", ztm)
            elif k == "flh":
                self.page.click_filter_input("请输入搜索关键词", flh)
            elif k == "zrz":
                self.page.click_filter_input("请输入搜索关键词", zrz)
            elif k == "ftm":
                self.page.click_filter_input("请输入搜索关键词", ftm)
            elif k == "fjh":
                self.page.click_filter_input("请输入搜索关键词", fjh)
            elif k == "cbs":
                self.page.click_filter_input("请输入搜索关键词", cbs)
            elif k == "jg":
                self.page.click_filter_input("请输入搜索关键词", jg)
            elif k == "cb":
                self.page.click_filter_input("请输入搜索关键词", cb)
            elif k == "tm":
                self.page.click_filter_input("请输入搜索关键词", tm)
            elif k == "dgh":
                self.page.click_filter_input("请输入搜索关键词", dgh)
            elif k == "tyskh":
                self.page.click_filter_input("请输入搜索关键词", tyskh)
            self.page.click_btn(path='查询按钮', param="查询")
            assert self.page.sub_menu_alert()
        TimeUtils().sleep(2)
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_receipt_dispose(self):
        """ 测试 书目信息 批量验收功能"""
        self.page.check_order()
        TimeUtils().sleep(2)
        self.page.click_check_accept()
        TimeUtils().sleep(2)
        assert self.page.sub_menu_alert()

    @pytest.mark.zhl
    def test_all_acceptance(self):
        """ 测试 书目信息 全部验收功能"""
        TimeUtils().sleep(2)
        self.page.click_all_accept()
        assert self.page.sub_menu_alert()


