# @Version  : 1.0
# @Author   : 韩顺平

# 编程创建一个Cal计算类，在其中定义2个成员变量表示两个操作数，
# 定义四个方法实现求和、差、乘、商(要求除数为0的话，要提示)
# 并创建对象，分别测试

"""
    思路分析
    1. 类名: Cal
    2. 属性: num1, num2
    3. 构造器/构造方法: __init__(self, num1,num2)
    4. 定义四个方法实现求和 def sum()、差 def minus()、乘 def mul()、商 def div()
    5. 商(要求除数为0的话，要提示)
"""


class Cal:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # 和
    def sum(self):
        return self.num1 + self.num2

    # 差
    def minus(self):
        return self.num1 - self.num2

    # 乘
    def mul(self):
        return self.num1 * self.num2

    # 除
    def div(self):
        # 商(要求除数为0的话，要提示)
        if self.num2 == 0:
            print("num2 不能为0")
            return None
        else:
            return self.num1 / self.num2


# 测试
cal = Cal(2, 0)
print("和=", cal.sum())
print("差=", cal.minus())
print("乘=", cal.mul())
print("除=", cal.div())
