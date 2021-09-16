# -*- coding:utf-8 -*-
import pytest
import time
from utils.driver_utils import DriverUtils
from base.log_config import LogConfig
from base.config import *

driver = None
log = LogConfig()


@pytest.fixture(scope='session', autouse=True)
def drivers():
    global driver
    driver = DriverUtils.get_driver()
    # driver.get(URL+"/elib/#/login")
    yield driver
    time.sleep(2)
    DriverUtils.quit_driver()
    return driver


@pytest.fixture(scope='session', autouse=True)
def logger():
    return log


def pytest_configure(config):
    marker_list = ["login", "public", "yun", "reading", "zll", "zhl", "skx", "skx1"]  # 标签名集合
    for markers in marker_list:
        config.addinivalue_line("markers", markers)


def pytest_collection_modifyitems(items):
    """ 解决pytest输出信息是乱码的问题 """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     # 获取钩子方法的调用结果
#     out = yield
#     # print('用例执行结果', out)
#
#     # 3. 从钩子方法的调用结果中获取测试报告
#     report = out.get_result()
#
#     log.info('测试报告：%s' % report)
#     log.info('步骤：%s' % report.when)
#     log.info('nodeid：%s' % report.nodeid)
#     log.info('执行结果: %s' % report.outcome)


# def pytest_terminal_summary(terminalreporter, exitstatus, config):
#     """ 收集测试结果 """
#     result = "#### total：{0}，passed：{1}，failed：{2} \n" \
#              "#### error：{3}，skipped：{4} \n" \
#              "#### time：{5} seconds".format(
#         terminalreporter._numcollected,
#         len(terminalreporter.stats.get('passed', [])),
#         len(terminalreporter.stats.get('failed', [])),
#         len(terminalreporter.stats.get('error', [])),
#         len(terminalreporter.stats.get('skipped', [])),
#         time.time() - terminalreporter._sessionstarttime
#     )
#     DING_MSG["markdown"]["text"] = result
