# @Version  : 1.0
# @Author   : 韩顺平

# 定义两个变量int类型，判断二者的和，是否能被3又能被5整除，打印提示信息
"""
    思路分析
    1. 定义num1 和 num2 并赋值
    2. 判断 (num1 + num2) % 3 == 0 and (num1 + num2) % 5 == 0 使用双分支if-else
    3. 然后输出结果
"""

num1 = 10
num2 = 5
if (num1 + num2) % 3 == 0 and (num1 + num2) % 5 == 0:
    print(f"{num1 + num2} 可以被3又能被5整除")
else:
    print(f"{num1 + num2} 不满足既可以被3又可以被5整除")
