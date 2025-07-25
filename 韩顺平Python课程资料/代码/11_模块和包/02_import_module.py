# @Version  : 1.0
# @Author   : 韩顺平


# import 模块名
# import math, random

# import math
# import random

# 得到一个数的绝对值
# print(math.fabs(-11.2))
# 从列表中随机返回一个元素
# print(random.choice(['apple', 'pear', 'banana']))

# 导入模块的指定功能

# from 模块 import 函数、类、变量..
# 解读: 导入math模块的 fabs函数
# from math import fabs

# 返回 x 的绝对值
# print(fabs(-11.2))


# # 导入模块的全部功能
# from math import *
#
# # 返回 x 的绝对值
# print(fabs(-234.5))
# # 返回 x 的平方根
# print(sqrt(9))

# 给导入的模块或者功能取别名

# import 模块 as 别名
import random as r
# from 模块 import 函数、类、变量.. as 别名
from math import fabs as fa

# 使用random的别名 r 来用对应的功能
print(r.choice([100, 200, 600]))
print(fa(-900.2))
