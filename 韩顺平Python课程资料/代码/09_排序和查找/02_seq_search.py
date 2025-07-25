# @Version  : 1.0
# @Author   : 韩顺平


"""
    顺序查找:
    有一个列表：白眉鹰王、金毛狮王、紫衫龙王、青翼蝠王, 猜名字游戏：
    从键盘中任意输入一个名称，判断列表中是否包含此名称【顺序查找】
    要求: 如果找到了，就提示找到，并给出下标值
"""
# 老韩说明, 如果只是完成查找功能, 我们可以直接使用list的方法index, 如下

names_list = ["白眉鹰王", "金毛狮王", "紫衫龙王", "青翼蝠王"]
find_name = "金毛狮王"


# 使用list.index完成查找
# res_index = names_list.index(find_name)
# print("res_index:", res_index)  # 1


# 除了掌握系统提供的index(), 程序员也应当掌握一些基本的查找方法
# (以后遇到不同业务, 需要定制查找, 也能处理)


# 编写顺序查找函数seq_search
def seq_search(my_list, find_val):
    """
    功能: 顺序查找指定的元素
    :param my_list: 传入的列表(即要查找的列表)
    :param find_val: 要查找的值/元素
    :return: 如果查找到则返回对应的索引下标, 否则返回-1
    """
    """
        思路分析
        1. 对列表进行遍历, 如果找到了, 则返回对应的下标
        2. 如果遍历结束, 没有找到, 则返回-1
    """
    find_index = -1
    # 遍历
    for i in range(len(my_list)):
        # 开始比较, 如果当前的元素就是要查找的值,则返回索引
        if my_list[i] == find_val:
            print(f"恭喜, 找到对应的值{find_val} 下标是{i}")
            find_index = i
            break  # 退出for
    else:
        print(f"没有找到对应的值 {find_val}")

    return find_index


# 测试
res_index = seq_search(names_list, find_name)
print("res_index:", res_index)

# 如果一个列表中有多个要查找的元素/值, 比如前面的列表有两个 金毛狮王,
# 请思考, 怎样才能把满足查询条件的元素的下标，都返回.

"""
    思路分析
    1. 顺序查找列表,把满足查询条件的元素的下标,都返回
    2. 定义一个空列表, 保存查找到的索引下标, 发现一个就动态的添加的列表
    3. 最后返回列表
"""


# 编写查找函数,把满足查询条件的元素的下标,都返回
def seq_search2(my_list, find_val):
    # 定义一个空列表
    find_index = []
    # 遍历
    for i in range(len(my_list)):
        # 开始比较, 如果当前的元素就是要查找的值就保存到find_index
        if my_list[i] == find_val:
            # 将找到的下标,添加到find_index
            find_index.append(i)

    return find_index


res_index = seq_search2(names_list, find_name)
print("res_index:", res_index)
