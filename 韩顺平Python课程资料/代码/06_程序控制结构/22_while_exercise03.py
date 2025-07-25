# @Version  : 1.0
# @Author   : 韩顺平

# 不断输入姓名，直到输入 "exit" 为止

"""
    思路分析:
    1. 定义变量 name 接收用户输入
    2. 使用while判断, 如果 name != "exit" 就循环的输入即可
"""
name = input("请输入名字: ")
while name != "exit":
    name = input("请输入名字: ")
    print("输入的内容是: ", name)
