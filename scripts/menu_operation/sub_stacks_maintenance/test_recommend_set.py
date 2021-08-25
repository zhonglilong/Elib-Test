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
        self.page.input_text(path='登录用户名', content="autotest")
        self.page.input_text(path='登录密码', content="Td123456")
        self.page.click_btn(path='登录按钮')

    def setup(self):
        DriverUtils.back_option()
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    def test_select(self):
        """ 测试 查询 功能 """
        # 点击查询，无错误弹窗
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

        # 选择成员馆为全部，点击查询，无错误弹窗
        self.page.click_filter_list(name='全部', cont='1')
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

        # 选择书库名为（默认不可删除的书库），成员馆保持不变（上一步为全部），点击查询，无错误弹窗
        self.page.click_filter_list(name='京东书目', cont='2')
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

        # 选择成员馆为拓迪总书库，书库名保持不变（上一步为京东书目）点击查询，无错误弹窗
        self.page.click_filter_list(name='拓迪总书库', cont='1')
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    def test_add(self):
        """测试 新增 功能 """
        # 荐购设置右上按钮1为新增，2为删除。点击新增，无错误弹窗
        TimeUtils.sleep(2)
        self.page.click_btn(path='右上按钮', param='1')
        assert self.page.sub_menu_alert() and self.page.pop_sidewindow_to_judge()


        # 成员馆设置为空点击保存，有错误弹窗
        self.page.click_btn(path='复选框叉', param='成员馆')
        self.page.click_btn(path='侧边弹窗底部按钮', param='保存')
        assert self.page.sub_menu_alert() == False

        # 选择成员馆为lxy测试一号馆，点击保存，无错误弹窗，查询成员馆lxy测试一号馆，无错误提示框，有数据
        TimeUtils.sleep(4)
        self.page.side_click_filter_list(name='成员馆', value='lxy测试一号馆')
        self.page.click_btn(path='侧边弹窗底部按钮', param='保存')
        self.page.click_filter_list(name='lxy测试一号馆', cont='1')
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert() and self.page.order()

        # 选择成员馆为测试用一号馆，测试用二号馆，点击保存，无错误弹窗，查询成员馆测试用一号馆，无错误提示框，有数据
        self.page.click_btn(path='右上按钮', param='1')
        TimeUtils.sleep(1)
        self.page.click_btn(path='复选框叉', param='成员馆')
        self.page.side_clicks_filter_list(name='成员馆', value=['测试用一号馆lxy', '测试用二号馆lxy'])
        self.page.click_btn(path='侧边弹窗底部按钮', param='保存')
        self.page.click_filter_list(name='测试用一号馆lxy', cont='1')
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert() and self.page.order()

        # 选择成员馆为lxy测试二号馆，是否启用选择否，书库选择京东书目，点击重置，无错误弹窗，此时信息为初始信息
