import pytest
import allure
from page.login.login_page import LoginPage
from base.config import *
from utils.driver_utils import DriverUtils


# 登录
@allure.feature('登录功能')
class TestLogin:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = LoginPage(drivers)

    def teardown(self):
        DriverUtils.back_option()

    @allure.feature('登录功能')
    @allure.story('登录成功分支')
    @allure.severity('critical')
    @allure.testcase("http://192.168.1.35:8080/elib/#/login")
    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.login
    def test_login(self, logger):
        """ 登录成功 """
        self.page.input_username(USERNAME)
        self.page.input_password(PASSWORD)
        self.page.click_login_btn()
        self.page.input_ocr()
        self.page.account_status_of_judge()
        assert self.page.sub_menu_alert()
        assert self.page.verify_name() == VERIFY
