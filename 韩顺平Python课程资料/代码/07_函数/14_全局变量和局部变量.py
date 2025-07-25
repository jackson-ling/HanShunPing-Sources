# @Version  : 1.0
# @Author   : 韩顺平

# n1 就是全局变量
n1 = 100


# 定义函数
def f1():
    # n2就是局部变量
    n2 = 200
    print(n2)
    # 可以访问全局变量n1
    print(n1)


# 调用
f1()
print(n1)

# 不能访问局部变量n2
# print(n2)
