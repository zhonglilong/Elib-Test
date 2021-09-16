# C:/test1@pytest.fixture(scope='function', autouse=True)
# -*- coding: utf-8 -*-
# @time : 
# Author : 小白
import pytest
import time
from utils.driver_utils import DriverUtils
from utils.time_utils import TimeUtils
from page.menu1_interview.sub2_acceptance.page1_receiving_report import ReceivingReportPage

# 采访-图书验收处理-验收单管理  测试用例
class TestReceivingReport:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = ReceivingReportPage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    # @allure.feature('【验收单管理】')
    # @allure.story('【验收单管理】查询成功分支')
    # @allure.severity('critical')
    # @allure.testcase("/elib/#/acquisition/tsydgl/zdsmyd")

    # @pytest.mark.zhl
    def test_select(self, logger):
        """ 测试 查询 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    @pytest.mark.parametrize("name", ["书商"])
    def test_select_bookseller(self, name):
        """ 测试 筛选书商 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_filter_list(name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    @pytest.mark.parametrize("ysd, ss", [("壹", "新华书店"), ("兰花亭", "中华书店")])
    def test_select_bookmsg(self, ysd, ss):
        """ 测试 筛选验收单，书商 """
        bookmsg = {"ysd": "验收单", "ss": "书商"}
        for k, v in bookmsg.items():
            self.page.click_filter_lists(1, str(v))
            time.sleep(1)
            if k == "ysd":
                self.page.click_filter_input("请输入搜索关键词", ysd)
            elif k == "ss":
                self.page.click_filter_input("请输入搜索关键词", ss)
            self.page.click_btn(path='查询按钮', param="查询")
            assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    @pytest.mark.reading
    def test_select_date(self):
        """ 测试 筛选日期 功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.input_filter_date(start=TimeUtils().today(), end=TimeUtils().today())
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    @pytest.mark.parametrize("founder", ["全部", "高桥靓仔", "小红", "小白", "小黑", "lxh2"])
    def test_select_founder(self, founder):
        """ 测试 筛选订单状态 功能 """
        # 创建日期算做3个单位长度
        self.page.click_filter_lists(5, founder)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.run(order=1)
    def test_add(self):
        """ 测试 新增验收单 功能
        这个用例不能运行太快，去掉sleep会提示 ElementNotInteractableException
        使用pytest.mark.flaky提高用例成功率
        """
        TimeUtils().sleep(1)
        self.page.click_btn(path='右上按钮', param='1')
        TimeUtils().sleep(1)
        self.page.input_text(path='采访-新增/编辑-输入', content=DriverUtils.ramdon_val(), param='验收单', itype="clickinput")
        TimeUtils().sleep(1)
        self.page.click_btn(path='采访-新增/编辑-按钮', param='保存')
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_update(self):
        """ 测试 编辑验收单 功能 """
        TimeUtils().sleep(2)
        self.page.click_compile_Details()
        TimeUtils().sleep(2)
        self.page.input_text(path='采访-验收单-备注', content="老弟好", param='验收单', itype="clearinput")
        TimeUtils().sleep(2)
        self.page.click_btn(path='采访-新增/编辑-按钮', param='保存')
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    @pytest.mark.parametrize("isbn, ztm, ydd, ysr, flh, zrz, cbs, jg, zdfs, jzlx, cb, tm, dgh, tyskh",
                             [("9787", "罗小黑", "妖灵会馆", "小白", "J649", "王", "出版社", "52.00", "平装", "纸张", "%", "罗小黑", "%", "%")])
    def test_search_details(self, isbn, ztm, ydd, ysr, flh, zrz, cbs, jg, zdfs, jzlx, cb, tm, dgh, tyskh):
        """ 测试 验收单详情 搜索功能 """
        self.page.click_receipt_Details()
        TimeUtils().sleep(2)
        ysdDetails = {"isbn": "ISBN", "ztm": "正题名", "ydd": "预订单", "ysr": "验收人", "flh": "分类号",
                      "zrz": "责任者", "cbs": "出版社", "jg": "价格", "zdfs": "装订方式", "jzlx": "介质类型",
                      " cb": "丛编", "tm": "题名", "dgh": "订购号", "tyskh": "统一书刊号"}
        for k, v in ysdDetails.items():
            self.page.click_filter_lists(1, str(v))
            time.sleep(1)
            if k == "isbn":
                self.page.click_filter_input("请输入搜索关键词", isbn)
            elif k == "ztm":
                self.page.click_filter_input("请输入搜索关键词", ztm)
            elif k == "ydd":
                self.page.click_filter_input("请输入搜索关键词", ydd)
            elif k == "ysr":
                self.page.click_filter_input("请输入搜索关键词", ysr)
            elif k == "flh":
                self.page.click_filter_input("请输入搜索关键词", flh)
            elif k == "zrz":
                self.page.click_filter_input("请输入搜索关键词", zrz)
            elif k == "jg":
                self.page.click_filter_input("请输入搜索关键词", jg)
            elif k == "zdfs":
                self.page.click_filter_input("请输入搜索关键词", zdfs)
            elif k == "jzlx":
                self.page.click_filter_input("请输入搜索关键词", jzlx)
            elif k == "cb":
                self.page.click_filter_input("请输入搜索关键词", cb)
            elif k == "tm":
                self.page.click_filter_input("请输入搜索关键词", tm)
            elif k == "dgh":
                self.page.click_filter_input("请输入搜索关键词", dgh)
            elif k == "tyskh":
                self.page.click_filter_input("请输入搜索关键词", tyskh)
            self.page.click_btn(path='查询按钮', param="查询")
            assert self.page.sub_menu_alert()
        TimeUtils().sleep(2)
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_compile_details(self):
        """测试 验收单详情 编辑功能"""
        # 编辑验收单中的书目信息，保存时一般无法正常保存
        self.page.click_receipt_Details()
        TimeUtils().sleep(2)
        self.page.click_compile_Details()
        self.page.input_text(path='采访-验收单-备注', content="老弟好", param='验收单', itype="clearinput")
        self.page.click_btn(path='采访-新增/编辑-按钮', param='保存')
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_delete_details(self):
        """测试 验收单详情 删除功能"""
        self.page.click_receipt_Details()
        TimeUtils().sleep(2)
        self.page.click_btn(path='查询按钮', param='查询')
        TimeUtils().sleep(2)
        self.page.click_btn(path='表格第一条数据操作列', ctype='moveClick')
        TimeUtils().sleep(2)
        self.page.click_btn(path='操作列选项', param='删除')
        TimeUtils().sleep(2)
        self.page.click_btn(path='采访-删除信息-确定', param='2')
        assert self.page.sub_menu_alert()


