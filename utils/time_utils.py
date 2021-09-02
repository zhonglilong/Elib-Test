# -*- coding:utf-8 -*-
import time


# 时间类
class TimeUtils:

    @classmethod
    def get_stamp(cls):
        """ 返回当前时间的时间戳
        :return: str
        """
        return str(round(time.time() * 1000))

    @classmethod
    def sleep(cls, times=3):
        """ 暂停时间（默认3秒）
        :return: 无返回
        """
        time.sleep(times)

    @classmethod
    def today(cls, istime=False):
        if istime is True:
            return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return time.strftime("%Y-%m-%d", time.localtime())


if __name__ == '__main__':
    print(TimeUtils().today(istime=True))
