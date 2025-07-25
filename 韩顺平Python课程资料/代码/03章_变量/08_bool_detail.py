# @Version  : 1.0
# @Author   : 韩顺平

# bool类型的基本使用
num1 = 100
num2 = 200

if num1 < num2:
    print("num1 < num2")

# 表示把 num1 > num2 的结果赋给 result变量
result = num1 > num2
print("result =", result)

# 看看result的数据类型
print("result的类型:", type(result))
print(type(1 > -1))

# 布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时，
# Python 会将 True 视为 1，False 视为 0

b1 = False
b2 = True

print(b1 + 10)  # ? 10
print(b2 + 10)  # ? 11

# 老师说明
# b1 = 0: 表示赋值, 把0赋给b1
# b1 == 0 : 表示判断 b1是否和0相等
if b1 == 0:
    print("OK")

if b2 == 1:
    print("HI")

# 在Python中，非0被视为真值，0值被视为假值

if 0:
    print("哈哈")

if 1.1:
    print("嘻嘻")

if "老韩":
    print("老韩你好~")





