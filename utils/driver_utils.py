# -*- coding:utf-8 -*-
from base.config import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random, os


# 工具类
class DriverUtils:
    __driver = None

    @classmethod
    def get_driver(cls, browser='chrome'):
        """ 获取浏览器驱动 """
        if cls.__driver is None:
            if RUN_ENV == 'docker':
                if browser == 'chrome':
                    cls.__driver = webdriver.Remote(RUN_DOCKER_URL, desired_capabilities=DesiredCapabilities.CHROME)
                elif browser == 'firefox':
                    cls.__driver = webdriver.Remote(RUN_DOCKER_URL, desired_capabilities=DesiredCapabilities.FIREFOX)
            else:
                cls.__driver = webdriver.Chrome(options=CHROME_OPTIONS)
            cls.__driver.get(URL + "/elib/#/login")
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(5)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        """ 关闭浏览器驱动 """
        cls.__driver.quit()
        cls.__driver = None

    @classmethod
    def back_option(cls):
        """ 返回【我的首页】，刷新页面 """
        cls.__driver.find_element_by_xpath("//div[@class='el-scrollbar__view']/span[1]").click()
        cls.__driver.refresh()
        TimeUtils().sleep(1)

    @classmethod
    def ramdon_val(cls):
        return ''.join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789', 6))

    # @classmethod
    # def check_dir(cls):
    #     if not os.path.exists(BASE_DIR + "\\resources\\log"):
    #         os.mkdir(BASE_DIR + "\\resources\\log")
    #         file = open(BASE_DIR + "\\resources\\log\\selenium.log", 'w')
    #         file.close()
    #     if not os.path.exists(BASE_DIR + "\\resources\\picture"):
    #         os.mkdir(BASE_DIR + "\\resources\\picture")
    #     if not os.path.exists(BASE_DIR + "\\resources\\report"):
    #         os.mkdir(BASE_DIR + "\\resources\\report")
    #         if not os.path.exists(BASE_DIR + "\\resources\\report\\allure_report"):
    #             os.mkdir(BASE_DIR + "\\resources\\report\\allure_report")
    #         if not os.path.exists(BASE_DIR + "\\resources\\report\\temp"):
    #             os.mkdir(BASE_DIR + "\\resources\\report\\temp")