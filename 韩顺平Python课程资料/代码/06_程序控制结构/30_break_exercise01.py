# @Version  : 1.0
# @Author   : 韩顺平


# 1-100以内的数求和，求出 当和 第一次大于20的当前控制循环的变量值是多少?
"""
    思路分析
    1. 定义变量sum累加和
    2. for遍历1-100, 当sum > 20时，就退出for -break
    3. 输出当前的控制循环的变量值即可
"""

# 定义变量sum累加和
sum = 0

# 遍历1-100
for i in range(1, 101):
    # 累加
    sum += i
    # 判断
    if sum > 20:
        break

print("i=", i)
