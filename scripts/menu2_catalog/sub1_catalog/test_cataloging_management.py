# -*- coding:utf-8 -*-
import logging
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
    @pytest.mark.yun
    @pytest.mark.parametrize("libname", ["CS馆"])
    def test_select_lib(self, libname):
        """ 测试 成员馆查询 功能 """
        self.page.click_filter_list([1, 1, 1], libname)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()
        assert self.page.verify_filter(num=[1, 1, 1], label='placeholder') == libname

    @pytest.mark.parametrize(
        # ISBN、正题名、分类号、责任者、主题词、出版日期、语种、出版社、出版地、价格、其他责任者、其他责任者的正题名、ISRC、从编、题名、订购号、统一书刊号
        "isbn, ztm, flh, zrz, ztc, cbrq, yz, cbs, cbd, jg, qtzrz, qtzrzdztm, isrc, cb, tm, dgh, tyskh", [
            (9787, "故宫怪兽", "B81", "汤志伟", "传统工艺", 2019, "chi", "社会科学出版社", "中国", "99", "张保生", "1", "2", "3", "4", "5", "6"),
            (5410, "秘密花园", "G12", "江畅", "民法", 2018, "eng", "新星出版社", "上海", "98", "1", "2", "3", "4", "5", "6", "7")
        ])
    @pytest.mark.zll
    def test_select_bookmsg(self, isbn, ztm, flh, zrz, ztc, cbrq, yz, cbs, cbd, jg, qtzrz, qtzrzdztm, isrc, cb, tm, dgh, tyskh):
        """ 测试 书目信息的关键词查询 功能 """
        bookmsg = {"ztm": ["正题名", ztm], "flh": ["分类号", flh], "zrz": ["责任者", zrz], "ztc": ["主题词", ztc], "cbrq": ["出版日期", cbrq], "yz": ["语种", yz],
                   "cbs": ["出版社", cbs], "cbd": ["出版地", cbd], "jg": ["价格", jg], "qtzrz": ["其他责任者", qtzrz], "qtzrzdztm": ["其他责任者的正题名", qtzrzdztm],
                   "isrc": ["ISRC", isrc], "cb": ["丛编", cb], "tm": ["题名", tm], "dgh": ["订购号", dgh], "tyskh": ["统一书刊号", tyskh], "isbn": ["ISBN", isbn]}
        for k, v in bookmsg.items():
            self.page.click_filter_list([1, 3, 1], str(v[0]))
            time.sleep(1)

            self.page.click_filter_input("请输入搜索关键词", str(v[1]))
            self.page.click_btn(path='查询按钮', param="查询")

            time.sleep(1)
            if self.page.pagenum()[0] == "0":
                assert str(self.page.alert_exist(atype='yellowAlert')).find("暂无数据") is not -1
            assert self.page.sub_menu_alert()

    @pytest.mark.parametrize(
        # ISBN、正题名、分类号、责任者、主题词、出版日期、语种、出版社、出版地、价格、其他责任者、其他责任者的正题名、ISRC、从编、题名、订购号、统一书刊号
        "isbn, ztm, flh, zrz, ztc, cbrq, yz, cbs, cbd, jg, qtzrz, qtzrzdztm, isrc, cb, tm, dgh, tyskh", [
            (9787, "故宫怪兽", "B81", "汤志伟", "传统工艺", 2019, "chi", "社会科学出版社", "中国", "99", "张保生", "1", "2", "3", "4", "5", "6"),
            (5410, "秘密花园", "G12", "江畅", "民法", 2018, "eng", "新星出版社", "上海", "98", "1", "2", "3", "4", "5", "6", "7")
        ])
    @pytest.mark.reading
    def test_select_bookmsgs(self, isbn, ztm, flh, zrz, ztc, cbrq, yz, cbs, cbd, jg, qtzrz, qtzrzdztm, isrc, cb, tm, dgh, tyskh):
        """ 测试 多个书目信息搜索框一起查询 功能 """
        bookmsgs = {"msg1": ["责任者", zrz, "主题词", ztc, "出版日期", cbrq], "msg2": ["语种", yz, "出版社", cbs, "出版地", cbd],
                    "msg3": ["价格", jg, "其他责任者", qtzrz, "其他责任者的正题名", qtzrzdztm], "msg4": ["ISRC", isrc, "丛编", cb, "题名", tm],
                    "msg5": ["订购号", dgh, "统一书刊号", tyskh], "msg6": ["ISBN", isbn, "正题名", ztm, "分类号", flh]}
        self.page.add_or_remove_filter(otype='add')
        self.page.add_or_remove_filter(otype='add')
        time.sleep(1)
        for k, v in bookmsgs.items():
            try:
                self.page.click_filter_list([1, 3, 1], str(v.pop(0)))
                self.page.click_filter_list([1, 4, 1], str(v.pop(1)))
                if v[2] is not None:
                    self.page.click_filter_list([1, 5, 1], str(v.pop(2)))
                time.sleep(1)

                i = 0
                for element in self.page.click_filter_inputs():
                    element.clear()
                    element.send_keys(str(v[i]))
                    i += 1
            except IndexError as e:
                logging.error("数组越界了：%s" % e)
            self.page.click_btn(path='查询按钮', param="查询")

            time.sleep(1)

            if self.page.pagenum()[0] == "0":
                assert str(self.page.alert_exist(atype='yellowAlert')).find("暂无数据") is not -1
            assert self.page.sub_menu_alert()

    @pytest.mark.reading
    def test_select_bookmsg_item(self):
        """ 测试 1~3个关键词搜索框的加减 功能 """
        num = self.page.verify_filter_num("1")
        self.page.add_or_remove_filter(otype='add')
        self.page.add_or_remove_filter(otype='add')
        num2 = self.page.verify_filter_num("1")
        assert num < num2 and num + 2 == num2
        assert self.page.sub_menu_alert()
        self.page.add_or_remove_filter(otype='remove')
        num3 = self.page.verify_filter_num("1")
        assert num3 < num2 and num3 + 1 == num2
        assert self.page.sub_menu_alert()
        self.page.add_or_remove_filter(otype='add')
        num4 = self.page.verify_filter_num("1")
        assert num3 < num4 and num3 + 1 == num4
        assert self.page.sub_menu_alert()
        self.page.add_or_remove_filter(otype='remove')
        self.page.add_or_remove_filter(otype='remove')
        num5 = self.page.verify_filter_num("1")
        assert num5 < num4 and num5 + 2 == num4
        assert self.page.sub_menu_alert()

    @pytest.mark.reading
    def test_select_items(self):
        """ 测试 第二行筛选项隐藏和显示 功能
        PS：没法测试好像，元素都在dom树中，无论是否显示判断都是显示
        """
        text = self.page.output_text(path='筛选项', param=['1', '5'])
        if text == '更多筛选':
            self.page.click_btn(path='筛选项', param=['1', '5'])
            assert self.page.output_text(path='筛选项', param=['1', '5']) == '隐藏筛选'
        elif text == '隐藏筛选':
            self.page.click_btn(path='筛选项', param=['1', '5'])
            assert self.page.output_text(path='筛选项', param=['1', '5']) == '更多筛选'
        else:
            logging.error("获取字符串不正确")
        assert self.page.sub_menu_alert()
        # self.page.click_btn(path='筛选项', param=['1', '5'])
        # time.sleep(3)
        # assert self.page.verify_filter_display(path='筛选项', param=['2', '5']) is True
        # assert self.page.sub_menu_alert()
        # self.page.click_btn(path='筛选项', param=['1', '5'])
        # time.sleep(2)
        # assert self.page.verify_filter_display(path='筛选项', param=['1', '5']) is False
        # assert self.page.sub_menu_alert()

    @pytest.mark.reading
    @pytest.mark.parametrize("value", ["是", "否", "全部"])
    def test_select_proofread(self, value):
        """ 测试 审校筛选 功能 """
        self.page.verify_filter_items()
        self.page.click_filter_list([2, 1, 1], value)
        self.page.click_btn(path='查询按钮', param="查询")
        if value == "是" and self.page.pagenum()[0] != "0":
            assert self.page.verify_checkbox('已审核') is True
        elif value == "否" and self.page.pagenum()[0] != "0":
            assert self.page.verify_checkbox('已审核') is False
        assert self.page.sub_menu_alert()

    @pytest.mark.zll
    @pytest.mark.parametrize("staff", ["创建人", "编目人", "审校人"])
    @pytest.mark.parametrize("value", ["吴君", "zll", "zhl"])
    def test_select_staff(self, staff, value):
        self.page.verify_filter_items()
        self.page.click_filter_list([2, 2, 1], staff)
        self.page.click_filter_list([2, 3, 1], value)
        self.page.click_btn(path='查询按钮', param="查询")
        time.sleep(1)
        if staff == "创建人" and self.page.pagenum()[0] != '0':
            assert value == self.page.verify_staff()[0]
        assert self.page.sub_menu_alert()
    #
    # @pytest.mark.reading
    # @pytest.mark.parametrize("date", ["创建日期", "编目日期", "审校日期"])
    # def test_select_date(self, date):
    #     self.page.verify_filter_items()
    #     self.page.click_filter_list([2, 4, 1], date)





