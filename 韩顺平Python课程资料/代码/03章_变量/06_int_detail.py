# @Version  : 1.0
# @Author   : 韩顺平
import sys

# 讲解int类型的细节
# 在python中,int可以表示很大数
# the limit (4300 digits) for integer
n3 = 9 ** 888
print("n3 =", n3, type(n3))

# python的整数有十进制，十六进制, 八进制，二进制表示
print(10)
# 十六进制
print(0x10)
# 八进制
print(0o10)
# 二进制
print(0b10)

# 字节数随着数字增大而增大

n1 = 0
n2 = 1
n3 = 2
n4 = 2 ** 15
n5 = 2 ** 30
n6 = 2 ** 128
# 在python中, 可以通过sys.getsizeof 返回对象(数据)的大小(按照字节单位返回)

print(n1, sys.getsizeof((n1)), "类型", type(n1))
print(n2, sys.getsizeof((n2)), "类型", type(n2))
print(n3, sys.getsizeof((n3)), "类型", type(n3))
print(n4, sys.getsizeof((n4)), "类型", type(n4))
print(n5, sys.getsizeof((n5)), "类型", type(n5))
print(n6, sys.getsizeof((n6)), "类型", type(n6))
print(sys.getsizeof(10))  # 28字节

print(sys.getsizeof(3))



