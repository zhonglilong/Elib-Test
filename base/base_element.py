# -*- coding:utf-8 -*-
import os
import yaml
from base.config import ELEMENT_PATH

class Element:
    """获取元素"""

    def __init__(self, name):
        self.file_name = '%s.yaml' % name
        self.element_path = os.path.join(ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        return find_dict_value(self.data, item)


def find_dict_value(dict_data, item):
    """ 解析yaml文件的数据，使用递归循环 """
    if isinstance(dict_data, dict):
        for x in range(len(dict_data)):
            key = list(dict_data.keys())[x]
            value = dict_data[key]
            if isinstance(value, list):
                for y in value:
                    for k, v in y.items():
                        if k == item: return v
            if isinstance(value, dict):
                return find_dict_value(value, item)

if __name__ == '__main__':
    search = Element('base')
    print(search['新增/编辑-输入'])
