# -*- coding:utf-8 -*-
import pytest
from page.menu_operation.sub_stacks_maintenance.page_recommend_set import RecommendSet
from utils.driver_utils import DriverUtils
from utils.time_utils import TimeUtils


# 运营-荐购设置 测试用例
class TestRecommendSet:
    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = RecommendSet(drivers)
        self.page.input_text(path='登录用户名', content="lxy")
        self.page.input_text(path='登录密码', content="Td123456")
        self.page.click_btn(path='登录按钮')

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()
