# @Version  : 1.0
# @Author   : 韩顺平

# 在初始化对象时, 会自动执行__init__方法

# class Person:
#     # 构造方法/构造器
#     def __init__(self):
#         print("__init__ 执行了")
#
#
# p1 = Person()
# p2 = Person()


class Person:
    name = None
    age = None

    # 构造方法/构造器
    # 构造方法是完成对象的初始化任务
    def __init__(self, name, age):
        print(f"__init__ 执行了 {name} {age}")
        # 老韩解读
        # 1. 把接收到的name和age赋给属性(name,age)
        # 2. self就是你当前创建的对象
        print(f"self id: {id(self)}")
        self.name = name
        self.age = age


# 创建对象
p1 = Person("kobe", 20)
print(f"p1 id: {id(p1)}")
print(f"p1 的信息 {p1.name} {p1.age}")  # kobe 20

p2 = Person("tim", 30)
print(f"p2 id: {id(p2)}")
print(f"p2 的信息 {p2.name} {p2.age}")  # tim 30
