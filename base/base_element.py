# -*- coding:utf-8 -*-
import os
import yaml
from base.config import ELEMENT_PATH


class Element:
    """获取元素"""

    def __init__(self, name, ytype="dict"):
        self.t = ytype
        self.element_path = os.path.join(ELEMENT_PATH, '%s.yaml' % name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        if self.t == 'dict':
            return find_dict_value(self.data, item)
        elif self.t == 'json':
            return find_json_value(self.data, item)


def find_dict_value(dict_data, item):
    """ 解析yaml文件的数据，使用递归循环 """
    if isinstance(dict_data, dict):
        for x in range(len(dict_data)):
            key = list(dict_data.keys())[x]
            value = dict_data[key]
            if isinstance(value, list):
                for y in value:
                    for k, v in y.items():
                        if k == item:
                            return v
            if isinstance(value, dict):
                # 如果直接return find_dict_value(value, item)，第一次循环"征订目录预订"后找不到就直接retuen None，后边的就不会继续循环
                if find_dict_value(value, item) is not None:
                    return find_dict_value(value, item)


def find_json_value(dict_data, item):
    return dict_data[item]


if __name__ == '__main__':
    search = Element('base')
    print(search['筛选项'])
    m = Element("model", ytype='json')
    print(m["marc"])
    print(m["marcSearch-1"])