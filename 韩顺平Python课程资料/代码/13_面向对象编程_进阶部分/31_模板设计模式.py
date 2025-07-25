# @Version  : 1.0
# @Author   : 韩顺平


"""
1) 有多个类，完成不同的任务job
2) 要求统计得到各自完成任务的时间
3) 请编程实现  使用模板设计模式
"""
import time
from abc import ABC, abstractmethod


# 抽象类-模板类
class Template(ABC):
    @abstractmethod
    def job(self):
        pass

    # 统计任务执行的时间
    def cal_time(self):
        # 得到开始的时间, 毫秒
        start = time.time() * 1000
        self.job()
        # 得到结束的时间, 毫秒
        end = time.time() * 1000
        print("计算任务 执行时间(毫秒) ", (end - start))


class AA(Template):

    def job(self):
        num = 0
        for i in range(1, 800001):
            num += i


class BB(Template):
    def job(self):
        num = 1
        for i in range(1, 90001):
            num -= i


# 测试 ， 模板设计模式
if __name__ == '__main__':
    aa = AA()
    aa.cal_time()
    bb = BB()
    bb.cal_time()
