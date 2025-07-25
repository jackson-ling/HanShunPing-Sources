# @Version  : 1.0
# @Author   : 韩顺平

# 1、集合是由不重复元素组成的无序容器

# 不重复元素组成, 可以理解成会自动去重
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(f"basket: {basket}")

# 无序, 也就是你定义元素的顺序和取出的顺序不能保证一致,
# 集合底层会按照自己的一套算法来存储和取数据, 所以每次取出顺序是不变的
set_a = {100, 200, 300, 400, 500}
print(f"set_a: {set_a}")
print(f"set_a: {set_a}")
print(f"set_a: {set_a}")
print(f"set_a: {set_a}")
print(f"set_a: {set_a}")
print(f"set_a: {set_a}")

set_a = {100, 200, 300, 400, 500}
# 集合不支持索引 ,会报错
# print(set_a[0])


# 使用for对集合进行遍历
print("-" * 30)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
for ele in basket:
    print(ele)

# 创建空集合只能用 set()，不能用 {}，{} 创建的是空字典，下一小节介绍：字典
set_b = {}  # 上面这样定义空集合不对，他是一个空字典
set_c = set()  # 创建空集合
# {} dict set() set
print(f"set_b: {set_b} 类型: {type(set_b)}  set_c: {set_c} 类型: {type(set_c)}")
