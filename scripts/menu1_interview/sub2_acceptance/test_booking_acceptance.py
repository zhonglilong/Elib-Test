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
        """ 测试 书目信息 批量验收功能 """
        self.page.check_order()
        TimeUtils().sleep(2)
        self.page.click_check_accept()
        TimeUtils().sleep(2)
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_all_acceptance(self):
        """ 测试 书目信息 全部验收功能 """
        TimeUtils().sleep(2)
        self.page.click_all_accept()
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_alter_parts(self):
        """ 测试 书目信息 MARC编目下拉列表 """
        TimeUtils().sleep(2)
        # self.page.click_btn(path="表格第*条数据", param="12")
        self.page.click_marc_catalog()
        TimeUtils().sleep(2)
        self.page.click_type_parts(name="CNMARC中文期刊")
        TimeUtils().sleep(2)
        self.page.click_mtype_template(name="中文期刊模板")
        TimeUtils().sleep(2)
        self.page.click_mcheck_out(name="馆藏资源")
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        TimeUtils().sleep(2)
        self.page.account_status_of_judge()
        TimeUtils().sleep(2)
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_catalog_list(self):
        """ 测试 书目信息 简单编目下拉列表 """
        TimeUtils().sleep(2)
        self.page.click_simple_template()
        TimeUtils().sleep(2)
        self.page.click_simple_parts(name="CNMARC中文期刊")
        TimeUtils().sleep(2)
        self.page.click_type_template(name="馆藏资源")
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        TimeUtils().sleep(2)
        self.page.account_status_of_judge()
        TimeUtils().sleep(2)
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    # @pytest.mark.parametrize("isbn, ztm, flh, zrz, cbs, isrc",[("1", "罗小黑", "J649", "方光光", "天津人民出版社", "%")])
    def test_parent_record(self):
        """ 测试 书目信息 父记录连接 """
        element = "el-button el-button--primary el-button--mini is-disabled"
        TimeUtils().sleep(2)
        self.page.click_simple_template()
        TimeUtils().sleep(2)
        classname = self.page.account_parent_record(path='编目-简单编目-添加父记录')
        if element in classname:
            self.page.click_btn(path='编目-简单编目-查看连接记录')
            TimeUtils().sleep(2)
            self.page.click_btn(path='父记录-移除')
            TimeUtils().sleep(2)
            self.page.click_btn(path='移除-确定')
            TimeUtils().sleep(2)
        self.page.click_btn(path='编目-简单编目-添加父记录')
        TimeUtils().sleep(2)
        self.page.input_text(path='添加父记录-查询输入框', param="2", content="1", itype="clearinput")
        TimeUtils().sleep(2)
        self.page.click_btn(path='添加父记录-查询')
        TimeUtils().sleep(2)
        self.page.click_btn(path='添加父记录-确认')
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    # @pytest.mark.parametrize("isbn, ztm, flh, zrz, cbs, isrc",[("1", "罗小黑", "J649", "方光光", "天津人民出版社", "%")])
    def test_refer_record(self):
        """ 测试 书目信息 查询父记录 解除连接 """
        element = "el-button el-button--primary el-button--mini is-disabled"
        TimeUtils().sleep(2)
        self.page.click_simple_template()
        TimeUtils().sleep(2)
        classname = self.page.account_parent_record(path='编目-简单编目-查看连接记录')
        if element in classname:
            self.page.click_btn(path='编目-简单编目-添加父记录')
            TimeUtils().sleep(2)
            self.page.input_text(path='添加父记录-查询输入框', param="2", content="1", itype="clearinput")
            TimeUtils().sleep(2)
            self.page.click_btn(path='添加父记录-查询')
            TimeUtils().sleep(2)
            self.page.click_btn(path='添加父记录-确认')
            TimeUtils().sleep(2)
        self.page.click_btn(path='编目-简单编目-查看连接记录')
        TimeUtils().sleep(2)
        self.page.click_btn(path='父记录-移除')
        TimeUtils().sleep(2)
        self.page.click_btn(path='移除-确定')
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        assert self.page.sub_menu_alert()

    @pytest.mark.zhl
    @pytest.mark.parametrize("isbn, ztm, flh, zrz, cbs, isrc", [("1", "罗小黑", "J649", "方光光", "天津人民出版社", "%")])
    def test_parent_refer(self, isbn, ztm, flh, zrz, cbs, isrc):
        """ 测试 书目信息 父记录连接查询 """
        element = "el-button el-button--primary el-button--mini is-disabled"
        TimeUtils().sleep(2)
        self.page.click_simple_template()
        TimeUtils().sleep(2)
        classname = self.page.account_parent_record(path='编目-简单编目-添加父记录')
        if element in classname:
            self.page.click_btn(path='编目-简单编目-查看连接记录')
            TimeUtils().sleep(2)
            self.page.click_btn(path='父记录-移除')
            TimeUtils().sleep(2)
            self.page.click_btn(path='移除-确定')
            TimeUtils().sleep(2)
        self.page.click_btn(path='编目-简单编目-添加父记录')
        TimeUtils().sleep(2)
        Spinner = {"isbn": "ISBN", "ztm": "正题名", "flh": "分类号", "zrz": "责任者", "cbs": "出版社", "isrc": "ISRC"}
        for k, v in Spinner.items():
            self.page.click_filter_parent(1, str(v))
            TimeUtils().sleep(2)
            self.page.click_filter_parent(3, str(v))
            time.sleep(1)
            if k == "isbn":
                self.page.click_parent_input("2", isbn)
                self.page.click_parent_input("4", isbn)
            elif k == "ztm":
                self.page.click_parent_input("2", ztm)
                self.page.click_parent_input("4", ztm)
            elif k == "flh":
                self.page.click_parent_input("2", flh)
                self.page.click_parent_input("4", flh)
            elif k == "zrz":
                self.page.click_parent_input("2", zrz)
                self.page.click_parent_input("4", zrz)
            elif k == "cbs":
                self.page.click_parent_input("2", cbs)
                self.page.click_parent_input("4", cbs)
            elif k == "isrc":
                self.page.click_parent_input("2", isrc)
                self.page.click_parent_input("4", isrc)
            TimeUtils().sleep(2)
            self.page.click_btn(path='添加父记录-查询')
        self.page.click_btn(path='添加父记录-取消')
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        assert self.page.sub_menu_alert()
