# -*- coding:utf-8 -*-
import pytest
from base.config import *
from utils.driver_utils import *


def check_dir():
    if not os.path.exists(BASE_DIR + "\\resources\\log"):
        os.mkdir(BASE_DIR + "\\resources\\log")
        file = open(BASE_DIR + "\\resources\\log\\selenium.log", 'w')
        file.close()
    if not os.path.exists(BASE_DIR + "\\resources\\picture"):
        os.mkdir(BASE_DIR + "\\resources\\picture")
    if not os.path.exists(BASE_DIR + "\\resources\\report"):
        os.mkdir(BASE_DIR + "\\resources\\report")
        if not os.path.exists(BASE_DIR + "\\resources\\report\\allure_report"):
            os.mkdir(BASE_DIR + "\\resources\\report\\allure_report")
        if not os.path.exists(BASE_DIR + "\\resources\\report\\temp"):
            os.mkdir(BASE_DIR + "\\resources\\report\\temp")


if __name__ == "__main__":
    # 先创建文件夹和文件
    check_dir()

    pytest.main(["-s", "-m login or zhl", "-v", SCRIPT_PATH, '--alluredir', TEMP_PATH])
    os.system('allure generate '+TEMP_PATH+' -o '+REPORT_PATH+' --clean')
    if DING == 'yes':
        """ 推送 dingding 消息 """
        print(DING_MSG["markdown"]["text"])
        # requests.post(
        #     url=WEBHOOK,
        #     params={'access_token': TOKEN, 'timestamp': TimeUtils().get_stamp(), 'sign': hmac_key(SECRCT, SIGN)},
        #     headers={'Content-Type': 'application/json; charset=utf-8'},
        #     json=DING_MSG,
        #     verify=False
        # )