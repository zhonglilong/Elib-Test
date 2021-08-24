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

    # 查找单个元素
    def find_el(self, feature):
        by, value = feature
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, value)))
        except (NoSuchElementException, TimeoutException):
            logging.error("No Such Element：" + value)

    # 查找多个元素
    def find_els(self, feature):
        by, value = feature
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located((by, value)))
        except (NoSuchElementException, TimeoutException):
            logging.error("No Such Elements：" + value)

    # 点击
    def click(self, feature):
        return self.find_el(feature).click()

    # 输入
    def input(self, feature, content):
        """ 先双击选中数据，再输入
        :param feature: 元祖，包含 By.XPATH 和 定位路径
        :param content: 输入的值
        :return:
        """
        ele = self.find_el(feature)
        self.chains().double_click(ele).perform()
        return ele.send_keys(content)

    # 清除
    def clear(self, feature):
        return self.find_el(feature).clear()

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
