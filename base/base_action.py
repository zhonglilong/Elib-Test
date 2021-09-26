import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from PIL import Image
from base.config import IMAGE_PATH
from selenium.webdriver.common.keys import Keys
import logging


# 基类
class BaseAction:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5

    def find_el(self, feature):
        """ element 显示等待 查找单个元素
        :param feature:传递元祖 <xpath 和 定位字符>
        :return: element
        """
        by, value = feature
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, value)))
        except (NoSuchElementException, TimeoutException):
            logging.error("No Such Element：" + value)

    def find_els(self, feature):
        """ element 显示等待 查找多个元素
        :param feature:传递元祖 <xpath 和 定位字符>
        :return: elements
        """
        by, value = feature
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located((by, value)))
        except(NoSuchElementException, TimeoutException):
            logging.error("No Such Elements：" + value)

    def click(self, feature):
        return self.find_el(feature).click()

    def clicks(self, feature):
        return self.chains().double_click(self.find_el(feature)).perform()

    def moveclick(self, feature):
        ele = self.find_el(feature)
        return self.chains().move_to_element(
            ele
        ).click(ele).perform()

    def input(self, feature, content):
        ele = self.find_el(feature)
        return ele.send_keys(content)

    def clickinput(self, feature, content):
        ele = self.find_el(feature)
        # send_keys_to_element：可以看看源码，相当于先点击一下element才输入值
        self.chains().send_keys_to_element(ele, content).perform()

    def clickinputs(self, feature, content):
        ele = self.find_el(feature)
        self.chains().double_click(ele).perform()
        return ele.send_keys(content)

    def clearinput(self, feature, content):
        """ 备注：此方法在执行貌似会报错，无法清除文本后再输入，可选择以下方法 clear_all_input """
        ele = self.find_el(feature).clear()
        return ele.send_keys(content)

    def clear_all_input(self, feature, content):
        """通过键盘全选输入框文本"""
        ele = self.find_el(feature)
        ele.send_keys(Keys.CONTROL, 'a')
        return ele.send_keys(content)

    def select(self, feature):
        """ 是否被选中
        :param feature:传递元祖 <xpath 和 定位字符>
        :return:True 或 False
        """
        return self.find_el(feature).is_selected()

    def enable(self, feature):
        """ 是否可用
        :param feature:传递元祖 <xpath 和 定位字符>
        :return:True 或 False
        """
        return self.find_el(feature).is_enabled()

    def display(self, feature):
        """ 是否显示
        :param feature:传递元祖 <xpath 和 定位字符>
        :return:True 或 False
        """
        return self.find_el(feature).is_displayed()

    # 获取页面源代码
    def get_source(self):
        return self.driver.page_source

    # 获取当前组件文本
    def text(self, feature):
        return self.find_el(feature).text

    def attribute(self, feature, label):
        return self.find_el(feature).get_attribute(label)

    # 刷新页面
    def refresh(self):
        self.driver.refresh()

    # 浏览器后退
    def back(self):
        self.driver.back()

    def chains(self):
        return ActionChains(self.driver)

    def screenshot(self, imageName, feature=None):
        self.driver.get_screenshot_as_file(IMAGE_PATH + "\\" + imageName)
        print(feature)
        if feature is not None:
            ele = self.find_el(feature)
            left = ele.location['x']
            right = ele.location['x'] + ele.size['width']
            top = ele.location['y']
            bottom = ele.location['y'] + ele.size['height']
            print(left, top, right, bottom)
            photo = Image.open(IMAGE_PATH + "\\" + imageName)
            photo = photo.crop((left, top, right, bottom))
            photo.save(IMAGE_PATH + "\\getVerify.png")

    def check_element(self, feature, atype="redAlert"):
        """ 判断是否有组件存在，根据atype判断组件类型
        判断是否有提示框，没有错误提示框为True，有错误提示框为False；分为2种情况：
        - 如果找不到提示框，就NoSuchElementException直接返回False
        - 如果找到了提示框，判断是不是错误信息，是的话返回False
        PS：Python的find()方法，找不到返回-1，找到返回下标（int类型）
        """
        by, value = feature
        if atype == "redAlert":
            try:
                element = self.driver.find_element(by, value)
                if str(element.get_attribute('class')).find("el-message--error") == -1:
                    return True
            except NoSuchElementException as e:
                return True
        elif atype == "yellowAlert":
            try:
                element = self.driver.find_element(by, value)
                if str(element.get_attribute('class')).find("el-message--warning") >= 0:
                    return True
            except NoSuchElementException as e:
                return False
        elif atype == "greenAlert":
            try:
                element = self.driver.find_element(by, value)
                if str(element.get_attribute('class')).find("el-message--success") >= 0:
                    return True
            except NoSuchElementException as e:
                return False
        elif atype == "pop":
            try:
                element = self.driver.find_element(by, value)
                if str(element.get_attribute('class')).find("el-message-box") == -1:
                    return False
                else:
                    return True
            except NoSuchElementException as e:
                return False
        elif atype == "dialog":
            try:
                element = self.driver.find_element(by, value)
                if element is not None:
                    return True
            except NoSuchElementException as e:
                return False
        elif atype == "element":
            try:
                self.driver.find_element(by, value)
                return True
            except NoSuchElementException:
                return False
        return False

    # 获取当前组件样式内容
    def element_css_style(self, feature):
        return self.find_el(feature).get_attribute("class")

    def element_sle_style(self, feature):
        return self.find_el(feature).get_attribute("style")

    def element_tle_style(self, feature):
        return self.find_el(feature).get_attribute("title")