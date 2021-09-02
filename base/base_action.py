import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from PIL import Image
from base.config import IMAGE_PATH
import logging


# 基类
class BaseAction:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

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
        except (NoSuchElementException, TimeoutException):
            logging.error("No Such Elements：" + value)

    def click(self, feature, ctype):
        """ 点击事件
        :param feature:传递元祖 <xpath 和 定位字符>
        :param ctype:传递字符串，区分点击类型，分为单击（click）和双击（clicks）
        :return: self
        """
        if ctype == "click":
            return self.find_el(feature).click()
        elif ctype == "clicks":
            return self.chains().double_click(
                self.find_el(feature)
            ).perform()
        else:
            logging.error("No Such Click Type：" + ctype)

    # # 双击
    # def clicks(self, feature):
    #     ele = self.find_el(feature)
    #     self.chains().double_click(ele).perform()
    #     return ele

    # # 选项框点击输入
    # def click_input(self, feature, content):
    #     ele = self.find_el(feature)
    #     # send_keys_to_element：可以看看源码，相当于先点击一下element才输入值
    #     self.chains().send_keys_to_element(ele, content).perform()
    #     return self

    # 输入
    def input(self, feature, content, itype):
        """ 输入事件
        :param feature: 传递元祖 <xpath 和 定位字符>
        :param content: 传递字符串，输入的内容
        :param itype: 传递字符串，区分输入类型，分为
            直接输入（input）、单击后输入（clickinput）、双击后输入（clickinputs）、清除后输入（clearinput）
        :return: self
        """
        ele = self.find_el(feature)
        if itype == "input":
            return ele.send_keys(content)
        elif itype == "clickinput":
            # send_keys_to_element：可以看看源码，相当于先点击一下element才输入值
            self.chains().send_keys_to_element(ele, content).perform()
        elif itype == "clickinputs":
            self.chains().double_click(ele).perform()
            return ele.send_keys(content)
        elif itype == "clearinput":
            ele.clear()
            return ele.send_keys(content)
        else:
            logging.error("No Such input Type：" + itype)

    # # 清除
    # def clear(self, feature):
    #     return self.find_el(feature).clear()

    # 获取页面源代码
    def get_source(self):
        return self.driver.page_source

    # 获取当前组件文本
    def text(self, feature):
        return self.find_el(feature).text

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

    def check_element(self, feature, type="alert"):
        """ 判断是否有组件存在，根据type判断组件类型
        判断是否有提示框，没有错误提示框为True，有错误提示框为False；分为2种情况：
        - 如果找不到提示框，就NoSuchElementException直接返回False
        - 如果找到了提示框，判断是不是错误信息，是的话返回False
        PS：Python的find()方法，找不到返回-1，找到返回下标（int类型）
        """
        by, value = feature
        if type == "alert":
            try:
                element = self.driver.find_element(by, value)
                if str(element.get_attribute('class')).find("el-message--error") == -1:
                    return True
            except NoSuchElementException as e:
                return True
        elif type == "button":
            try:
                element = self.driver.find_element(by, value)
                if str(element.get_attribute('class')).find("el-button") == -1:
                    return False
            except NoSuchElementException as e:
                return False
        else:
            try:
                self.driver.find_element(by, value)
                return True
            except NoSuchElementException:
                return False
        return False

    def isElementPop(self, feature):
        """ 判断是否有弹窗，没有弹窗为False，有弹窗为True；分为2种情况：
        - 如果找不到弹窗，就NoSuchElementException直接返回False
        - 如果找到了提示框，返回True
        PS：Python的find()方法，找不到返回-1，找到返回下标（int类型）
        """
        by, value = feature
        try:
            element = self.driver.find_element(by, value)
            if str(element.get_attribute('class')).find("el-message-box") == -1:
                return False
            else:
                return True
        except NoSuchElementException as e:
            return False
