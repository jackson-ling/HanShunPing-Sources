# @Version  : 1.0
# @Author   : 韩顺平


# 当我们接收Person年龄时，要求范围在 18 – 120 之间，否则抛出一个自定义异常，
# 并给出提示信息(循环提示,直到输入了正确的年龄)

# 自定义异常-AgeError

class AgeError(Exception):
    pass


while True:
    try:
        age = int(input("请输入年龄(18-120): "))
        # 要求范围在18 – 120之间
        # 老师开发技巧: 可以先写出正确的范围，然后取反
        if not (18 <= age <= 120):
            raise AgeError("年龄需要在18-120之间")
        break
    except ValueError as e:
        print("你输入的不是整数")
    except AgeError as e:
        print(e)

print(f"你输入的age: {age}")
