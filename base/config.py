# -*- coding:utf-8 -*-
import os
from utils.time_utils import TimeUtils
from selenium import webdriver

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'resources\\log')

# 页面元素目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'page\\page_element')

# 测试文件目录
SCRIPT_PATH = os.path.join(BASE_DIR, 'scripts')

# 测试报告目录
TEMP_PATH = os.path.join(BASE_DIR, 'resources\\report\\temp')
REPORT_PATH = os.path.join(BASE_DIR, 'resources\\report\\allure_report')

# 图片目录
IMAGE_PATH = os.path.join(BASE_DIR, 'resources\\picture')

# 业务系统地址
URL = 'http://192.168.1.35:8080/elib/#/login'    # 业务系统环境

# 运行环境
# 只有docker和local两种
RUN_ENV = 'local'
RUN_DOCKER_URL = 'http://127.0.0.1:5555/wd/hub'  # 这个是本地运行docker

# 测试账号
# USERNAME = 'zll'
# PASSWORD = 'Td123456'
# VERIFY = 'zll'
USERNAME = 'lxh'
PASSWORD = 'Td123456'
VERIFY = '小黑'


# Chrome 设置
CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_argument('disable-infobars')
# CHROME_OPTIONS.add_argument("headless")
CHROME_OPTIONS.add_argument('profile.managed_default_content_settings.images')
CHROME_OPTIONS.add_argument('lang=zh_CN.UTF-8')
CHROME_OPTIONS.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"')

if __name__ == '__main__':
    print(SCRIPT_PATH)