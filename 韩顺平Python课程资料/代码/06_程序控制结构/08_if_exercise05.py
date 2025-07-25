# @Version  : 1.0
# @Author   : 韩顺平


# 判断一个年份是否是闰年，闰年的条件是符合下面二者之一：
# (1)年份能被4整除，但不能被100整除  (2)能被400整除

"""
    思路分析
    1. 定义一个year 保存年份
    2. 判断 (year % 4 == 0 and year % 100 !=0) or year % 400 == 0 是否成立
    3. 如果成立就是闰年，否则就不是闰年 if-else
"""
year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")
