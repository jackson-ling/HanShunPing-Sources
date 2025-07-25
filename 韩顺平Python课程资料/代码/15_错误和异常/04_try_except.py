# @Version  : 1.0
# @Author   : 韩顺平


"""
    try:
         可能出现异常的代码
    except [异常 as 别名]:
         发生异常时, 对异常处理的代码
"""
try:
    # num1 = 10
    # num2 = 0
    # res = num1 / num2
    str = "hello"
    print(str[100])  # IndexError
# 处理方式1-最简单的方式
# except:
#     print("出现异常了")
# 处理方式2-获取到异常
# 老师说明:
# 1. 表示要捕获Exception 和它的子类类型异常
# 2. 捕获的异常范围是比较大
# except Exception as e:
#     print(f"捕获到异常,异常的信息是{e} 类型是{type(e)}")
# 处理方式3-指定捕获具体的异常
except ZeroDivisionError as e:
    print(f"捕获到指定异常 ZeroDivisionError")

print("程序继续执行..")


