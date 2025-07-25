# @Version  : 1.0
# @Author   : 韩顺平

# isinstance 使用案例

class AA:
    pass


class BB(AA):
    pass


class CC:
    pass


# 创建两个对象
obj = BB()
obj2 = AA()

# 分析输出的结果
print(f"obj 是不是BB的对象 {isinstance(obj, BB)}")  # T
print(f"obj 是不是AA的对象 {isinstance(obj, AA)}")  # T
print(f"obj 是不是CC的对象 {isinstance(obj, CC)}")  # F

num = 9  # int类型
print(f"num 是不是int: {isinstance(num, int)}")  # T
print(f"num 是不是str: {isinstance(num, str)}")  # F
# # 是元组中的一个返回 True
print(f"num 是不是str/int/list: {isinstance(num, (str, int, list))}")  # F
