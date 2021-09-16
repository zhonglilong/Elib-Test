# -*- coding:utf-8 -*-
import pytest
from base.config import *
from utils.driver_utils import *


def check_dir():
    if not os.path.exists(BASE_DIR + "\\resources\\log"):
        os.makedirs(BASE_DIR + "\\resources\\log")
    if not os.path.exists(BASE_DIR + "\\resources\\picture"):
        os.makedirs(BASE_DIR + "\\resources\\picture")
    if not os.path.exists(BASE_DIR + "\\resources\\report"):
        os.makedirs(BASE_DIR + "\\resources\\report")
        if not os.path.exists(BASE_DIR + "\\resources\\report\\allure_report"):
            os.makedirs(BASE_DIR + "\\resources\\report\\allure_report")
        if not os.path.exists(BASE_DIR + "\\resources\\report\\temp"):
            os.makedirs(BASE_DIR + "\\resources\\report\\temp")


if __name__ == "__main__":
    # 先创建文件夹和文件
    check_dir()

    pytest.main(["-s", "-m login or yun", "-v", SCRIPT_PATH, '--alluredir', TEMP_PATH])
    # pytest.main(["-s", "-m login or yun", "-v", SCRIPT_PATH])
    os.system('allure generate '+TEMP_PATH+' -o '+REPORT_PATH+' --clean')