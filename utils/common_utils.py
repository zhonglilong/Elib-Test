# -*- coding:utf-8 -*-
import logging
import random
import time

from base.base_element import Element
from utils.driver_utils import *

ele = Element('base')


def ramdon_val():
    return ''.join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789', 6))


def check_param(path, param=None):
    """ 用于检查param传过来的值
    :param path: 传递 yaml文件中的 xpath名称
    :param param: 传递 xpath 参数（可以为None，str，list）
    :return:
    """
    if param is not None:
        # 判断传过来的是不是个list
        if isinstance(param, list):
            value = ele[path].format(*param)
        else:
            value = ele[path].format(str(param))
    else:
        value = ele[path]
    return value


def check_download(f, load=1):
    """ 检测是否下载指定文件
    :param f: 文件名（可只输入部分）
    :param load: 等待文件时间
    :return: True 或 False
    """
    try:
        if os.path.exists(FILE_PATH):
            time.sleep(int(load))
            for file in os.listdir(FILE_PATH):
                if f in file:
                    return True
            return False
    except Exception:
        logging.info("file is not exist")
        return False


def clear_download():
    """ 清空文件夹FILE_PATH """
    for file in os.listdir(FILE_PATH):
        if len(file) > 0:
            os.remove(FILE_PATH + "\\" + file)

