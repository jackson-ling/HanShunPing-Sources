# @Version  : 1.0
# @Author   : 韩顺平
from abc import ABC, abstractmethod


# 1) 编写一个Employee类，做成抽象基类, 包含如下三个属性：name，id，salary,
# 提供必要的构造器和抽象方法：work()
# 2) 对于Manager类来说，他既是员工，还具有奖金(bonus)的属性,
# 请使用继承的思想, 设计CommonEmployee类和Manager类，要求实现work(),
# 提示 "经理/普通员工 名字 工作中...."
# OOP继承 + 抽象类 3min

# 父类-抽象类
class Employee(ABC):
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


# 子类 CommonEmployee
class CommonEmployee(Employee):
    def work(self):
        print(f"普通员工 {self.name} 工作中....")


class Manager(Employee):

    def __init__(self, name, id, salary, bonus):
        super().__init__(name, id, salary)
        self.bonus = bonus

    def work(self):
        print(f"经理 {self.name} 工作中....")


# 测试
manager = Manager("king", "1-111", 10000, 100000)
manager.work()

commonEmployee = CommonEmployee("tim", "1-222", 5000)
commonEmployee.work()
