# -*- coding:utf-8 -*-
import json
import pytest
import time
from utils.driver_utils import DriverUtils
from base.config import *
from _pytest import terminal

driver = None


@pytest.fixture(scope='session', autouse=True)
def drivers():
    global driver
    driver = DriverUtils.get_driver()
    # driver.get(URL+"/elib/#/login")
    yield driver
    time.sleep(3)
    DriverUtils.quit_driver()
    return driver


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """ 收集测试结果 """
    result = "#### total：{0}，passed：{1}，failed：{2} \n" \
             "#### error：{3}，skipped：{4} \n" \
             "#### time：{5} seconds".format(
        terminalreporter._numcollected,
        len(terminalreporter.stats.get('passed', [])),
        len(terminalreporter.stats.get('failed', [])),
        len(terminalreporter.stats.get('error', [])),
        len(terminalreporter.stats.get('skipped', [])),
        time.time() - terminalreporter._sessionstarttime
    )
    DING_MSG["markdown"]["text"] = result
