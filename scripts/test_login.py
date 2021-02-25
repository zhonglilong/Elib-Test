import pytest
import allure
from page.login_page import LoginPage
from base.config import *
from utils.driver_utils import DriverUtils
from base.logging import logger

# 登录
@allure.feature('登录功能')
class TestLogin:

    @pytest.fixture(scope='function', autouse=True)
    def setup_class(self, drivers):
        self.page = LoginPage(drivers)

    @classmethod
    def teardown_class(cls):
        DriverUtils.back_ops()

    @allure.feature('登录功能')
    @allure.story('登录成功分支')
    @allure.severity('critical')
    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=3)
    def test_login(self):
        """ 登录成功 """
        logger.info("aaaaaaaaaa")
        self.page.input_username(USERNAME)
        self.page.input_password(PASSWORD)
        self.page.click_login_btn()
        self.page.click_bm_btn()
        self.page.click_wxbm_btn()
        self.page.click_bmgl_btn()
        self.page.click_query_btn()
        assert self.page.get_sub_menu_alert()