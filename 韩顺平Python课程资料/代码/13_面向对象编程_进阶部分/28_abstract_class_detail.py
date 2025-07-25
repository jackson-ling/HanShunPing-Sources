# @Version  : 1.0
# @Author   : 韩顺平

# 抽象类需要继承ABC, 并且需要至少一个抽象方法

"""
    抽象类使用注意事项和细节
"""

from abc import ABC, abstractmethod


#
#
# class AAA(ABC):
#     name = "tim"
#
#     # @abstractmethod
#     # def f1(self):
#     #     pass
#
#
# # 如果没有一个抽象方法, 能实例化..
# obj1 = AAA()
# print("ok")

# class AAA(ABC):
#     name = "tim"
#
#     @abstractmethod
#     def f1(self):
#         pass
#
#     def hi(self):
#         print("hi()~~")
#
#     def ok(self):
#         pass
#
#
# class BBB(AAA):
#     # 实现父类的f1抽象方法
#     def f1(self):
#         print("BBB-f1()...")
#
#
# obj2 = BBB()
# obj2.f1()
# obj2.hi()
# obj2.ok()
# print("~~~")

# 如果一个类继承了抽象类，则它必须实现抽象类的所有抽象方法，否则它仍然是一个抽象类


class AAA(ABC):
    name = "tim"

    @abstractmethod
    def f1(self):
        pass

    @abstractmethod
    def f2(self):
        pass

    def hi(self):
        print("hi()~~")

    def ok(self):
        pass


class BBB(AAA):
    # 实现父类的f1抽象方法
    def f1(self):
        print("BBB-f1()...")
    # 如果没有完全实现AAA的抽象方法
    # 会报错: Can't instantiate abstract class BBB with abstract method f2
    def f2(self):
        print("BBB-f2()...")


obj2 = BBB() #?
obj2.f1()
obj2.hi()
obj2.ok()
print("~~~")
