#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
from page.menu1_interview.sub1_reservation.page4_recommended_by_readers import RecommendedByReadersPage
from utils.driver_utils import DriverUtils
from utils.common_utils import ramdon_val
from utils.time_utils import TimeUtils
import time
from base.base_action import BaseAction


# 采访-图书预订处理-读者荐购 测试用例
class TestRecommendedByReaders:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = RecommendedByReadersPage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    #查询区
    @pytest.mark.yun
    def test_select_state(self):
        """ 测试 状态查询 功能 """
        self.page.click_btn(path='查询按钮', param="查询")
        self.page.click_filter_firstlist(num=2,name='全部')
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.yun
    @pytest.mark.parametrize("isbn, ztm, zrz, cbs",
                             [(1032, "故事", "张", "广东"),
                              (6105, "童话", "李", "北京")])
    def test_select_fourthing(self,isbn,ztm,zrz,cbs):
        """ 测试 ISBN、正题名、责任者、出版社查询 功能 """
        fourmsg = {"isbn": "ISBN", "ztm": "正题名", "zrz": "责任者", "cbs": "出版社"}
        for k, v in fourmsg.items():
            self.page.click_filter_firstlist(3, str(v))
            time.sleep(1)
            if k is "isbn":
                self.page.click_filter_firstinput("请输入搜索关键词", isbn)
            elif k is "ztm":
                self.page.click_filter_firstinput("请输入搜索关键词", ztm)
            elif k is "zrz":
                self.page.click_filter_firstinput("请输入搜索关键词", zrz)
            elif k is "cbs":
                self.page.click_filter_firstinput("请输入搜索关键词", cbs)
                TimeUtils().sleep(2)
            self.page.click_btn(path='查询按钮', param="查询")
            assert self.page.sub_menu_alert()

    @pytest.mark.yun
    def test_select_sort(self):
        """ 测试 排序方式 功能 """
        self.page.click_btn(path='查询按钮', param="查询")
        self.page.click_filter_firstlist(num=5, name='ISBN')
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @pytest.mark.yun
    def test_select_date(self):
        """ 测试 荐购时间 功能 """
        TimeUtils().sleep(2)
        self.page.input_filter_date(start=TimeUtils().today(), end=TimeUtils().today())
        TimeUtils().sleep(2)
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @pytest.mark.yun
    def test_import_book(self):
        '''测试 导出荐购书籍 功能'''
        TimeUtils().sleep(2)
        self.page.click_btn(path='右上按钮',param='2')
        result = self.page.judge_by_url_and_status_code('http://192.168.1.35:8080/service/api/e/interview/file/tsjgE')  # (此url为导出文件时的目标接口)
        assert result

    @pytest.mark.yun
    def test_import_reader(self):
        '''测试 导出读者 功能'''
        TimeUtils().sleep(2)
        self.page.click_btn(path='右上按钮', param='3')
        result = self.page.judge_by_url_and_status_code('http://192.168.1.35:8080/service/api/e/interview/param/readerImport')  # (此url为导出读者时的目标接口)
        assert result





