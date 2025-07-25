# @Version  : 1.0
# @Author   : 韩顺平


# 函数
def hi():
    print("hi, python")


# 定义类
class Person:
    name = None
    age = None

    def ok(self):
        pass


# 创建了对象 p 和 p2
p = Person()
p2 = Person()

"""
    老韩解读
    1. 动态的给p对象添加方法m1, 注意只是针对p对象添加方法
    2. m1是你新增加的方法的名称，由程序员指定名字
    3. 即m1方法和函数hi关联起来, 当调用m1方法时，会执行hi函数
"""
p.m1 = hi
# 调用m1(即hi)
p.m1()

# print(type(p.m1), type(hi))  # function
# print(type(p.ok))  # method

# 因为没有动态的给p2添加方法, 会报错
# p2.m1()
