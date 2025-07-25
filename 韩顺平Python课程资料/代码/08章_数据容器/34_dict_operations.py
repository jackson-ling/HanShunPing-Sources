# @Version  : 1.0
# @Author   : 韩顺平

# 演示字典常用操作

"""
    演示字典的常用操作
    {"one": 1, "two": 2, "three": 3}
"""
# 定义字典
dict_a = {"one": 1, "two": 2, "three": 3}
# 1  len(d): 返回字典 d 中的项数
print(f"dict_a 的元素个数是: {len(dict_a)}")  # 3

# 2  d[key]: 返回 d 中以 key 为键的项。 如果映射中不存在 key 则会引发 KeyError
print("key为three对应的value:", dict_a['three'])  # 3

# 3  d[key] = value: 将 d[key] 设为 value, 如果key已经存在，则是修改value,
# 如果key没有存在，则是增加 key-value, 注意会直接修改原来的字典-示意图
# 修改 需求: 修改 key = 'one' 对应的value为 第一
dict_a['one'] = '第一'
print(f"dict_a: {dict_a}")  # {"one": '第一', "two": 2, "three": 3}

# 添加 需求: 增加 key为'four' value为4
dict_a['four'] = 4
print(f"dict_a: {dict_a}")  # {"one": '第一', "two": 2, "three": 3,"four":4}

# 4  del d[key]: 将 d[key] 从 d 中移除。 如果映射中不存在 key 则会引发 KeyError
# 需求 删除 key为'four'的元素
del dict_a["four"]
print(f"dict_a: {dict_a}")  # {"one": '第一', "two": 2, "three": 3}

# 5  pop(key[, default]) ：
# 如果 key 存在于字典中则将其移除并返回其值，否则返回 default。
# 如果 default 未给出且 key 不存在于字典中，则会引发 KeyError
# 需求: 将 key 为 'one' 的值返回, 并将该元素从字典移除
val = dict_a.pop('one')
print(f"val: {val}")  # '第一'
print(f"dict_a: {dict_a}")  # {"two": 2, "three": 3}

# 6  keys()： 返回字典所有的key
dict_a_keys = dict_a.keys()
print(f"dict_a_keys: {dict_a_keys} 类型 {type(dict_a_keys)}")
for k in dict_a_keys:
    print("k->", k)

# 7  key in d: 如果 d 中存在键 key 则返回 True，否则返回 False
# 需求: 判断 字典中是否有 key 'two'
print("two" in dict_a)  # True

# 8  clear(): 移除字典中的所有元素
# 需求: 将字典清空
dict_a.clear()
print(f"dict_a: {dict_a}")  # {}
