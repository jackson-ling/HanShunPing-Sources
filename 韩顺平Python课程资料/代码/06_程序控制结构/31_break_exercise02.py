# @Version  : 1.0
# @Author   : 韩顺平


# 实现登录验证，有三次机会，如果用户名为 "张无忌" , 密码 "888"
# 提示登录成功, 否则提示还有几次机会，请使用for+break完成

"""
    老韩思路分析:
    1. 实现登录验证, 有3次机会, 我使用for循环3次
    2. 接收用户的输入 (名字name+密码pwd), 如果满足条件，就break
    3. 根据登录的情况，提示成功/还有几次登录机会
"""

# 定义个变量-表示还有几次登录机会
change = 3

# 登录3次
for i in range(1, 4):
    name = input("请输入登录名: ")
    pwd = input("请输入密码: ")
    change -= 1
    # 判断是否成功
    if name == "张无忌" and pwd == "888":
        print("登录成功, 恭喜小伙伴")
        break
    else:
        print(f"你还有 {change} 次登录机会")
