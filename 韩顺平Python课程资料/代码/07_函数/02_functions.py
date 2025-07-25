# # @Version  : 1.0
# # @Author   : 韩顺平
#
# # 1、自定义cry 函数, 输出 "小猫, 喵喵叫..."
# """
#     思路分析
#     1. 函数名: cry
#     2. 形参列表: 无 ()
#     3. 函数体: 完成 输出 "小猫, 喵喵叫..."
# """
#
#
# # 定义函数
# def cry():
#     print("小猫, 喵喵叫...")
#
#
# # 调用函数
# """
#     1.cry()就是调用函数
# """
# cry()

# 2、自定义cal01函数, 可以计算从 1+..+1000的结果

# """
#     思路分析:
#     1. 函数名: cal01
#     2. 形参列表： 无()
#     3. 函数体：完成 可以计算从 1+..+1000的结果
# """
#
#
# # 定义函数
# def cal01():
#     total = 0
#     # 函数体
#     for i in range(1, 1001):
#         total += i
#     print("total =", total)
#
#
# # 调用函数cal01()
# cal01()

# 3、自定义cal02函数,该函数可以接收一个数n, 计算从 1+..+n 的结果
# """
#     思路分析：
#     1. 函数名: cal02
#     2. 形参列表： (n)
#     3. 函数体: 完成 计算从 1+..+n 的结果
# """
#
#
# # 定义函数
# def cal02(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     print("total =", total)
# # 调用
# """
#     老师解读
#     1. cal02(10)调用函数 cal02
#     2. (10) 表示我调用函数时，传入了实参 10 即把 10赋给了形参n :n=10
# """
# cal02(10)

# 自定义get_sum函数, 可以计算两个数的和, 并返回结果
# """
#     思路分析:
#     1.函数名: get_sum
#     2.形参列表: (num1,num2)
#     3. 函数体： 完成 可以计算两个数的和, 并返回结果
# """
#
#
# 定义函数
def get_sum(num1, num2):
    # total = num1 + num2
    # return total
    return num1 + num2

# 调用
"""
    1. get_sum(10, 50)调用get_sum
    2. (10,50) 表示传入了两个实参 10,50, 把10赋给num1,把50赋给了num2
    3. result 就是接收get_sum() 函数返回的结果
"""
result = get_sum(30, 50)
print("result =", result)


# 使用函数来解决前面的计算问题

def cal04():
    # 接收用户的输入
    n1 = float(input("请输入一个数"))
    n2 = float(input("请输入一个数"))
    oper = input("请输入运算符 +,-,*,/:")
    # 统计结果
    res = 0.0
    # 多分支的判断
    if oper == "+":
        res = n1 + n2
    elif oper == "-":
        res = n1 - n2
    elif oper == "*":
        res = n1 * n2
    elif oper == "/":
        res = n1 / n2
    else:
        print("输入的运算符不对.")

    print(n1, oper, n2, "=", res)


# 使用cal04
cal04()

# 如果还有这样的需求，调用函数cal04即可
cal04()
