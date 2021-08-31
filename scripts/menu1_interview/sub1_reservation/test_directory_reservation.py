# -*- coding:utf-8 -*-
import pytest
import allure
from page.menu1_interview.sub1_reservation.page1_directory_reservation import DirectoryReservationPage
from utils.driver_utils import DriverUtils
from utils.time_utils import TimeUtils


# 采访-征订目录预订 测试用例
class TestDirectoryReservation:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = DirectoryReservationPage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    @allure.feature('【征订目录预订】')
    @allure.story('【征订目录预订】查询成功分支')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/zdsmyd")
    # @pytest.mark.skip
    @pytest.mark.yun
    def test_select(self, logger):
        """ 测试 查询 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @allure.feature('【征订目录预订】')
    @allure.story('【征订目录预订】筛选书商成功分支')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/zdsmyd")
    @pytest.mark.parametrize("name", ["TJ_gys | 新华书店"])
    # @pytest.mark.yun
    def test_select_bookseller(self, name):
        """ 测试 筛选书商 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_filter_list(name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    @allure.feature('【征订目录预订】')
    @allure.story('【征订目录预订】筛选日期成功分支')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/zdsmyd")
    @pytest.mark.reading
    @pytest.mark.yun
    def test_select_date(self):
        """ 测试 筛选日期 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.input_filter_date(start=TimeUtils().today(), end=TimeUtils().today())
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @allure.feature('【征订目录预订】')
    @allure.story('【征订目录预订】筛选征订目录名称成功分支')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/zdsmyd")
    @pytest.mark.parametrize("name", [1, 2, 3])
    @pytest.mark.yun
    def test_select_name(self, name):
        """ 测试 筛选征订目录名称 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_filter_input(name)
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @allure.feature('【征订目录预订】')
    @allure.story('【征订目录预订】添加成功')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/zdsmyd")
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.run(order=1)
    # @pytest.mark.yun
    def test_add(self):
        """ 测试 新增征订目录 功能
        这个用例不能运行太快，去掉sleep会提示 ElementNotInteractableException
        使用pytest.mark.flaky提高用例成功率
        """
        TimeUtils().sleep(1)
        self.page.click_btn(path='右上按钮', param='1')
        TimeUtils().sleep(1)
        self.page.input_text(path='新增/编辑-输入', content=DriverUtils.ramdon_val(), param='征订目录')
        TimeUtils().sleep(1)
        self.page.click_btn(path='新增/编辑-按钮', param='保存')
        assert self.page.sub_menu_alert()

    @allure.feature('【征订目录预订】')
    @allure.story('【征订目录预订】修改成功')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/zdsmyd")
    @pytest.mark.flaky(reruns=3)
    # @pytest.mark.yun
    def test_update(self):
        """ 测试 修改征订目录 功能 """
        TimeUtils().sleep(1)
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep(1)
        self.page.double_click_order()
        TimeUtils().sleep(1)
        self.page.input_text(path='新增/编辑-输入', content=DriverUtils.ramdon_val(), param='征订目录')
        TimeUtils().sleep(1)
        self.page.click_btn(path='新增/编辑-按钮', param='保存')
        assert self.page.sub_menu_alert()

    @allure.feature('【征订目录预订】')
    @allure.story('【征订目录预订】删除成功')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/zdsmyd")
    @pytest.mark.run(order=-1)
    # @pytest.mark.yun
    def test_delete(self):
        """ 测试 删除征订目录 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.check_order()
        self.page.click_btn(path='右上按钮', param='2')
        self.page.click_btn(path='删除信息-确定', param='2')
        assert self.page.sub_menu_alert()

    @allure.feature('【征订目录预订详情】')
    @allure.story('【征订目录预订】查询成功分支')
    @allure.severity('critical')
    @allure.testcase("/elib/#/acquisition/tsydgl/zdsmlb?zdpcid=8b16efd1d55242378938fc2ff2cce293")
    # @pytest.mark.yun
    def test_select_list(self):
        """ 测试详情页的 查询 功能 """
        self.page.click_order_link()
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()
