# -*- coding:utf-8 -*-
import time

import pytest
import allure
from page.menu2_catalog.sub1_catalog.page1_cataloging_management import CatalogingManagementPage
from utils.driver_utils import DriverUtils
from utils.time_utils import TimeUtils


# 编目-编目管理 测试用例
class TestCatalogingManagement:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = CatalogingManagementPage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    @pytest.mark.yun
    @pytest.mark.reading
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @pytest.mark.reading
    @pytest.mark.zll
    @pytest.mark.parametrize("libname", ["CS馆"])
    def test_select_lib(self, libname):
        """ 测试 成员馆查询 功能 """
        self.page.click_filter_list([1, 1], libname)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()
        assert self.page.verify_filter(num=[1, 1], label='placeholder') == libname

    @pytest.mark.parametrize(
        # ISBN、正题名、分类号、责任者、主题词、出版日期、语种、出版社、出版地、价格、其他责任者、其他责任者的正题名、ISRC、从编、题名、订购号、统一书刊号
        "isbn, ztm, flh, zrz, ztc, cbrq, yz, cbs, cbd, jg, qtzrz, qtzrzdztm, isrc, cb, tm, dgh, tyskh", [
            (9787, "故宫怪兽", "B81", "汤志伟", "传统工艺", 2019, "chi", "社会科学出版社", "中国", "99", "张保生", "1", "2", "3", "4", "5", "6"),
            (5410, "秘密花园", "G12", "江畅", "民法", 2018, "eng", "新星出版社", "上海", "98", "1", "2", "3", "4", "5", "6", "7")
        ])
    @pytest.mark.zll
    def test_select_bookmsg(self, isbn, ztm, flh, zrz, ztc, cbrq, yz, cbs, cbd, jg, qtzrz, qtzrzdztm, isrc, cb, tm, dgh, tyskh):
        bookmsg = {"isbn": "ISBN", "ztm": "正题名", "flh": "分类号", "zrz": "责任者", "ztc": "主题词",
                   "cbrq": "出版日期", "yz": "语种", "cbs": "出版社", "cbd": "出版地", "jg": "价格", "qtzrz": "其他责任者",
                   "qtzrzdztm": "其他责任者的正题名", "isrc": "ISRC", "cb": "从编", "tm": "题名", "dgh": "订购号", "tyskh": "统一书刊号"}
        for k, v in bookmsg.items():
            self.page.click_filter_list([1, 3], str(v))
            time.sleep(1)
            if k is "isbn":
                self.page.click_filter_input("请输入搜索关键词", isbn)
            elif k is "ztm":
                self.page.click_filter_input("请输入搜索关键词", ztm)
            elif k is "flh":
                self.page.click_filter_input("请输入搜索关键词", flh)
            elif k is "zrz":
                self.page.click_filter_input("请输入搜索关键词", zrz)
            elif k is "ztc":
                self.page.click_filter_input("请输入搜索关键词", ztc)
            elif k is "cbrq":
                self.page.click_filter_input("请输入搜索关键词", cbrq)
            elif k is "yz":
                self.page.click_filter_input("请输入搜索关键词", yz)
            elif k is "cbs":
                self.page.click_filter_input("请输入搜索关键词", cbs)
            elif k is "cbd":
                self.page.click_filter_input("请输入搜索关键词", cbd)
            elif k is "jg":
                self.page.click_filter_input("请输入搜索关键词", jg)
            elif k is "qtzrz":
                self.page.click_filter_input("请输入搜索关键词", qtzrz)
            elif k is "qtzrzdztm":
                self.page.click_filter_input("请输入搜索关键词", qtzrzdztm)
            elif k is "isrc":
                self.page.click_filter_input("请输入搜索关键词", isrc)
            elif k is "cb":
                self.page.click_filter_input("请输入搜索关键词", cb)
            elif k is "tm":
                self.page.click_filter_input("请输入搜索关键词", tm)
            elif k is "tm":
                self.page.click_filter_input("请输入搜索关键词", dgh)
            elif k is "tm":
                self.page.click_filter_input("请输入搜索关键词", tyskh)
            self.page.click_btn(path='查询按钮', param="查询")
            assert self.page.sub_menu_alert()
