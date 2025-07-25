# @Version  : 1.0
# @Author   : 韩顺平


def f3():  # f3() 没有捕获处理10/0异常
    print("---f3() start----")
    print(10 / 0)
    print("---f3() end----")


def f2():
    print("---f2() start---")
    f3()
    print("---f2() end---")


def f1():
    try:
        f2()
    except Exception as e:
        print(f"f1()捕获异常->{e}")


f1()

"""
    分析输出
    1. ---f2() start---
    2. ---f3() start----
    3. f1()捕获异常-> Zero...
"""
