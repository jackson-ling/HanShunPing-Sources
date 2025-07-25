# @Version  : 1.0
# @Author   : 韩顺平

"""
 思路分析：
 1. 定义一个变量num, 接收用户的输入整数, 定义一个 i = 0
 2. 遍历 0-num, 第一个加数是 0-num 第二个加数是 num-0
 3. 使用while循环完成即可
"""
num = int(input("请输入一个整数: "))
i = 0
# 遍历 0-num
while i <= num:
    print(f"{i} + {num - i} = {num}")
    i += 1

