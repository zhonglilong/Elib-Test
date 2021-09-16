# -*- coding:utf-8 -*-
import random
from base.base_element import Element

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
