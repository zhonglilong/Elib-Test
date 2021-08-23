# -*- coding:utf-8 -*-
import pytest
from base.config import *

if __name__ == "__main__":
    pytest.main([SCRIPT_PATH, '--alluredir', TEMP_PATH])
    os.system('allure generate '+TEMP_PATH+' -o '+REPORT_PATH+' --clean')
    print("test")
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