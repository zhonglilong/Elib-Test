# -*- coding:utf-8 -*-
import pytest
from page.menu8_operation.sub_stacks_maintenance.page_recommend_set import RecommendSet
from utils.driver_utils import DriverUtils
from utils.time_utils import TimeUtils

# 运营-荐购设置 测试用例
class TestRecommendSet:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = RecommendSet(drivers)
        self.page.login()      # 为单列执行时创建

    def setup(self):
        DriverUtils.back_option()
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    @pytest.mark.yun
    @pytest.mark.parametrize("name, sort", [("default", "default"), ("全部", "1"), ("京东书目", "2"), (["全部", "1"], ["京东书目", "2"])])
    def test_select(self, name, sort):
        """ 测试 查询 功能 """
        self.page.select_data(import1=name, import2=sort)

    @pytest.mark.yun
    @pytest.mark.parametrize("id, userd, tableName,", [("lxy测试一号馆", "2", "京东书目"), (["测试用一号馆lxy", "lxy测试二号馆"], "1", "京东书目")])
    def test_add(self, id, userd, tableName):
        """测试 新增 功能 """
        TimeUtils.sleep(2)
        self.page.click_btn(path='右上按钮', param='1')
        assert self.page.sub_menu_alert() and self.page.pop_sidewindow_to_judge()
        self.page.data_configuration(id, userd, tableName)

    @pytest.mark.yun
    @pytest.mark.parametrize("id", ["测试用二号馆lxy", "测试用二号馆lxy"])
    def test_readd(self, id):
        """  重复新增已有馆 (前置：已执行新增测试用例)"""
        TimeUtils.sleep(2)
        self.page.click_btn(path='右上按钮', param='1')
        TimeUtils.sleep(1)
        self.page.side_click_filter_list(name='成员馆', value=id)
        self.page.click_btn(path='侧边弹窗底部按钮', param='保存')
        assert self.page.sub_menu_alert() is False

    def test_idnull_add(self):
        """  新增时馆为空  """
        TimeUtils.sleep(2)
        self.page.click_btn(path='右上按钮', param='1')
        TimeUtils.sleep(1)
        self.page.click_btn(path='复选框叉', param='成员馆')
        self.page.click_btn(path='侧边弹窗底部按钮', param='保存')

    def test_reset(self):
        """  重置测试 """
        pass # 日后补充

    @pytest.mark.yun
    @pytest.mark.parametrize("id, newid, userd, tableName,", [("lxy测试一号馆", "lxy测试一号馆", "1", "京东书目"), ("lxy测试一号馆", ["lxy测试一号馆", "lxy测试二号馆"], "2", "京东书目")])
    def test_update(self, id, newid, userd, tableName):
        """测试 编辑 功能 """
        self.page.data_update(id, newid, userd, tableName)

    @pytest.mark.yun
    @pytest.mark.parametrize("id", ["测试用二号馆lxy", "lxy测试一号馆"])
    def test_delete(self, id):
        """测试 删除 功能 """
        self.page.data_del(id)
