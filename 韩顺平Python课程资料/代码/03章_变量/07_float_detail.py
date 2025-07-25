# @Version  : 1.0
# @Author   : 韩顺平

n1 = 4.5
n2 = -3.6
print("n1 =", n1)
print("n2 =", n2)

# 浮点类型的表示形式
n3 = 5.12
n4 = .512
print("n4 =", n4)

# 科学计数法形式:如：5.12e2,  5.12E-2
n5 = 5.12e2  # 5.12乘以10的2次方 512.0
n6 = 5.12E-2  # 5.12除以10的2次方 0.0512
print("n5 =", n5)
print("n6 =", n6)

# 浮点类型计算后, 存在精度的损失, 可以使用 Decimal 类进行精确计算
# 老韩说如何解决
# 1. 为了避免浮点数的精度问题，可以使用Decimal 类进行精确计算
# 2. 如果使用Decimal 类 , 需要导入Decimal 类

# 导入Decimal 类
from decimal import Decimal

# b = 8.1 / 3  # 2.6666666669
b = Decimal("8.1") / Decimal("3") # 2.7
print("b =", b)
