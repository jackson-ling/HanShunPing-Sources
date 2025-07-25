# @Version  : 1.0
# @Author   : 韩顺平


"""
1) 有多个类，完成不同的任务job
2) 要求统计得到各自完成任务的时间
3) 请编程实现  传统方式实现.py
"""
import time


class AA:

    def job(self):
        # 得到开始的时间, 秒数
        start = time.time()
        num = 0
        for i in range(1, 800001):
            num += i
        # 得到结束的时间, 秒数
        end = time.time()
        print("计算任务 执行时间(秒) ", (end - start))


class BB:
    def job(self):
        start = time.time()
        num = 1
        for i in range(1, 90001):
            num -= i
        end = time.time()
        print("计算任务 执行时间 ", (end - start))


# 测试 ， 模板设计模式
if __name__ == '__main__':
    aa = AA()
    aa.job()
    bb = BB()
    bb.job()
