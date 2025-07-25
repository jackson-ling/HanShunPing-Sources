# @Version  : 1.0
# @Author   : 韩顺平


"""
列表使用注意事项和细节
"""


# 1.如果我们需要一个空列表, 可以通过 [], 或者 list() 方式来定义
# list1 = []
# list2 = list()
# print(list1, type(list1))
# print(list2, type(list2))

# 2、列表的数据项可以有多个, 而且数据类型没有限制

# list3 = [100, "jack", 4.5, True, "jack"]
# print(list3)  # [100, "jack", 4.5, True, "jack"]

# 嵌套列表
# list4 = [100, "tom", ["天龙八部", "笑傲江湖", 300]]
# print("list4=", list4)

# 4、列表索标必须在指定范围内使用，否则报：IndexError: list index out of range,
# 比如 list1 = [1, 2.1, '韩顺平教育'] 有效下标为 0-2

# list5 = [1, 2.1, '韩顺平教育']
# 索引越界
# print(list5[3])


# 5. 索引也可以从尾部开始，最后一个元素的索引为 -1, 往前一位为 -2, 以此类推

# list1 = [1, 2.1, '韩顺平教育']
# print(list1[-1])  # '韩顺平教育'
# print(list1[-2])  # 2.1
# 依然不能索引越界
# print(list1[-4])


# 通过 列表[索引]=新值 对数据进行更新, 使用 列表.append(值) 方法来添加元素
# list_a = ["天龙八部", "笑傲江湖"]
# print("list_a: ", list_a)  # ["天龙八部", "笑傲江湖"]
# list_a[0] = "雪山飞狐"
# print("list_a: ", list_a)  # ["雪山飞狐", "笑傲江湖"]
# list_a.append("倚天屠龙")
# print("list_a: ", list_a)  # ["雪山飞狐", "笑傲江湖", "倚天屠龙"]
# del list_a[1]
# print("list_a->", list_a) # ["雪山飞狐", "倚天屠龙"]


# 列表的元素是可以修改的, 修改后, 列表变量指向地址不变, 只是数据内容变化
# list1 = [1, 2.1, '韩顺平教育']
# print(f"list: {list1} 地址: {id(list1)} || {list1[2]} {id(list1[2])} ")
# list1[2] = 'python'  # 可以修改
# print(f"list: {list1} 地址: {id(list1)} || {list1[2]} {id(list1[2])} ")


# 扩展一下, 列表在赋值的特点, 示意图说明
# list1 = [1, 2.1, '韩顺平教育']
# list2 = list1
# list2[0] = 500
# print("list2=", list2)  # 输出?[500, 2.1, '韩顺平教育']
# print("list1=", list1)  # 输出?[500, 2.1, '韩顺平教育']


# 扩展一下, 看看列表在函数传参时的特点, 示意图
def f1(l):
    l[0] = 100
    print("l的id:", id(l))


list10 = [1, 2.1, 200]
print("list10的id:", id(list10))
f1(list10)
print("list10:", list10)  # 输出? [100,2.1,200]
