# -*- coding:utf-8 -*-
import pytest
import allure
from page.menu1_interview.sub1_reservation.page1_directory_reservation import DirectoryReservationPage
from utils.driver_utils import DriverUtils


# 采访-征订目录预订 测试用例
class TestDirectoryReservation:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = DirectoryReservationPage(drivers)

    def setup(self):
        self.page.click_model("采访")
        self.page.click_menu("图书预订处理")
        self.page.click_sub_menu(1, "征订目录预订")

    def teardown(self):
        DriverUtils.back_option()

    @allure.feature('【征订目录预订】查询功能')
    @allure.story('【征订目录预订】查询成功分支')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/zdsmyd")
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_sub_menu_btn(" 查询")
        assert self.page.sub_menu_alert()

    @allure.feature('【征订目录预订】筛选书商')
    @allure.story('【征订目录预订】筛选书商成功分支')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/zdsmyd")
    def test_select_bookseller(self):
        """ 测试 筛选书商 功能"""
        self.page.click_sub_menu_btn(" 查询")
        self.page.click_sub_menu_filter("1")
        self.page.click_sub_menu_filter_list()
        self.page.click_sub_menu_btn(" 查询")
        assert self.page.sub_menu_alert()

    @allure.feature('【征订目录预订】筛选日期')
    @allure.story('【征订目录预订】筛选日期成功分支')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/zdsmyd")
    def test_select_date(self):
        """ 测试 筛选日期 功能"""
        self.page.click_sub_menu_btn(" 查询")
        self.page.input_sub_menu_filter_date("2021-03-16", "2021-03-16")
        self.page.click_sub_menu_btn(" 查询")
        assert self.page.sub_menu_alert()

    @allure.feature('【征订目录预订】筛选征订目录名称')
    @allure.story('【征订目录预订】筛选征订目录名称成功分支')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/zdsmyd")
    @pytest.mark.parametrize("name", [1, 2, 3])
    def test_select_name(self, name):
        """ 测试 筛选征订目录名称 功能"""
        self.page.click_sub_menu_btn(" 查询")
        self.page.click_sub_menu_filter_input(name)
        self.page.click_sub_menu_btn(" 查询")
        assert self.page.sub_menu_alert()


    def test_add(self):
        """ 测试 新增征订目录 功能"""
        pass


    @allure.feature('【征订目录预订详情】查询功能')
    @allure.story('【征订目录预订】查询成功分支')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/zdsmlb?zdpcid=8b16efd1d55242378938fc2ff2cce293")
    def test_select_list(self):
        """ 测试详情页的 查询 功能 """
        self.page.click_sub_menu_list(3)
        self.page.click_sub_menu_btn(" 查询 ")
        assert self.page.sub_menu_alert()
