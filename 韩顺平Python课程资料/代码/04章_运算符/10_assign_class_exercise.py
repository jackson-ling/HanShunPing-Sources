# @Version  : 1.0
# @Author   : 韩顺平

# 有两个变量, a和b, 要求将其进行交换, 动动脑筋, 要求不使用前面老师讲过两种方式完成
"""
    老师分析
    1. a, b 记录值
    2. 需要小伙伴动动脑筋
    a = 1, b = 2
    a = a + b
    b = a - b
    a = a - b
"""
a = 1
b = 2
print(f"交换前a = {a} b = {b}")
a = a + b
b = a - b
a = a - b
print(f"交换后a = {a} b = {b}")
