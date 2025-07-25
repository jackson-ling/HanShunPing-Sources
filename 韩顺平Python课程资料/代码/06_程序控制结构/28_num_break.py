# @Version  : 1.0
# @Author   : 韩顺平

# 随机生成 1-100的一个数, 直到生成了97这个数, 看看你一共用了几次
"""
    思路分析
    1. 定义变量count 统计一共用了多少次, count += 1
    2. 使用while true 无限循环生成随机数, 直到生成 97 就退出
    3. 输出count即可
"""
# 导入random模块
import random

# 统计一共用了多少次
count = 0

while True:
    # 生成随机数
    n = random.randint(1, 100)
    # 统计次数
    count += 1
    if n == 97:
        break

print(f"生成97一共用了 {count} 次")
