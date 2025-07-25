# @Version  : 1.0
# @Author   : 韩顺平

# 2、出票系统：根据淡旺季的月份和年龄，打印票价 [课后练习]  nested_if_example2.py
# 4-10 旺季：
#   成人(18-60): 60
#   儿童(<18): 半价
#   老人(>60): 1/3
# 淡季：
#   成人: 40
#   其他: 20

"""
    思路分析
    1. 需要定义两个变量 month , age, 接收用户的输入
    2. 淡季和旺季使用 if-else 判断
    3. 如果是旺季，使用多分支进行判断age ,给出相应的价格
    4. 如果是淡季，使用双分支判断age, 给出相应的价格
"""
# 代码实现
month = int(input("请输入月份: "))
age = int(input("请输入年龄: "))

if 4 <= month <= 10:  # 旺季
    if age > 60:
        print("价格为¥20")
    elif age >= 18:
        print("价格为¥60")
    else:
        print("价格为¥30")
else:  # 淡季
    if 18 <= age <= 60:
        print("价格为¥40")
    else:
        print("价格为¥20")
