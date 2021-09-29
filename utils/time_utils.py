# -*- coding:utf-8 -*-
import time
from datetime import datetime


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
    def current_year(cls):
        """
        获取当前系统年的年份
        :return:
        """
        return datetime.now().year

    @classmethod
    def today(cls, istime=False):
        if istime is True:
            return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return time.strftime("%Y-%m-%d", time.localtime())

    @classmethod
    def long_ago_time(cls, month_num, fulltime=False):
        '''
        获取前N个月前的时间点
        :return:
        '''
        long_ago = time.time() - int(month_num)*60*60*24*30
        if fulltime is True:
            return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(long_ago))
        return time.strftime("%Y-%m-%d", time.localtime(long_ago))

    @classmethod
    def check_time_state(cls, start_time, end_time, target_time, same_time=True):
        '''
        判断获取的数据的第一个时间是否在规定时间区间内
        same_time为True：输入时间区域包含时分秒
        same_time为False：输入时间区域不包含时分秒
        :return:
        '''
        if same_time is True:
            start_time_sec = time.mktime(time.strptime(start_time, "%Y-%m-%d %H:%M:%S"))
            end_time_sec = time.mktime(time.strptime(end_time, "%Y-%m-%d %H:%M:%S"))
            target_time_sec = time.mktime(time.strptime(target_time, "%Y-%m-%d %H:%M:%S"))
            return (start_time_sec <= target_time_sec) and (end_time_sec >= target_time_sec)
        elif same_time is False:
            start_time_sec = time.mktime(time.strptime(start_time, "%Y-%m-%d"))
            end_time_sec = time.mktime(time.strptime(end_time, "%Y-%m-%d"))
            target_time_sec = time.mktime(time.strptime(target_time, "%Y-%m-%d %H:%M:%S"))
            return (start_time_sec <= target_time_sec) and (end_time_sec >= target_time_sec)

if __name__ == '__main__':
    print(TimeUtils().today(istime=True))
