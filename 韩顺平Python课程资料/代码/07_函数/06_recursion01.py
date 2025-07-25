# @Version  : 1.0
# @Author   : 韩顺平

# 当执行test(4), 输出什么? 2min
def test(n):
    if n > 2:
        test(n - 1)
    print("n=", n)


# 调用test(4)
test(4)

# 阶乘, 当执行factorial(4), 返回值是多少?
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return factorial(n - 1) * n


# 执行
# print(factorial(4))
