# -*- coding:utf-8 -*-
import os
from utils.time_utils import TimeUtils
from selenium import webdriver

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'resources/log/selenium.log')

# 页面元素目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'page/page_element')

# 测试文件目录
SCRIPT_PATH = os.path.join(BASE_DIR, 'scripts')

# 测试报告目录
TEMP_PATH = os.path.join(BASE_DIR, 'resources/report/temp')
REPORT_PATH = os.path.join(BASE_DIR, 'resources/report/allure_report')


# 业务系统地址
URL = 'http://192.168.1.47:8080/elib/#/login'
# URL = 'https://yun.library3.cn/elib/#/login'


# 运行环境
# 只有docker和local两种
RUN_ENV = 'docker'
RUN_DOCKER_URL = 'http://127.0.0.1:5555/wd/hub'  # 这个是本地运行docker
# RUN_DOCKER_URL = 'http://172.17.0.2:5555/wd/hub'   # 这个是jenkins运行docker


# 是否推送钉钉（yes or no）
# 软件测试组的钉钉推送
DING = "no"
WEBHOOK = "https://oapi.dingtalk.com/robot/send"
SECRCT = "SEC41d0d24f31f5246acb8b3c01183d0c57ff90075cf3440ad0a8470254c7f08e89"
TOKEN = "27eabace414eea411b5741ca286c138e4deb29f3807c8d615180a870c9c48d35"
SIGN = '{}\n{}'.format(TimeUtils().get_stamp(), SECRCT)
DING_MSG = {
    "msgtype": "markdown",
    "markdown": {
        "title": "自动化测试结果",
        "text": " "
    }, "at": {
        "atMobiles": [],
        "isAtAll": False
    }
}


# Chrome 设置
CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_argument('disable-infobars')
# CHROME_OPTIONS.add_argument("headless")
CHROME_OPTIONS.add_argument('profile.managed_default_content_settings.images')
CHROME_OPTIONS.add_argument('lang=zh_CN.UTF-8')
CHROME_OPTIONS.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"')


# 测试账号
USERNAME = 'TJ'
PASSWORD = 'Td123456'
VERIFY = '统计管理员'

if __name__ == '__main__':
    print(ELEMENT_PATH)