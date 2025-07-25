# @Version  : 1.0
# @Author   : 韩顺平


# 我们看看下面一段代码 (对象传递机制.py)
class Person:
    age = None
    name = None


p1 = Person()
p1.age = 10
p1.name = "小明"
p2 = p1  # 把p1赋给了p2,即: 让p2指向p1
print(p2.age)  # p2.age 是多少? 10
print(f"p1.name地址:{id(p1.name)} p2.name地址:{id(p2.name)}") #地址是相同的


"""
    我们看看下面一段代码, 会输出什么信息: 
"""
a = Person()
a.age = 10
a.name = "jack"
b = a
print(b.name)  # jack
b.age = 200
b = None
print(a.age)  # 200
# print(b.age)  # 报错
