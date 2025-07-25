# @Version  : 1.0
# @Author   : 韩顺平

# 假如还有97天放假, 问：合xx个星期零xx天
'''
    思路分析
    1. 定义变量
    days: 记录总的天数
    week: 记录对应的星期
    left_day: 记录剩余的天数
    2. week: 记录对应的星期 days // 7
    3. left_day: 记录剩余的天数 days % 7
    4. 输出信息
'''

# 定义相关的变量
days = 97
week = days // 7
left_day = days % 7
# 输出
print(f"假如还有{days}天放假, 则：合{week}个星期 零{left_day}天")

# 定义一个变量保存华氏温度，华氏温度转换摄氏温度的公式为: 5/9*(华氏温度-100),
# 请求出华氏温度对应的摄氏温度。[234.5]

"""
    老师的思路:
    1. 定义变量 hua_shi she_shi 
    2. 根据要求直接套用公式即可
    3. 输出结果
"""
hua_shi = 234.5
she_shi = 5 / 9 * (hua_shi - 100)
print(f"华氏温度{hua_shi} 对应的摄氏温度 {she_shi}")
print("华氏温度 %.2f 对应的摄氏温度 %.2f" % (hua_shi, she_shi))


