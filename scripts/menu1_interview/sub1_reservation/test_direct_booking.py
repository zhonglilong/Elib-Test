#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
from page.menu1_interview.sub1_reservation.page3_direct_booking import DirectBookingPage
from utils.driver_utils import DriverUtils
from utils.common_utils import ramdon_val
from utils.time_utils import TimeUtils
import time
from base.base_action import BaseAction


# 采访-图书预订处理-直接预订 测试用例
class TestDirectBooking:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = DirectBookingPage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    #一：增加区
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.run(order=1)
    @pytest.mark.yun
    def test_add_simple_book(self):
        '''测试 新增书籍（简单编目的） 功能'''
        TimeUtils().sleep(2)
        self.page.click_btn(path='右上按钮',param='3')
        TimeUtils().sleep(2)
        self.page.input_text(path='简单编目-输入', content=ramdon_val(), param='11', itype="clickinput")   #仅仅写正题名
        TimeUtils().sleep(2)
        self.page.click_btn(path='新增-编目-右下方按钮',param='5')
        TimeUtils().sleep(2)
        assert  self.page.sub_menu_alert()

    @pytest.mark.yun
    def test_booking_bibliography_click_button(self):
        '''测试 点击目标书籍，点击上方按钮进行书目预订 功能'''
        TimeUtils().sleep(6)
        self.page.click_btn(path='表格某一行的数据', param='3', ctype="click")
        TimeUtils().sleep(2)
        self.page.click_btn(path='右上按钮', param='2')
        TimeUtils().sleep(2)
        self.page.input_text(path='书目信息-预订-预订配置', content='4', param='1', itype="clickinputs")  # 仅仅写正题名
        TimeUtils().sleep(2)
        self.page.click_btn(path='预订配置-下方按钮', param='1')
        TimeUtils().sleep(2)
        assert self.page.sub_menu_alert()

    @pytest.mark.yun
    def test_booking_bibliography_double_click(self):
        '''测试 点击目标书籍，双击进行书目预订 功能'''
        TimeUtils().sleep(6)
        self.page.click_btn(path='表格某一行的数据', param='4',ctype="clicks")
        TimeUtils().sleep(2)
        self.page.input_text(path='书目信息-预订-预订配置', content='5', param='1', itype="clickinputs")  # 仅仅写正题名
        TimeUtils().sleep(2)
        self.page.click_btn(path='预订配置-下方按钮', param='1')
        TimeUtils().sleep(2)
        assert self.page.sub_menu_alert()

    #二：查询区
    @pytest.mark.yun
    @pytest.mark.parametrize("isbn, ztm, flh, zrz, ztc, cbs, cb,, dgh, tyskh",
                             [(5002, "故事", 64, "张", "小说", "广东", 2, 11, 12),
                              (5080, "童话", 52, "李", "散文", "北京", 4, 22, 18)])
    def test_select_bookmsg(self, isbn, ztm, flh, zrz, ztc, cbs, cb, dgh, tyskh):
        """ 测试 条件筛选 """
        TimeUtils().sleep(6)
        bookmsg = {"isbn": "ISBN", "ztm": "正题名", "flh": "分类号", "zrz": "责任者", "ztc": "主题词", "cbs": "出版社", "cb": "丛编", "dgh": "订购号", "tyskh": "统一书刊号"}
        for k, v in bookmsg.items():
            self.page.click_filter_firstlist(1, str(v))
            time.sleep(1)
            if k is "isbn":
                self.page.click_filter_firstinput("请输入搜索关键词", isbn)
            elif k is "ztm":
                self.page.click_filter_firstinput("请输入搜索关键词", ztm)
            elif k is "flh":
                self.page.click_filter_firstinput("请输入搜索关键词", flh)
            elif k is "zrz":
                self.page.click_filter_firstinput("请输入搜索关键词", zrz)
            elif k is "ztc":
                self.page.click_filter_firstinput("请输入搜索关键词", ztc)
            elif k is "cbs":
                self.page.click_filter_firstinput("请输入搜索关键词", cbs)
            elif k is "cb":
                self.page.click_filter_firstinput("请输入搜索关键词", cb)
            elif k is "dgh":
                self.page.click_filter_firstinput("请输入搜索关键词", dgh)
            elif k is "tyskh":
                self.page.click_filter_firstinput("请输入搜索关键词", tyskh)
                TimeUtils().sleep(2)
            self.page.click_btn(path='查询按钮', param="查询")
            assert self.page.sub_menu_alert()

    #三：修改区
    @pytest.mark.yun
    def test_parameter_setting(self):
        '''测试 点击右上方的参数设置按钮 功能'''
        TimeUtils().sleep(6)
        self.page.click_btn(path='右上按钮',param='4')
        TimeUtils().sleep(1)
        button_result = self.page.verify_button_status(path='设为默认参数按钮', label='class')
        TimeUtils().sleep(1)
        if 'is-checked' in button_result:
            self.page.input_text(path='默认参数表格内容', content='1234', param='1', itype="clickinputs")
            TimeUtils().sleep(1)
            self.page.input_text(path='默认参数表格内容', content='2345', param='7', itype="clickinputs")
            TimeUtils().sleep(1)
            self.page.click_btn(path='默认参数表格-下方操作按钮', param='1')
        else:
            self.page.click_btn(path='设为默认参数按钮')
            self.page.input_text(path='默认参数表格内容', content='123', param='1', itype="clickinputs")
            TimeUtils().sleep(1)
            self.page.input_text(path='默认参数表格内容', content='234', param='7', itype="clickinputs")
            TimeUtils().sleep(1)
            self.page.click_btn(path='默认参数表格-下方操作按钮', param='1')
        assert self.page.sub_menu_alert()





