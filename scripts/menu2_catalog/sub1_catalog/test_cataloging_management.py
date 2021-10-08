# -*- coding:utf-8 -*-
import logging
import time
from base.base_element import Element
import pytest
import allure
from selenium.webdriver.common.by import By
from page.menu2_catalog.sub1_catalog.page1_cataloging_management import CatalogingManagementPage
from utils.common_utils import ramdon_val, check_download, clear_download
from utils.driver_utils import DriverUtils
from utils.time_utils import TimeUtils
from model.marc_model import MARCModel

model = Element("model", ytype='json')


# 编目-编目管理 测试用例
class TestCatalogingManagement:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = CatalogingManagementPage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    @pytest.mark.yun
    @pytest.mark.reading
    def test_select(self):
        """ 测试 查询 功能 """
        self.page.click_btn(path='查询按钮', param='查询')
        assert self.page.sub_menu_alert()

    @pytest.mark.reading
    @pytest.mark.yun
    @pytest.mark.parametrize("libname", ["CS馆"])
    def test_select_lib(self, libname):
        """ 测试 成员馆查询 功能 """
        self.page.click_filter_list([1, 1, 1], libname)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()
        assert self.page.verify_filter(num=[1, 1, 1], label='placeholder') == libname

    @pytest.mark.parametrize(
        # ISBN、正题名、分类号、责任者、主题词、出版日期、语种、出版社、出版地、价格、其他责任者、其他责任者的正题名、ISRC、从编、题名、订购号、统一书刊号
        "isbn, ztm, flh, zrz, ztc, cbrq, yz, cbs, cbd, jg, qtzrz, qtzrzdztm, isrc, cb, tm, dgh, tyskh", [
            (9787, "故宫怪兽", "B81", "汤志伟", "传统工艺", 2019, "chi", "社会科学出版社", "中国", "99", "张保生", "1", "2", "3", "4", "5", "6"),
            (5410, "秘密花园", "G12", "江畅", "民法", 2018, "eng", "新星出版社", "上海", "98", "1", "2", "3", "4", "5", "6", "7")
        ])
    @pytest.mark.reading
    def test_select_bookmsg(self, isbn, ztm, flh, zrz, ztc, cbrq, yz, cbs, cbd, jg, qtzrz, qtzrzdztm, isrc, cb, tm, dgh, tyskh):
        """ 测试 书目信息的关键词查询 功能 """
        bookmsg = {"ztm": ["正题名", ztm], "flh": ["分类号", flh], "zrz": ["责任者", zrz], "ztc": ["主题词", ztc], "cbrq": ["出版日期", cbrq], "yz": ["语种", yz],
                   "cbs": ["出版社", cbs], "cbd": ["出版地", cbd], "jg": ["价格", jg], "qtzrz": ["其他责任者", qtzrz], "qtzrzdztm": ["其他责任者的正题名", qtzrzdztm],
                   "isrc": ["ISRC", isrc], "cb": ["丛编", cb], "tm": ["题名", tm], "dgh": ["订购号", dgh], "tyskh": ["统一书刊号", tyskh], "isbn": ["ISBN", isbn]}
        for k, v in bookmsg.items():
            self.page.click_filter_list([1, 3, 1], str(v[0]))
            time.sleep(1)

            self.page.click_filter_input("请输入搜索关键词", str(v[1]))
            self.page.click_btn(path='查询按钮', param="查询")

            time.sleep(1)
            if self.page.pagenum()[0] == "0":
                assert str(self.page.alert_exist(atype='yellowAlert')).find("暂无数据") is not -1
            assert self.page.sub_menu_alert()

    @pytest.mark.parametrize(
        # ISBN、正题名、分类号、责任者、主题词、出版日期、语种、出版社、出版地、价格、其他责任者、其他责任者的正题名、ISRC、从编、题名、订购号、统一书刊号
        "isbn, ztm, flh, zrz, ztc, cbrq, yz, cbs, cbd, jg, qtzrz, qtzrzdztm, isrc, cb, tm, dgh, tyskh", [
            (9787, "故宫怪兽", "B81", "汤志伟", "传统工艺", 2019, "chi", "社会科学出版社", "中国", "99", "张保生", "1", "2", "3", "4", "5", "6"),
            (5410, "秘密花园", "G12", "江畅", "民法", 2018, "eng", "新星出版社", "上海", "98", "1", "2", "3", "4", "5", "6", "7")
        ])
    @pytest.mark.reading
    def test_select_bookmsgs(self, isbn, ztm, flh, zrz, ztc, cbrq, yz, cbs, cbd, jg, qtzrz, qtzrzdztm, isrc, cb, tm, dgh, tyskh):
        """ 测试 多个书目信息搜索框一起查询 功能 """
        bookmsgs = {"msg1": ["责任者", zrz, "主题词", ztc, "出版日期", cbrq], "msg2": ["语种", yz, "出版社", cbs, "出版地", cbd],
                    "msg3": ["价格", jg, "其他责任者", qtzrz, "其他责任者的正题名", qtzrzdztm], "msg4": ["ISRC", isrc, "丛编", cb, "题名", tm],
                    "msg5": ["订购号", dgh, "统一书刊号", tyskh], "msg6": ["ISBN", isbn, "正题名", ztm, "分类号", flh]}
        self.page.add_or_remove_filter(otype='add')
        self.page.add_or_remove_filter(otype='add')
        time.sleep(1)
        for k, v in bookmsgs.items():
            try:
                self.page.click_filter_list([1, 3, 1], str(v.pop(0)))
                self.page.click_filter_list([1, 4, 1], str(v.pop(1)))
                if v[2] is not None:
                    self.page.click_filter_list([1, 5, 1], str(v.pop(2)))
                time.sleep(1)

                i = 0
                for element in self.page.click_filter_inputs():
                    element.clear()
                    element.send_keys(str(v[i]))
                    i += 1
            except IndexError as e:
                logging.error("数组越界了：%s" % e)
            self.page.click_btn(path='查询按钮', param="查询")

            time.sleep(1)

            if self.page.pagenum()[0] == "0":
                assert str(self.page.alert_exist(atype='yellowAlert')).find("暂无数据") is not -1
            assert self.page.sub_menu_alert()

    @pytest.mark.reading
    def test_select_bookmsg_item(self):
        """ 测试 1~3个关键词搜索框的加减 功能 """
        num = self.page.verify_filter_num("1")
        self.page.add_or_remove_filter(otype='add')
        self.page.add_or_remove_filter(otype='add')
        num2 = self.page.verify_filter_num("1")
        assert num < num2 and num + 2 == num2
        assert self.page.sub_menu_alert()
        self.page.add_or_remove_filter(otype='remove')
        num3 = self.page.verify_filter_num("1")
        assert num3 < num2 and num3 + 1 == num2
        assert self.page.sub_menu_alert()
        self.page.add_or_remove_filter(otype='add')
        num4 = self.page.verify_filter_num("1")
        assert num3 < num4 and num3 + 1 == num4
        assert self.page.sub_menu_alert()
        self.page.add_or_remove_filter(otype='remove')
        self.page.add_or_remove_filter(otype='remove')
        num5 = self.page.verify_filter_num("1")
        assert num5 < num4 and num5 + 2 == num4
        assert self.page.sub_menu_alert()

    @pytest.mark.reading
    def test_select_items(self):
        """ 测试 第二行筛选项隐藏和显示 功能 """
        text = self.page.output_text(path='筛选项', param=['1', '5'])
        if text == '更多筛选':
            self.page.click_btn(path='筛选项', param=['1', '5'])
            assert self.page.output_text(path='筛选项', param=['1', '5']) == '隐藏筛选'
            assert self.page.verify_display(path='筛选项', param=['2', '5']) is True
        elif text == '隐藏筛选':
            self.page.click_btn(path='筛选项', param=['1', '5'])
            assert self.page.output_text(path='筛选项', param=['1', '5']) == '更多筛选'
            assert self.page.verify_display(path='筛选项', param=['2', '5']) is False
        else:
            logging.error("获取字符串不正确")
        assert self.page.sub_menu_alert()

    @pytest.mark.reading
    @pytest.mark.parametrize("value", ["是", "否", "全部"])
    def test_select_proofread(self, value):
        """ 测试 查询审校 功能 """
        self.page.verify_filter_items()
        self.page.click_filter_list([2, 1, 1], value)
        self.page.click_btn(path='查询按钮', param="查询")
        if value == "是" and self.page.pagenum()[0] != "0":
            assert self.page.verify_checkbox('已审核') is True
        elif value == "否" and self.page.pagenum()[0] != "0":
            assert self.page.verify_checkbox('已审核') is False
        assert self.page.sub_menu_alert()

    @pytest.mark.reading
    @pytest.mark.parametrize("staff", ["创建人", "编目人", "审校人"])
    @pytest.mark.parametrize("value", ["吴君", "zll", "zhl"])
    def test_select_staff(self, staff, value):
        """ 测试 查询操作员 功能 """
        self.page.verify_filter_items()
        self.page.click_filter_list([2, 2, 1], staff)
        self.page.click_filter_list([2, 3, 1], value)
        self.page.click_btn(path='查询按钮', param="查询")
        time.sleep(1)
        if staff == "创建人" and self.page.pagenum()[0] != '0':
            assert value == self.page.verify_data("16")[0]
        assert self.page.sub_menu_alert()

    @pytest.mark.reading
    @pytest.mark.parametrize("date", ["创建日期", "编目日期", "审校日期"])
    def test_select_date(self, date):
        """ 测试 查询日期 功能 """
        self.page.verify_filter_items()
        self.page.click_filter_list([2, 4, 1], date)
        self.page.input_filter_date(start=TimeUtils().today(), end=TimeUtils().today())
        self.page.click_btn(path='查询按钮', param="查询")
        time.sleep(1)
        if date == "创建日期" and self.page.pagenum()[0] != '0':
            assert TimeUtils().today() == self.page.verify_data("17")[0]
        assert self.page.sub_menu_alert()

    @pytest.mark.reading
    @pytest.mark.parametrize("source", ["馆藏资源", "全部"])
    def test_select_source(self, source):
        """ 测试 查询检索来源 功能 """
        self.page.verify_filter_items()
        self.page.click_filter_list([2, 7, 1], source)
        self.page.click_btn(path='查询按钮', param="查询")
        time.sleep(1)
        if source == "馆藏资源" and self.page.pagenum()[0] != '0':
            assert source == self.page.verify_data("20")[0]
        assert self.page.sub_menu_alert()

    @pytest.mark.reading
    @pytest.mark.parametrize("column", [("成员馆", "ISBN", "分类号"), ("正题名", "责任者")])
    def test_select_column(self, column):
        """ 测试 列设置 功能 """
        before_columns = self.page.columns_data()
        self.page.click_btn(path='筛选项', param=[1, 6])
        time.sleep(1)
        for c in column:
            self.page.click_btn(path='列设置里面的选项', param=c, ctype='click')
            time.sleep(2)
        self.page.click_btn(path='查询按钮', param="查询")
        time.sleep(2)
        operating_columns = self.page.columns_data()
        assert before_columns > operating_columns
        assert self.page.sub_menu_alert()

        time.sleep(1)
        self.page.click_btn(path='筛选项', param=[1, 6])
        time.sleep(1)
        self.page.click_btn(path='列设置里面的全选', ctype='click')
        time.sleep(2)
        self.page.click_btn(path='查询按钮', param="查询")
        time.sleep(2)
        after_columns = self.page.columns_data()
        assert before_columns == after_columns
        assert self.page.sub_menu_alert()

    @pytest.mark.reading
    def test_select_collection(self):
        """ 测试 勾选 零馆藏书目 功能 """
        self.page.click_btn(path='编目-零馆藏书目-勾选框')
        time.sleep(2)
        assert self.page.verify_checkbox_collection() is True
        assert self.page.sub_menu_alert()

    @pytest.mark.reading
    def test_proofread(self):
        """ 测试 勾选审校 功能 """
        if self.page.pagenum()[0] != 0 and self.page.verify_checkbox('已审核') is True:
            self.page.click_btn(path='编目-审校/推荐-勾选框', param='已审核')
            time.sleep(1)
            assert self.page.verify_checkbox('已审核') is False
        elif self.page.pagenum()[0] != 0 and self.page.verify_checkbox('已审核') is False:
            self.page.click_btn(path='编目-审校/推荐-勾选框', param='已审核')
            time.sleep(1)
            assert self.page.verify_checkbox('已审核') is True
        assert str(self.page.alert_exist(atype='greenAlert')).find("操作成功") is not -1
        assert self.page.sub_menu_alert()

    @pytest.mark.reading
    def test_recommend(self):
        """ 测试 勾选荐购(单本书) 功能 """
        # 是否存在数据且没被勾选
        if self.page.pagenum()[0] != 0 and self.page.verify_checkbox('已推荐') is False:
            self.page.click_btn(path='编目-审校/推荐-勾选框', param='已推荐')
            # 是否弹出 图书推荐 这个窗口
            if self.page.dialog_exist('图书推荐'):
                self.page.click_btn(path='编目-推荐多选列表')
                # 多选列表是否有值
                if self.page.element_exist(path='编目-推荐多选列表-是否存在'):
                    self.page.click_btn(path='编目-推荐关闭按钮')
                    pytest.skip('请在 设置-图书推荐 中添加推荐主题')
                else:
                    self.page.click_btn(path='编目-推荐多选列表-值')
                    self.page.input_text(path='编目-推荐备注', content=ramdon_val(), itype='clickinput')
                    self.page.click_btn(path='菜单', param='推 荐')
                    assert str(self.page.alert_exist(atype='greenAlert')).find("操作成功") is not -1
                    assert self.page.sub_menu_alert()
                    assert self.page.verify_checkbox('已推荐') is True
                    assert self.page.verify_display(path='编目-拼音/推荐/分编弹窗', param='图书推荐') is False
            else: pytest.fail('没有弹出/找到 图书推荐 这个弹窗')
        else: pytest.skip('没有数据 或者 第一条数据已被勾选')

    @pytest.mark.reading
    def test_recommend_unchecked(self):
        """ 测试 勾选荐购(单本书)，未选择图书直接点击推荐 功能 """
        # 是否存在数据且没被勾选
        if self.page.pagenum()[0] != 0 and self.page.verify_checkbox('已推荐') is False:
            self.page.click_btn(path='编目-审校/推荐-勾选框', param='已推荐')
            # 是否弹出 图书推荐 这个窗口
            if self.page.dialog_exist('图书推荐'):
                self.page.click_btn(path='菜单', param='推 荐')
                assert str(self.page.alert_exist(atype='yellowAlert')).find("请选择关联主题") is not -1
                assert self.page.sub_menu_alert()
                self.page.click_btn(path='编目-推荐关闭按钮')
            else: pytest.fail('没有弹出/找到 图书推荐 这个弹窗')
        else: pytest.skip('没有数据 或者 第一条数据已被勾选')

    @pytest.mark.reading
    def test_recommend_cancel(self):
        """ 测试 勾选荐购(单本书)，直接点击取消 功能 """
        # 是否存在数据且没被勾选
        if self.page.pagenum()[0] != 0 and self.page.verify_checkbox('已推荐') is False:
            self.page.click_btn(path='编目-审校/推荐-勾选框', param='已推荐')
            # 是否弹出 图书推荐 这个窗口
            if self.page.dialog_exist('图书推荐'):
                self.page.click_btn(path='编目-推荐取消按钮')
                time.sleep(1)
                assert self.page.verify_checkbox('已推荐') is False
                assert self.page.sub_menu_alert()
                assert self.page.verify_display(path='编目-拼音/推荐/分编弹窗', param='图书推荐') is False
            else: pytest.fail('没有弹出/找到 图书推荐 这个弹窗')
        else: pytest.skip('没有数据 或者 第一条数据已被勾选')

    @pytest.mark.reading
    def test_recommend_multi_checked(self):
        """ 测试 勾选荐购(多本书) 功能 """
        if self.page.pagenum()[0] != 0:
            self.page.columns_data(num=0)
            time.sleep(1)
            self.page.click_btn(path='编目-右上更多/导出按钮', param='1')
            time.sleep(1)
            self.page.click_btn(path='编目-更多/导出单选列表', param='1')
            # 是否弹出 图书推荐 这个窗口
            time.sleep(1)
            if self.page.dialog_exist('图书推荐'):
                self.page.click_btn(path='编目-推荐多选列表')
                # 多选列表是否有值
                if self.page.element_exist(path='编目-推荐多选列表-是否存在'):
                    self.page.click_btn(path='编目-推荐关闭按钮')
                    pytest.skip('请在 设置-图书推荐 中添加推荐主题')
                else:
                    self.page.click_btn(path='编目-推荐多选列表-值')
                    self.page.input_text(path='编目-推荐备注', content=ramdon_val(), itype='clickinput')
                    self.page.click_btn(path='菜单', param='推 荐')
                    assert str(self.page.alert_exist(atype='greenAlert')).find("操作成功") is not -1
                    assert self.page.sub_menu_alert()
                    assert self.page.verify_checkbox('已推荐') is True
                    assert self.page.verify_display(path='编目-拼音/推荐/分编弹窗', param='图书推荐') is False
            else: pytest.fail('没有弹出/找到 图书推荐 这个弹窗')
        else: pytest.skip('没有数据')

    @pytest.mark.reading
    def test_recommend_multi_unchecked(self):
        """ 测试 取消勾选荐购(多本书) 功能 """
        if self.page.pagenum()[0] != 0 and self.page.verify_checkbox('已推荐') is True:
            self.page.columns_data(num=0)
            time.sleep(1)
            self.page.click_btn(path='编目-右上更多/导出按钮', param='1')
            time.sleep(1)
            self.page.click_btn(path='编目-更多/导出单选列表', param='2')
            time.sleep(1)
            assert self.page.verify_checkbox('已推荐') is False
            assert self.page.sub_menu_alert()
            assert self.page.verify_display(path='编目-拼音/推荐/分编弹窗', param='图书推荐') is False
        else: pytest.skip('没有数据 或者 第一条数据未被勾选')

    @pytest.mark.reading
    def test_recommend_multi_cancel(self):
        """ 测试 荐购未勾选取消勾选 功能 """
        if self.page.pagenum()[0] != 0 and self.page.verify_checkbox('已推荐') is False:
            self.page.click_btn(path='表格第一条数据')
            self.page.click_btn(path='编目-右上更多/导出按钮', param='1')
            self.page.click_btn(path='编目-更多/导出单选列表', param='2')
            assert self.page.verify_checkbox('已推荐') is False
            assert self.page.sub_menu_alert()
            assert str(self.page.alert_exist(atype='yellowAlert')).find("选中的书籍中没有已推荐的书籍") is not -1
            assert self.page.verify_display(path='编目-拼音/推荐/分编弹窗', param='图书推荐') is False
        else: pytest.skip('没有数据 或者 第一条数据已被勾选')

    @pytest.mark.reading
    @pytest.mark.parametrize("marcfbType", ["MARC21西文图书", "CNMARC中文图书"])
    def test_multi_marcfb_type(self, marcfbType):
        """ 测试 修改多条数据 marc分编类型 """
        if self.page.pagenum()[0] != 0:
            self.page.click_btn(path='表格第一条数据')
            self.page.click_btn(path='编目-右上更多/导出按钮', param='1')
            self.page.click_btn(path='编目-更多/导出单选列表', param='3')
            # 是否弹出 修改分编类型 这个窗口
            if self.page.dialog_exist('修改分编类型'):
                self.page.input_text(path='编目-修改分编类型-筛选项', content=marcfbType)
                time.sleep(1)
                self.page.click_btn(path='编目-修改分编类型-单选列表', param=marcfbType)
                time.sleep(1)
                self.page.click_btn(path='编目-修改分编类型-按钮', param='确定')
                assert str(self.page.alert_exist(atype='greenAlert')).find("操作成功") is not -1
                assert self.page.sub_menu_alert()
            else: pytest.fail('没有弹出/找到 修改分编类型 这个弹窗')
        else: pytest.skip('没有数据 或者 第一条数据已被勾选')

    @pytest.mark.reading
    @pytest.mark.parametrize("num", ["1", "2", "3", "4"])
    @pytest.mark.flaky(reruns=3)
    def test_download(self, num):
        """ 测试 下载文件 """
        clear_download()
        if self.page.pagenum()[0] != 0:
            time.sleep(2)
            self.page.click_btn(path='编目-右上更多/导出按钮', param='2')
            time.sleep(2)
            self.page.click_btn(path='编目-更多/导出单选列表', param=num)
            assert check_download(f="书目信息", load='2')
            assert self.page.sub_menu_alert()
            time.sleep(2)
        else: pytest.skip('没有数据')

    @pytest.mark.reading
    def test_delete(self):
        """ 测试 删除书目信息 功能 """
        if self.page.pagenum()[0] != 0 and self.page.verify_enable(path='右上按钮', param='4') is False:
            num = int(self.page.pagenum()[1])
            self.page.click_btn(path='表格第一条数据')
            assert self.page.verify_enable(path='右上按钮', param='4') is True
            self.page.click_btn(path='右上按钮', param='4')
            if self.page.pop_window_to_judge():
                self.page.click_btn(path='删除确定/取消', param='2')
                assert str(self.page.alert_exist(atype='greenAlert')).find("操作成功") is not -1
                assert num == int(self.page.pagenum()[1]) + 1
                assert self.page.sub_menu_alert()
            else: pytest.fail('没有弹出/找到 删除 弹窗')
        else: pytest.skip('没有数据')

    # @pytest.mark.parametrize(
    #     # ISBN、ISSN、ISRC、正题名、责任者、出版社、出版地、出版日期、出版周期、附件、分类号、统一书刊号、国内订购号、国外订购号、书目控制号、语种、页码、版次、价格、期刊价格、尺寸、一般资料标识
    #     # 一般性附注、主题词、摘要、丛编题名、丛编责任者、正题名拼音、责任者拼音、分辑名、副题名、分辑号、并列题名、其他责任者、版本与书目史附注、并列正题名、封面题名、著者、另一作者正题名
    #     "isbn, issn, isrc, ztm, zrz, cbs, cbd, cbrq, cbzq, fj, flh, tyskh, gndgh, gwdgh, smkzh, yz, ym, bc, jg, qkjg, cc"
    #     "ybzlbs, ybxfz, ztc, zy, cbtm, cbzrz, ztmpy, zrzpy, fjm, ftm, fjh, bltm, qtzrz, bbysmsfz, blztm, fmtm, zz, lyzzztm",
    #     [
    #         (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
    #          30, 31, 32, 33, 34, 35, 36, 37, 38, 39)
    #     ])
    # @pytest.mark.parametrize("value", [{"isbn": "1", "issn": "2", "isrc": "3", "ztm": "4", "zrz": "5", "cbs": "6", "cbd": "7", "cbrq": "8", "cbzq": "9", "fj": "10", "flh": "11", "tyskh": "12", "gndgh": "13", "gwdgh": "14", "smkzh": "15", "yz": "16", "ym": "17", "bc": "18", "jg": "19", "qkjg": "20", "cc": "21", "ybzlbs": "22", "ybxfz": "23", "ztc": "24", "zy": "25", "cbtm": "26", "cbzrz": "27", "ztmpy": "28", "zrzpy": "29", "fjm": "30", "ftm": "31", "fjh": "32", "bltm": "33", "qtzrz": "34", "bbysmsfz": "35", "blztm": "36", "fmtm": "37", "zz": "38", "lyzzztm": "39"}, {"isbn": "11", "issn": "12"}])
    @pytest.mark.parametrize("value", model["marc"])
    @pytest.mark.zll
    def test_marcEdit_add(self, value):
        """ 测试 简单编目 新增书目 功能 """
        print(value)

        

        # print(marcs.get_isbn())
        # print(marcs.get_issn())
        # self.page.click_btn(path='右上按钮', param='3')
        # time.sleep(1)
        # self.page.click_btn(path='MARC编辑-简单/MARC编目', param='简单编目')