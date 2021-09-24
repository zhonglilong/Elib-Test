# C:/test1
# -*- coding: utf-8 -*-
# @time : 
# Author : 小白
import pytest
import time
from utils.driver_utils import DriverUtils
from utils.time_utils import TimeUtils
from utils.common_utils import ramdon_val
from page.menu1_interview.sub2_acceptance.page2_booking_acceptance import BookingAcceptancePage

# 采访-图书验收处理-预订验收  测试用例

class TestBookingAcceptance:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = BookingAcceptancePage(drivers)

    def setup(self):
        self.page.model()
        self.page.menu()
        self.page.sub_menu()

    def teardown(self):
        DriverUtils.back_option()

    # @pytest.mark.zhl
    @pytest.mark.parametrize("name", ["全部", "妖灵会馆", "老君书阁"])
    def test_select_bookseller(self, name):
        """ 测试 预订单 筛选功能"""
        self.page.click_btn(path='查询按钮', param='查询')
        self.page.click_filter_list(name=name)
        self.page.click_btn(path='查询按钮', param="查询")
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    @pytest.mark.parametrize("isbn, ztm, flh, zrz, ftm, fjh, cbs, jg, cb, tm, dgh, tyskh",
                             [("9787", "罗小黑", "J649", "东篱子", "珍藏版", "灵枢篇", "出版社", "52.00", "%", "罗小黑", "%", "%")])
    def test_search_details(self, isbn, ztm, flh, zrz, ftm, fjh, cbs, jg, cb, tm, dgh, tyskh):
        """ 测试 书目信息 搜索功能 """
        ysdDetails = {"isbn": "ISBN", "ztm": "正题名", "flh": "分类号", "zrz": "责任者", "ftm": "副题名", "fjh": "分辑号", "cbs": "出版社"
            , "jg": "价格", " cb": "丛编", "tm": "题名", "dgh": "订购号", "tyskh": "统一书刊号"}
        for k, v in ysdDetails.items():
            self.page.click_filter_lists(2, str(v))
            time.sleep(1)
            if k == "isbn":
                self.page.click_filter_input("请输入搜索关键词", isbn)
            elif k == "ztm":
                self.page.click_filter_input("请输入搜索关键词", ztm)
            elif k == "flh":
                self.page.click_filter_input("请输入搜索关键词", flh)
            elif k == "zrz":
                self.page.click_filter_input("请输入搜索关键词", zrz)
            elif k == "ftm":
                self.page.click_filter_input("请输入搜索关键词", ftm)
            elif k == "fjh":
                self.page.click_filter_input("请输入搜索关键词", fjh)
            elif k == "cbs":
                self.page.click_filter_input("请输入搜索关键词", cbs)
            elif k == "jg":
                self.page.click_filter_input("请输入搜索关键词", jg)
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
    def test_receipt_dispose(self):
        """ 测试 书目信息 批量验收功能 """
        self.page.check_order()
        TimeUtils().sleep(2)
        self.page.click_check_accept()
        TimeUtils().sleep(2)
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_all_acceptance(self):
        """ 测试 书目信息 全部验收功能 """
        TimeUtils().sleep(2)
        self.page.click_all_accept()
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_alter_parts(self):
        """ 测试 书目信息 MARC编目下拉列表 """
        TimeUtils().sleep(2)
        # self.page.click_btn(path="表格第*条数据", param="12")
        self.page.click_marc_catalog()
        TimeUtils().sleep(2)
        self.page.click_type_parts(name="CNMARC中文期刊")
        TimeUtils().sleep(2)
        self.page.click_mtype_template(name="中文期刊模板")
        TimeUtils().sleep(2)
        self.page.click_mcheck_out(name="馆藏资源")
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        TimeUtils().sleep(2)
        self.page.account_status_of_judge()
        TimeUtils().sleep(2)
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_catalog_list(self):
        """ 测试 书目信息 简单编目下拉列表 """
        TimeUtils().sleep(2)
        self.page.click_simple_template()
        TimeUtils().sleep(2)
        self.page.click_simple_parts(name="CNMARC中文期刊")
        TimeUtils().sleep(2)
        self.page.click_type_template(name="馆藏资源")
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        TimeUtils().sleep(2)
        self.page.account_status_of_judge()
        TimeUtils().sleep(2)
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_parent_record(self):
        """ 测试 书目信息 父记录连接 """
        element = "el-button el-button--primary el-button--mini is-disabled"
        TimeUtils().sleep(2)
        self.page.click_simple_template()
        TimeUtils().sleep(2)
        classname = self.page.account_parent_record(path='编目-简单编目-添加父记录')
        if element in classname:
            self.page.click_btn(path='编目-简单编目-查看连接记录')
            TimeUtils().sleep(2)
            self.page.click_btn(path='父记录-移除')
            TimeUtils().sleep(2)
            self.page.click_btn(path='移除-确定')
            TimeUtils().sleep(2)
        self.page.click_btn(path='编目-简单编目-添加父记录')
        TimeUtils().sleep(2)
        self.page.input_text(path='添加父记录-查询输入框', param="2", content="1", itype="clearinput")
        TimeUtils().sleep(2)
        self.page.click_btn(path='添加父记录-查询')
        TimeUtils().sleep(2)
        self.page.click_btn(path='添加父记录-确认')
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_refer_record(self):
        """ 测试 书目信息 查询父记录 解除连接 """
        element = "el-button el-button--primary el-button--mini is-disabled"
        TimeUtils().sleep(2)
        self.page.click_simple_template()
        TimeUtils().sleep(2)
        classname = self.page.account_parent_record(path='编目-简单编目-查看连接记录')
        if element in classname:
            self.page.click_btn(path='编目-简单编目-添加父记录')
            TimeUtils().sleep(2)
            self.page.input_text(path='添加父记录-查询输入框', param="2", content="1", itype="clearinput")
            TimeUtils().sleep(2)
            self.page.click_btn(path='添加父记录-查询')
            TimeUtils().sleep(2)
            self.page.click_btn(path='添加父记录-确认')
            TimeUtils().sleep(2)
        self.page.click_btn(path='编目-简单编目-查看连接记录')
        TimeUtils().sleep(2)
        self.page.click_btn(path='父记录-移除')
        TimeUtils().sleep(2)
        self.page.click_btn(path='移除-确定')
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    @pytest.mark.parametrize("isbn, ztm, flh, zrz, cbs, isrc", [("1", "罗小黑", "J649", "方光光", "天津人民出版社", "%")])
    def test_parent_refer(self, isbn, ztm, flh, zrz, cbs, isrc):
        """ 测试 书目信息 父记录连接查询 """
        element = "el-button el-button--primary el-button--mini is-disabled"
        TimeUtils().sleep(2)
        self.page.click_simple_template()
        TimeUtils().sleep(2)
        classname = self.page.account_parent_record(path='编目-简单编目-添加父记录')
        if element in classname:
            self.page.click_btn(path='编目-简单编目-查看连接记录')
            TimeUtils().sleep(2)
            self.page.click_btn(path='父记录-移除')
            TimeUtils().sleep(2)
            self.page.click_btn(path='移除-确定')
            TimeUtils().sleep(2)
        self.page.click_btn(path='编目-简单编目-添加父记录')
        TimeUtils().sleep(2)
        Spinner = {"isbn": "ISBN", "ztm": "正题名", "flh": "分类号", "zrz": "责任者", "cbs": "出版社", "isrc": "ISRC"}
        for k, v in Spinner.items():
            self.page.click_filter_parent(1, str(v))
            TimeUtils().sleep(2)
            self.page.click_filter_parent(3, str(v))
            time.sleep(1)
            if k == "isbn":
                self.page.click_parent_input("2", isbn)
                self.page.click_parent_input("4", isbn)
            elif k == "ztm":
                self.page.click_parent_input("2", ztm)
                self.page.click_parent_input("4", ztm)
            elif k == "flh":
                self.page.click_parent_input("2", flh)
                self.page.click_parent_input("4", flh)
            elif k == "zrz":
                self.page.click_parent_input("2", zrz)
                self.page.click_parent_input("4", zrz)
            elif k == "cbs":
                self.page.click_parent_input("2", cbs)
                self.page.click_parent_input("4", cbs)
            elif k == "isrc":
                self.page.click_parent_input("2", isrc)
                self.page.click_parent_input("4", isrc)
            TimeUtils().sleep(2)
            self.page.click_btn(path='添加父记录-查询')
        self.page.click_btn(path='添加父记录-取消')
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_new_information(self):
        """ 测试 书目信息 新增 """
        TimeUtils().sleep(2)
        self.page.click_added()
        TimeUtils().sleep(2)
        self.page.input_text(path='简单编目-书目信息输入', param="11", content=ramdon_val(), itype="clickinputs")
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_style_information(self):
        """ 测试 书目信息 查询 """
        element = "display: none;"
        TimeUtils().sleep(2)
        self.page.click_refer()
        TimeUtils().sleep(2)
        classname = self.page.account_parent_style(path='编目-图书信息查询结果')
        if element in classname:
            self.page.click_btn(path='编目-图书信息查询结果勾选')
            TimeUtils().sleep(2)
            self.page.click_btn(path='编目-图书信息查询合并按钮')
            TimeUtils().sleep(2)
            self.page.click_btn(path='编目-图书信息合并提示窗口')
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_parent_reviser(self):
        """ 测试 书目信息 审校 """
        element = "ALT + O"
        TimeUtils().sleep(2)
        self.page.click_btn(path='右上按钮', param="3")
        classname = self.page.account_parent_style(path='编目-取消审校定位元素')
        TimeUtils().sleep(2)
        if element in classname:
            self.page.click_btn(path='编目-右下角按钮', param="取消审校")
            TimeUtils().sleep(2)
            self.page.click_btn(path='编目-审校/取消审校窗口确定')
            TimeUtils().sleep(2)
            self.page.click_btn(path='编目-右下角按钮', param="保存")
            TimeUtils().sleep(2)
        self.page.click_btn(path='编目-右下角按钮', param="审校")
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-审校/取消审校窗口确定')
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_add_fields(self):
        """ 测试 MARC编目 添加字段 """
        TimeUtils().sleep(2)
        self.page.click_add_fields()
        TimeUtils().sleep(2)
        self.page.input_text(path='编目-MARC编目-字段识别', param="2", content="110", itype="clickinputs")
        TimeUtils().sleep(2)
        self.page.input_text(path='编目-MARC编目-字段内容', param="2", content="▼a" + ramdon_val(), itype="clickinputs")
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_delete_fields(self):
        """ 测试 MARC编目 删除字段 重置恢复 """
        TimeUtils().sleep(2)
        self.page.click_delete_fields()
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-MARC编目-上方按钮', param="重置")
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-粘贴网页MARC-重置恢复')
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        assert self.page.sub_menu_alert()

    # @pytest.mark.zhl
    def test_marc_cope(self):
        """ 测试 MARC编目 粘贴网页MARC """
        TimeUtils().sleep(2)
        self.page.click_btn(path='右上按钮', param="3")
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-简单编目/MARC编目', param="2")
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-MARC编目-上方按钮', param="粘贴网页MARC")
        TimeUtils().sleep(2)
        self.page.input_text(path='编目-粘贴网页MARC-书目信息输入', content=
        "000    nam0 2200241   450" +"\n" +
        "001    011420239" +"\n" +
        "005    20210923114053.0" +"\n" +
        "010    |a978-7-302-58350-9|dCNY39.00" +"\n" +
        "100    |a20210923d2021    em y0chiy50      ea" +"\n" +
        "101 0  |achi" +"\n" +
        "102    |aCN|b110000" +"\n" +
        "105    |aa   z   000yy" +"\n" +
        "106    |ar" +"\n" +
        "200 1  |a人工智能导论|9ren gong zhi neng dao lun|f马月坤，陈昊主编" +"\n" +
        "210    |a北京|c清华大学出版社|d2021" +"\n" +
        "215    |a263页|c图|d26cm" +"\n" +
        "300    |a人工智能通识教材" +"\n" +
        "330    |a全书共13章，第1章介绍人工智能的基本概念、发展简史，并着重介绍了人工智能的主要研究内容与各种应用，以开阔读者的视野，引导读者进入人工智能各个研究领域；第2-6章阐述人工智能的基本原理和技术基础，重点论述知识图谱、自然语言处理、智能语音、计算机视觉、机器学习和神经网络等关键通用技术，为后续章节介绍行业应用做知识储备和技术铺垫；第7-12章介绍人工智能目前在行业中的应用，包括智能交通、智能商务、智能司法、智能教育、智能医疗、其他行业智能应用等6个模块，读者可以专业需要选择其中几个行业应用案例进行重点学习，感受到人工智能在专业中的融合；第13章介绍当前人工智能研究存在的热点问题和伦理争议。" +"\n" +
        "606 0  |a人工智能|j教材" +"\n" +
        "690    |aTP18|v5" +"\n" +
        "701  0 |a马月坤|9ma yue kun|4主编" +"\n" +
        "701  0 |a陈昊|9chen hao|4主编" +"\n" +
        "801  0 |aCN|b91MARC|c20210923" , itype="clickinputs")
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-粘贴网页MARC-确定')
        TimeUtils().sleep(2)
        self.page.click_btn(path='编目-右下角按钮', param="保存")
        assert self.page.sub_menu_alert()