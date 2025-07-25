# @Version  : 1.0
# @Author   : 韩顺平


# 演示type()使用

name = "tom"  # 字符串
age = 20  # 整型
score = 90.4  # 浮点型(小数)
gender = "男"  # 字符串
is_pass = True  # bool类型

# 查看变量的类型(本质是查看变量指向的数据的类型)
print(type(name))
print(type(age))
print(type(score))
print(type(gender))
print(type(is_pass))

# type可以直接查看具体的值(字面量)的类型
print(f"hello 的类型是{type("hello")}")
print(f"1.1 的类型是{type(1.1)}")
print(f"30 的类型是{type(30)}")
print(f"True 的类型是{type(True)}")

