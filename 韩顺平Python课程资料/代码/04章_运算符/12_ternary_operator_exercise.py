# @Version  : 1.0
# @Author   : 韩顺平


# 请使用前面讲的 if-else方式, 得到3个数的最大值 [代码: ternary_operator_exercise.py]
# 老韩提醒: 看课程小伙伴，暂停，先自己做，再听老师评讲

"""
    思路分析
    1. a, b, c三个数
    2. 先求出 a , b 的最大值 max1
    3. 再求出 max1 和 c的最大值max2
"""

# 1. a, b, c三个数
a = 30
b = 50
c = 53
# 2. 先求出 a , b 的最大值 max1
max1 = a if a > b else b
# 3. 再求出 max1 和 c的最大值
max2 = max1 if max1 > c else c
print("max2=", max2)

# 我们还可以使用一条语句完成, 即可以支持嵌套使用,可读性差, 小伙伴知道可以这样使用即可
# 不推荐..
max = (a if a > b else b) if (a if a > b else b) > c else c
print("max=", max)
