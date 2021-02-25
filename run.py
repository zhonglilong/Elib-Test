import pytest
import os
from base.config import TEMP_PATH, REPORT_PATH, SCRIPT_PATH

if __name__ == "__main__":
    pytest.main([SCRIPT_PATH, '--alluredir', TEMP_PATH])
    os.system('allure generate '+TEMP_PATH+' -o '+REPORT_PATH+' --clean')
