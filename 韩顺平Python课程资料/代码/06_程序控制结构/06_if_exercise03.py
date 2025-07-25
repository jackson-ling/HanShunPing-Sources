# @Version  : 1.0
# @Author   : 韩顺平

# 编写程序，定义2个float型变量并赋值, 如果第一个数大于10.0，
# 且第2个数小于20.0，打印两数之和

"""
    思路分析
    1. 定义变量num1 和 num2 并赋值
    2. 判断 num1 >10.0 and num2 < 20.0 是否成立使用if单分支
    3. 根据判断的结果，输出 num1 + num2
"""
num1 = 11.2
num2 = 5.2
if num1 > 10.0 and num2 < 20.0:
    print(f"{num1} + {num2} = {num1 + num2}")

