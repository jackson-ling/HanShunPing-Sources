# @Version  : 1.0
# @Author   : 韩顺平


# 演示元组常用操作
tuple_a = (100, 200, 300, 400, 600, 200)
print("tuple_a 元组元素个数:", len(tuple_a))  # 6
print("tuple_a 元组最大元素:", max(tuple_a))  # 600
print("tuple_a 元组最小元素:", min(tuple_a))  # 100

# tuple.count(obj) ： 统计某个元素在列表中出现的次数
print("100出现次数是:", tuple_a.count(100))  # 1
print("200出现次数是:", tuple_a.count(200))  # 2

# tuple.index(obj)： 从列表中找出某个值第一个匹配项的索引位置
# 如果找不到, 会报错: ValueError: x is not in tuple
print("200第1次出现在元组的索引是: ", tuple_a.index(200))  # 1

print(3000 in tuple_a)  # F
