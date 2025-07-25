# @Version  : 1.0
# @Author   : 韩顺平
from abc import ABC, abstractmethod


# 我们看看如何把Animal做成抽象类，并让子类Tiger实现

# Animal就是抽象类
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 这时: cry就是一个抽象方法
    @abstractmethod
    def cry(self):
        # """
        # 动物都有叫唤的行为...但是这个行为不明确(即不能明确的实现..)
        # :return:
        # """
        # print("不知道是什么动物, 不知道是什么叫声...")
        pass


# 注意:抽象类(含有抽象方法), 不能实例化
# TypeError: Can't instantiate abstract class Animal
# animal = Animal("动物", 3)


# 编写子类Tiger 继承 Animal 并实现抽象方法
class Tiger(Animal):
    def cry(self):
        print(f"老虎 {self.name} 嗷嗷叫...")


tiger = Tiger("皮皮", 2)
tiger.cry()
