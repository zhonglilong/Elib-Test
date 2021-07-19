# -*- coding:utf-8 -*-
import pytest
import allure
from page.menu1_interview.sub1_reservation.page2_reservation_management import ReservationManagementPage
from utils.driver_utils import DriverUtils
from utils.time_utils import TimeUtils

# 采访-预订单管理 测试用例
class TestReservationManagement:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = ReservationManagementPage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    @allure.feature('【预订单管理】')
    @allure.story('【预订单管理】查询成功分支')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/yddgl")
    @pytest.mark.skip
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @allure.feature('【预订单管理】')
    @allure.story('【预订单管理】筛选 预订单/书商 成功分支')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/yddgl")
    @pytest.mark.parametrize("name, content", [("预订单", "1"), ("书商", "新华书店")])
    @pytest.mark.skip
    def test_select_order_or_bookseller(self, name, content):
        """ 测试 筛选预订单/书商 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_filter_list(name=name)
        self.page.input_text(path='筛选-输入框', param='请输入搜索关键词', content=content)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @allure.feature('【预订单管理】')
    @allure.story('【预订单管理】筛选日期成功分支')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/yddgl")
    @pytest.mark.skip
    def test_select_date(self):
        """ 测试 筛选日期 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.input_filter_date(start=TimeUtils().today(), end=TimeUtils().today())
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @allure.feature('【预订单管理】')
    @allure.story('【预订单管理】添加成功')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/yddgl")
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.run(order=1)
    # @pytest.mark.skip
    def test_add(self):
        """ 测试 新增预订单 功能 """
        self.page.click_btn(path='右上按钮', param='1')
        self.page.input_text(path='新增/编辑-输入', content=DriverUtils.ramdon_val(), param='预订单')
        self.page.click_btn(path='新增/编辑-按钮', param='保存')
        assert self.page.sub_menu_alert()