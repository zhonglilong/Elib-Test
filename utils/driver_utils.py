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
            cls.__driver.implicitly_wait(0.5)
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