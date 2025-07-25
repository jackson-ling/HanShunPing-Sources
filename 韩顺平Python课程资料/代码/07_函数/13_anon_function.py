# @Version  : 1.0
# @Author   : 韩顺平

# 编写一个函数, 可以接收一个匿名函数和两个数, 通过匿名函数计算,
# 返回两个数的最大值

def f1(fun, num1, num2):
    """
    功能: 调用fun返回num1和num2的最大值
    :param fun: 接收函数(匿名的)
    :param num1:
    :param num2:
    :return:
    """
    print(f"fun类型: {type(fun)}")  # function
    return fun(num1, num2)


# 关键是看如何传入匿名函数调用

"""
    1. lambda a, b: a if a > b else b 就是匿名函数
    2. 不需要 return, 运算结果就是返回值
"""

max_val = f1(lambda a, b: a if a > b else b, 12, 10)
print("max_val =", max_val)
