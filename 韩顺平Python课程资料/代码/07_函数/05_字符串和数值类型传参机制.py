# @Version  : 1.0
# @Author   : 韩顺平

"""
    字符串和数值类型传参机制
"""


# 定义函数f1
def f1(a):
    print(f"f1() a的值: {a} 地址是: {id(a)}")
    a += 1
    print(f"f1() a的值: {a} 地址是: {id(a)}")


# 定义变量a = 10
a = 10
print(f"调用f1()前 a的值: {a} 地址是: {id(a)}")
# 调用f1(a)
f1(a)
print(f"调用f1()后 a的值: {a} 地址是: {id(a)}")


# 定义函数f2
def f2(name):
    print(f"f2() name的值: {name} 地址是: {id(name)}")
    name += " hi"
    print(f"f2() name的值: {name} 地址是: {id(name)}")


# 输出一个分隔符，方便观察
print("--------------------")
name = "tom"
print(f"调用f2()前 name的值: {name} 地址是: {id(name)}")
f2(name)
print(f"调用f2()后 name的值: {name} 地址是: {id(name)}")
