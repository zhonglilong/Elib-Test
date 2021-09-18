# -*- coding:utf-8 -*-
import pytest
import time
from page.menu9_special.sub4_resource_management.page1_resource_classify import ResourceClassifyPage
from utils.driver_utils import DriverUtils
from utils.time_utils import TimeUtils
from utils.common_utils import *


# 特色-资源分类 测试用例
class TestResourceClassify:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = ResourceClassifyPage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    @pytest.mark.skx
    def test_select(self, logger):
        """ 测试 查询按钮 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("data", ["分类一", "分类二", "分类三"])
    @pytest.mark.skx
    def test_select_name(self, data):
        """ 测试 筛选分类名称 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_filter_input(data)
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("text", [random_val()])
    @pytest.mark.skx
    def test_add(self, text):
        """ 测试 新增 功能
        """
        time.sleep(1)  # 这里必须延迟后才能点击
        self.page.click_btn(path='右上按钮', param='1')
        time.sleep(1)  # 这里必须延迟后才能点击
        self.page.input_text(path='新增/编辑-输入', content=text, param='分类名称')
        self.page.click_btn(path='侧边弹窗底部按钮', param='保存')
        assert self.page.sub_menu_alert()

    @pytest.mark.skx
    def test_delete(self):
        """ 测试 删除 功能
        """
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_btn(path='表格第一条数据')
        self.page.click_btn(path='右上按钮', param='3')
        self.page.click_btn(path='特色-删除弹框-确定/取消', param='2')
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("text", [random_val()])
    @pytest.mark.skx1
    def test_redact(self, text):
        """ 测试 编辑 功能
        """
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_btn(path='表格第一条数据')
        self.page.click_btn(path='右上按钮', param='2')
        time.sleep(1)
        self.page.input_text(path='新增/编辑-输入', content=text, param='分类名称', itype="clearallinput")
        assert self.page.sub_menu_alert()

    @pytest.mark.parametrize("text", [random_val()])
    @pytest.mark.skx
    def test_add_del(self, text):
        """ 测试 新增后删除功能
        """
        time.sleep(1)  # 这里必须延迟后才能点击
        self.page.click_btn(path='右上按钮', param='1')
        time.sleep(1)  # 这里必须延迟后才能点击
        self.page.input_text(path='新增/编辑-输入', content=text, param='分类名称')
        self.page.click_btn(path='侧边弹窗底部按钮', param='保存')
        self.page.click_btn(path='查询按钮', param='查询')
        time.sleep(2)
        self.page.click_btn(path='表格第一条数据')
        self.page.click_btn(path='右上按钮', param='3')
        self.page.click_btn(path='特色-删除弹框-确定/取消', param='2')
        assert self.page.sub_menu_alert()


