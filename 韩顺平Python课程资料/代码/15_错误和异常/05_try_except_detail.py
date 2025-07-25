# @Version  : 1.0
# @Author   : 韩顺平


# 1、如果异常发生了，则异常发生后面的代码不会执行，直接进入到except子句

# num1 = 10
# num2 = 0
# try:
#     res = num1 / num2  # Zero...
#     print("hi...")
# except Exception as e:
#     print(f"出现了异常 异常信息->{e}")
#
# print("继续执行...")

# 2、如果异常没有发生，则顺序执行try的代码块，不会进入到except子句

# num1 = 10
# num2 = 2
# try:
#     res = num1 / num2
#     print("hi...")
# except Exception as e:
#     print(f"出现了异常 异常信息->{e}")
#
# print("继续执行...")


# 3、如果希望没有发生异常, 要执行某段代码, 则使用else子句

# num1 = 10
# num2 = 2
# try:
#     res = num1 / num2
#     print("hi...")
# except Exception as e:
#     print(f"出现了异常 异常信息->{e}")
# else:
#     # 如果try子句没有发生异常,则执行else子句
#     print("执行了else...")
#
# print("继续执行...")


# 4、如果希望不管是否发生异常，
# 都执行某段代码(比如关闭连接，释放资源等)则使用finally子句

# num1 = 10
# num2 = 1
# try:
#     res = num1 / num2
#     print("hi...")
# except Exception as e:
#     print(f"出现了异常 异常信息->{e}")
# else:
#     print("执行了else...")
# finally:
#     print("执行了 finally~~~~")
#
# print("继续执行...")
#
# """
#     分析输出
#     1. hi...
#     2. 执行了else...
#     3. 执行了 finally~~~~
#     4. 继续执行...
# """

# 5、可以有多个except子句，捕获不同的异常(进行不同的业务处理)，
# 如果发生异常，只会匹配一个except, 建议把具体的异常写在前面,
# 基类异常在后比如(IndexError 在前, Exception 在后), 这样当具体异常匹配不到时,
# 再由基类异常匹配

# num1 = 10
# num2 = 0
# try:
#     res = num1 / num2  # 异常Zero...
#     str_a = "hello"
#     print(str_a[20]) # 异常IndexError
#     open("d:/temp/temp/temp.txt", "r", encoding="utf-8") # 异常FileNotFoundError
#     print("hi...")
#
# except IndexError as e:
#     print(f"出现了异常IndexError 异常信息->{e}")
# except ZeroDivisionError as e:
#     print(f"出现了异常ZeroDivisionError 异常信息->{e}")
# except Exception as e:
#     print(f"出现了异常Exception 异常信息->{e}")
# finally:
#     print("执行了 finally~~~~")
#
# print("继续执行...")


# 6、一个except子句, 也可以捕获不同的异常
num1 = 10
num2 = 0
try:
    # res = num1 / num2 # Zero...
    # str_a = "hello"
    # print(str_a[20])  # IndexError
    open("d:/temp/temp/temp.txt", "r", encoding="utf-8")
    print("hi...")
except (IndexError, ZeroDivisionError, NameError) as e:
    print(f"捕获多种异常 信息->{e} 类型{type(e)}")
finally:
    print("执行了 finally~~~~")

print("继续执行...")
