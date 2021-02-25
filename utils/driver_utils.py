import time
from base.config import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 工具类
class DriverUtils:
    __driver = None

    # 获取浏览器驱动
    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            # logging.info("creat chrome driver")
            if RUN_ENV == 'docker':
                cls.__driver = webdriver.Remote(RUN_DOCKER_URL, desired_capabilities=DesiredCapabilities.CHROME)
            else:
                cls.__driver = webdriver.Chrome(options=CHROME_OPTIONS)
            cls.__driver.get(URL)
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(5)
        else:
            pass
            # logging.info("use existed chrome driver")
        return cls.__driver

    # 关闭浏览器驱动
    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None:
            # logging.info("quit chrome driver")
            cls.__driver.quit()
            cls.__driver = None
        else:
            # logging.info("chrome driver is still alive")
            pass

    @classmethod
    def back_ops(cls):
        cls.__driver.find_element_by_xpath("//div[@class='el-scrollbar__view']/span[1]").click()
        cls.__driver.refresh()
        time.sleep(1)
