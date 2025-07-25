# @Version  : 1.0
# @Author   : 韩顺平

# 细节的案例
# 示例：
a = 1
b = 99

print(a and b)  # 99
# 在python() 括起来的运算优先级最高
print((a > b) and b)  # F
print((a < b) and b)  # 99
