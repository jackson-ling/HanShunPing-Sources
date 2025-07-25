# @Version  : 1.0
# @Author   : 韩顺平

# 某人有100, 000元, 每经过一次路口，需要交费, 规则如下:
# 当现金 > 50000时, 每次交5 %
# 当现金 <= 50000时, 每次交1000
#
# 编程计算该人可以经过多少次路口, 使用while + break方式 完成

"""
    思路分析
    1. 定义变量money=100000 表示钱的数量
    2. 定义变量count = 0 用来统计经过了多少个路口
    3. 使用while 无限循环, 按照过路口付款的规则来减少money, 直到不够过路口为止, break
    4. 最后输出count即可
"""
# 定义变量money=100000 表示钱的数量
money = 100000
# 定义变量count = 0 用来统计经过了多少个路口
count = 0
while True:
    # 当现金 > 50000时, 每次交5%
    if money > 50000:
        # 累加count
        count += 1
        money -= money * 0.05
    # 当现金 <= 50000 时, 每次交1000
    elif money >= 1000:
        count += 1
        money -= 1000
    else:
        break

print(f"该人可以经过 {count} 次路口, 剩余的钱为 {money}")
