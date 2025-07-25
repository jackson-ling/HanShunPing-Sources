# @Version  : 1.0
# @Author   : 韩顺平

# @Version  : 1.0
# @Author   : 韩顺平

# n1 = 100
#
#
# def f1():
#     # n1 重新定义了
#     n1 = 200
#     print(n1)
#
#
# f1()
# print(n1)


n1 = 100


def f1():
    # global 关键字标明使用全局变量n1
    global n1
    n1 = 200
    print(n1)  # 200


f1()
print(n1)  # 200
