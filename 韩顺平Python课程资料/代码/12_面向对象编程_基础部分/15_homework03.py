# @Version  : 1.0
# @Author   : 韩顺平

# 定义一个圆类Circle, 定义属性：半径，提供显示圆周长功能的方法， 提供显示圆面积的方法

"""
    思路分析:
    1  类名: Circle
    2. 属性: radius 动态生成
    3. 构造器: __init__(self,radius)
    4. 方法:  len(self) 显示圆周长
    5. 方法: area(self) 显示面积
"""

# 导入math
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def len(self):
        len = 2 * math.pi * self.radius
        print("周长:", len)

    def area(self):
        area = math.pi * self.radius * self.radius
        print("面积:", round(area, 2))  # 113.1


# 测试
circle = Circle(6)
circle.len()  # 周长
circle.area()  # 面积
