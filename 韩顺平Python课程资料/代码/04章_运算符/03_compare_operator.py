# @Version  : 1.0
# @Author   : 韩顺平

# 讲解比较运算符的使用

a = 9
b = 8
print(a > b)  # T
print(a >= b)  # T
print(a <= b)  # F
print(a < b)  # F
print(a == b)  # F
print(a != b)  # T
# 表示把 a>b比较的结果，赋给flag
flag = a > b  # flag = True
print("flag = ", flag)  # T
print(a is b)  # F
print(a is not b)  # T

str1 = "abc#"
str2 = "abc#"

print("------------------")
print(str1 == str2)  # T
print(str1 is str2)  # T
