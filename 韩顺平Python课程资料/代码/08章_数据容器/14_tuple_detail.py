# @Version  : 1.0
# @Author   : 韩顺平

"""
元组使用注意事项和细节
"""
# 1.如果我们需要一个空元组, 可以通过 (), 或者 tuple() 方式来定义
# tuple_a = ()
# tuple_b = tuple()
# print(f"tuple_a 内容是{tuple_a} 类型是{type(tuple_a)}")
# print(f"tuple_b 内容是{tuple_b} 类型是{type(tuple_b)}")

# 2、元组的数据项可以有多个, 而且数据类型没有限制

# tuple_c = (100, "jack", 4.5, True, "jack")
# print(tuple_c)  # (100, "jack", 4.5, True, "jack")

# 嵌套元组
# tuple_d = (100, "tom", ("天龙八部", "笑傲江湖", 300))
# print("tuple_d=", tuple_d)  # (100, "tom", ("天龙八部", "笑傲江湖", 300))


# 元组索引必须在指定范围内使用，否则报：IndexError: list index out of range,
# 比如 tuple_d = (1, 2.1, '韩顺平教育') 有效下标为 0-2

# tuple_d = (1, 2.1, '韩顺平教育')
# 索引越界
# print(tuple_d[3])

# 元组的元素是不能修改,
# 会报错 TypeError: 'tuple' object does not support item assignment
# tuple_e = (1, 2.1, '韩顺平教育')
# tuple_e[2] = 'python'  # 不能修改


# 6、可以修改元组内 list的内容(包括 修改、增加、删除等)
# tuple_f = (1, 2.1, '韩顺平教育', ["jack", "tom", "mary"])
# # 访问元组中list及其元素
# print(tuple_f[3])  # ["jack", "tom", "mary"]
# print(tuple_f[3][0])  # jack
# # 修改
# tuple_f[3][0] = "HSP"
# print(f"tuple_f 内容是 {tuple_f}")  # (1, 2.1, '韩顺平教育', ["HSP", "tom", "mary"])
# # tuple_f[3] = [10,20] #不能替换整个列表元素
#
# # 删除
# del tuple_f[3][0]
# print(f"tuple_f 内容是 {tuple_f}")  # (1, 2.1, '韩顺平教育', ["tom", "mary"])
#
# # 增加
# tuple_f[3].append("smith")
# print(f"tuple_f 内容是 {tuple_f}")  # (1, 2.1, '韩顺平教育', ["tom", "mary","smith"])


# 7、索引也可以从尾部开始，最后一个元素的索引为 -1, 往前一位为 -2, 以此类推

# tuple_g = (1, 2.1, '韩顺平教育', ["jack", "tom", "mary"])
# print(tuple_g[-2])  # '韩顺平教育'

# 8、定义只有一个元素的元组, 需要带上逗号
tuple_h = (100,)
print(f"tuple_h的类型是{type(tuple_h)}")
