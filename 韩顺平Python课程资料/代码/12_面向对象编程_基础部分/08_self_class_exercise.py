# @Version  : 1.0
# @Author   : 韩顺平


# ● 定义Person类
# 1) 里面有name、age属性
# 2) 并提供compare_to比较方法，用于判断是否和另一个人相等
# 3) 名字和年龄都一样，就返回True, 否则返回False

"""
    思路分析
    1. 类名: Person
    2. 属性: name、age
    3. 方法: compare_to(self,other)
    4. 功能: 名字和年龄都一样，就返回True, 否则返回False
"""


class Person:
    name = None
    age = None

    def compare_to(self, other):
        # 名字和年龄都一样，就返回True, 否则返回False
        return self.name == other.name and self.age == other.age


# 测试
p1 = Person()
p1.name = "tim"
p1.age = 31

p2 = Person()
p2.name = "tim"
p2.age = 31

print(p1.compare_to(p2)) #
