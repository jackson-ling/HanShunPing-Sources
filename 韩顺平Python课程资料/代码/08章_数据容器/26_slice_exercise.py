# @Version  : 1.0
# @Author   : 韩顺平

# 1、定义列表 list_name = ["Jack", "Lisa", "Hsp", "Paul", "Smith", "Kobe"]
# - 取出前三个名字
# - 取出后三个名字, 并且保证原来顺序

# 列表定义
list_name = ["Jack", "Lisa", "Hsp", "Paul", "Smith", "Kobe"]

# - 取出前三个名字
# slice_a = list_name[0:3:1]
slice_a = list_name[:3:]

print("取出前三个名字:", slice_a)

# - 取出后三个名字, 并且保证原来顺序
"""
    思路分析：
    1. 使用反向切片
    2. 步长 -1 起始索引 -1 结束索引 -4 
"""
slice_b = list_name[-1:-4:-1]
slice_b.reverse()  # 对元素进行逆序操作
print("取出后三个名字:", slice_b) # ["Paul", "Smith", "Kobe"]
