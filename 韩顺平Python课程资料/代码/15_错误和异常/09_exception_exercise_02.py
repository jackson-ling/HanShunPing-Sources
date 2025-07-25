# @Version  : 1.0
# @Author   : 韩顺平


def f3():
    print("---f3() start----")
    try:
        print(10 / 0)
    except Exception as e:
        print(f"hi {e}")
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
    1. ---f2() start---
    2. ---f3() start----
    3. hi Zero.....
    4. ---f3() end----
    5. ---f2() end---

"""


def f3():
    print("---f3() start----")
    print(10 / 0)
    print("---f3() end----")


def f2():
    print("---f2() start---")
    try:
        f3()
    except Exception as e:
        print(f"ok {e}")
    print("---f2() end---")


def f1():
    try:
        f2()
    except Exception as e:
        print(f"f1()捕获异常->{e}")


f1()

"""

    1. ---f2() start---
    2. ---f3() start----
    3. ok Zero....
    4. ---f2() end---

"""


def f3():
    print("---f3() start----")
    print(10 / 0)
    print("---f3() end----")


def f2():
    print("---f2() start---")
    f3()
    print("---f2() end---")


def f1():
    f2()


f1()

"""
    1. ---f2() start---
    2. ---f3() start----
    3. 由系统给出错误提示信息
"""
