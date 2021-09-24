#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
from page.menu1_interview.sub1_reservation.page2_advance_order import AdvanceOrderPage
from utils.driver_utils import DriverUtils
from utils.common_utils import ramdon_val
from utils.time_utils import TimeUtils
import time
from base.base_action import BaseAction


# 采访-图书预订处理-预订单管理 测试用例
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

    #一：增加区
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.run(order=1)
    @pytest.mark.yun
    def test_add_information(self):
        '''测试 新增预订单 功能'''
        TimeUtils().sleep(1)
        self.page.click_btn(path='右上按钮',param='1')
        TimeUtils().sleep(1)
        self.page.input_text(path='采访-新增/编辑-输入', content=ramdon_val(), param='预订单', itype="clickinput")
        TimeUtils().sleep(1)
        self.page.click_btn(path='采访-新增/编辑-按钮',param='保存')
        assert  self.page.sub_menu_alert()

    # 二：查询区
    @pytest.mark.yun
    @pytest.mark.parametrize("ydd, ss", [(1, "新华书店"), (2, "京东")])
    def test_select_ordermsg(self, ydd, ss):
        """ 测试 条件筛选（预订单和书商）筛选预订单(ydd) 书商(ss) """
        ordermsg = {"ydd": "预订单", "ss": "书商"}
        for k, v in ordermsg.items():
            self.page.click_filter_firstlist(1, str(v))
            # //筛选项：div[@class='header__line'][{0}]/div[{1}]  导入“1”进去 //div[@class='header__line'][1]/div[1]
            # 导入“1”进去 //div[@class='header__line'][1]/div[1] -->选择框
            # //div[@class='header__line'][1]/div[2] -->输入框
            time.sleep(1)
            if k is "ydd":
                self.page.click_filter_firstinput("请输入搜索关键词", ydd)
            elif k is "ss":
                self.page.click_filter_firstinput("请输入搜索关键词", ss)
            self.page.click_btn(path='查询按钮', param="查询")
            assert self.page.sub_menu_alert()

    #@pytest.mark.reading
    @pytest.mark.run(order=2)
    @pytest.mark.yun
    def test_select_date(self):
        """ 测试 条件筛选（创建时间） 筛选日期 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.input_filter_date(start=TimeUtils().today(), end=TimeUtils().today())
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    #三：修改区
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.yun
    def test_information_click_button_update(self):
        '''测试 点击操作中的修改按钮，修改预订单 功能'''
        TimeUtils().sleep(1)
        self.page.click_btn(path='查询按钮',param='查询')
        TimeUtils().sleep(1)
        self.page.click_select_list(name='编辑')
        TimeUtils().sleep(1)
        self.page.input_text(path='采访-新增/编辑-输入', content=ramdon_val(), param='预订单', itype="clickinput")
        TimeUtils().sleep(1)
        self.page.click_btn(path='采访-新增/编辑-按钮',param='保存')
        assert self.page.sub_menu_alert()

    #四：删除区
    @pytest.mark.run(order=-1)
    @pytest.mark.yun
    def test_above_delete(self):
        '''测试 删除预订单 点击上方删除按钮功能'''
        self.page.click_btn(path='查询按钮',param='查询')
        TimeUtils().sleep(1)
        self.page.check_order()
        TimeUtils().sleep(1)
        self.page.click_btn(path='右上按钮',param='4')
        TimeUtils().sleep(1)
        self.page.click_btn(path='采访-删除信息-确定',param='2')
        TimeUtils().sleep(1)
        assert self.page.sub_menu_alert()

    @pytest.mark.run(order=-2)
    @pytest.mark.yun
    def test_below_delete(self):
        '''测试 删除预订单 点击下方操作"..."里面的删除按钮功能'''
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep(1)
        self.page.click_select_list(name='删除')
        TimeUtils().sleep(1)
        self.page.click_btn(path='采访-删除信息-确定', param='2')
        TimeUtils().sleep(1)
        assert self.page.sub_menu_alert()

    @pytest.mark.yun
    def test_empty_order(self):
        '''测试 勾选预订单，点击上方的清空订单按钮功能'''
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep(1)
        self.page.check_order()
        TimeUtils().sleep(1)
        self.page.click_btn(path='右上按钮', param='2')
        TimeUtils().sleep(1)
        self.page.click_btn(path='采访-清空订单信息-确定',param='2')
        TimeUtils().sleep(1)
        assert self.page.sub_menu_alert()

    #五：其它
    @pytest.mark.yun
    def test_view_details(self):
        '''测试 跳转到详情页 点击下方的操作的详情按钮功能，通过判断标题名是否一样，验证是否成功'''
        self.page.click_btn(path='查询按钮',param='查询')
        TimeUtils().sleep(1)
        target_data_title = self.page.find_order_name_param(path='预订单标题名', param='1')
        TimeUtils().sleep(2)
        self.page.click_select_list(name='详情')
        TimeUtils().sleep(2)
        target_data_details_title = self.page.find_order_name(path='预订单详情内的标题')
        TimeUtils().sleep(1)
        assert target_data_title == target_data_details_title

    @pytest.mark.yun
    def test_double_click_view_details(self):
        '''测试 双击预订单，通过判断标题名是否一样，验证是否成功'''
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep(1)
        target_data_title = self.page.find_order_name_param(path='预订单标题名', param='3')
        self.page.double_click_target_order(path='表格某一行的数据',param='3',ctype='clicks')
        TimeUtils().sleep(1)
        target_data_details_title = self.page.find_order_name(path='预订单详情内的标题')
        TimeUtils().sleep(1)
        assert target_data_title == target_data_details_title

    @pytest.mark.yun
    def test_view_deficiency_information(self):
        '''测试 查看订单的催缺信息'''
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep()
        target_data_title = self.page.find_order_name_param(path='预订单标题名',param='2')
        self.page.click_btn(path='表格某一行的勾选框', param='2')
        TimeUtils().sleep(1)
        self.page.click_btn(path='右上按钮', param='3')
        TimeUtils().sleep(1)
        target_data_details_title = self.page.find_order_name_param(path='催缺信息页标题',param='2')
        assert target_data_title == target_data_details_title

    @pytest.mark.yun
    def test_export_file(self):
        '''测试 目标订单的导出功能(用状态码判断是否成功)'''
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep(1)
        self.page.check_order()
        TimeUtils().sleep(1)
        self.page.click_btn(path='右上按钮', param='5')
        TimeUtils().sleep(1)
        result = self.page.judge_by_url_and_status_code('http://192.168.1.35:8080/serviceapi/e/interview/file/ydsmE')      #(此url为导出文件时的目标接口)
        assert result

    @pytest.mark.yun
    def test_column_setting(self):
        '''测试 操作取消设置列(点击取消列设置前计算列数，点击后再计算列数)'''
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep(2)
        before_operation_columns = self.page.total_form_exist_columns()
        TimeUtils().sleep(2)
        self.page.click_btn(path='列设置按钮',param='列设置')
        TimeUtils().sleep(2)
        self.page.click_btn(path='列设置里面的选项', param='成员馆',ctype='click')
        TimeUtils().sleep(2)
        after_operation_columns = self.page.total_form_exist_columns() + 1
        self.page.refresh()  # 刷新页面
        TimeUtils().sleep(2)
        assert before_operation_columns == after_operation_columns

    @pytest.mark.yun
    def test_all_column_setting(self):
        '''测试 操作全选设置列(先取消列，再全选列)'''
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep(2)
        before_operation_columns = self.page.total_form_exist_columns()         #初始全选，12条
        TimeUtils().sleep(2)
        self.page.click_btn(path='列设置按钮', param='列设置')
        TimeUtils().sleep(2)
        self.page.click_btn(path='列设置里面的选项', param='成员馆', ctype='click')
        TimeUtils().sleep(2)
        self.page.click_btn(path='列设置里面的选项', param='书商', ctype='click')
        TimeUtils().sleep(2)
        self.page.click_btn(path='列设置里面的选项', param='预算', ctype='click')
        TimeUtils().sleep(2)
        operating_columns = self.page.total_form_exist_columns()        #取消3条，剩9条
        TimeUtils().sleep(2)
        self.page.refresh()     #刷新页面
        TimeUtils().sleep(2)
        self.page.click_btn(path='列设置按钮', param='列设置')
        TimeUtils().sleep(2)
        self.page.click_btn(path='列设置里面的全选',param=None,ctype='click')
        TimeUtils().sleep(2)
        after_operation_columns = self.page.total_form_exist_columns()      #全选，恢复12条
        TimeUtils().sleep(2)
        assert before_operation_columns == 12 and operating_columns == 9 and after_operation_columns == 12

    @pytest.mark.yun
    def test_set_work_order(self):
        '''测试 点击设为工作预订单,通过弹出窗口判断和class是否为on判断'''
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep(2)
        self.page.click_btn(path='设为工作预订单列', param='3')
        judge_result = self.page.verify_order_status(path='设为工作预订单列', param='5',label='class')
        assert 'on' in judge_result
        assert self.page.sub_menu_alert()

