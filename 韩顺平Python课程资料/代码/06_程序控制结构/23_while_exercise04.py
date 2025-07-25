# @Version  : 1.0
# @Author   : 韩顺平

# 打印1~100之间所有是9的倍数的整数，统计个数  及 总和

"""
    思路分析
    1. 定义i = 1 max_num = 100, 表示我们要遍历的范围
    2. 如果 i % 9 == 0 则说明 i 是9的倍数
    3. 定义count 来统计个数 count += 1 定义sum 来累加 总和 sum += i
"""

i = 1
max_num = 100
# 定义count 来统计个数
count = 0
# 定义sum 来累加 总和
sum = 0
# 遍历 1- 100
while i <= max_num:
    if i % 9 == 0:  # 说明 i 是9的倍数
        # 输出i
        print(i)
        count += 1
        sum += i
    i += 1

print(f"count = {count} sum = {sum}")
