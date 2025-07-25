# @Version  : 1.0
# @Author   : 韩顺平

"""
    二分查找的思路分析
    前提: 该列表是一个排好序的列表(为了分析方便, 就以从小到大的列表为例分析)
    1. 找到列表的中间数 mid_val 和 find_val 比较
    2. 如果mid_val > find_val , 则到 mid_val的左边查找
    3. 如果mid_val < find_val , 则到 mid_val的右边查找
    4. 如果mid_val == find_val , 则到 找到，返回对应的下标即可
    5. 不断的重复 1-4步骤， 这里就是不断的折半, 使用while
    6. 如果while 结束，都没有找到, 说明find_val 没有在列表

"""

# 要查找的列表
num_list = [1, 8, 10, 89, 1000, 1234]
# num_list = [1234, 1000, 89, 10, 8, 1]


# 编写二分查找函数
def binary_search(my_list, find_val):
    """
    功能: 完成二分查找
    :param my_list: 要查找的列表(该列表是有大小顺序)
    :param find_val: 要查找的元素/值
    :return: 如果找到返回对应的下标, 如果没有找到,返回-1
    """
    # left_index: 表示左边的索引
    # right_index: 表示右边的索引
    left_index, right_index = 0, len(my_list) - 1
    # 定义找到数的下标
    find_index = -1
    # 使用while循环,不断的折半比较, 比较的前提是满足 left_index <= right_index
    while left_index <= right_index:
        # 中间数的下标/索引
        mid_index = (left_index + right_index) // 2
        # 2.如果mid_val > find_val, 则到mid_val的左边查找
        if my_list[mid_index] > find_val:
            right_index = mid_index - 1
        # 3.如果mid_val < find_val, 则 mid_val的右边查找
        elif my_list[mid_index] < find_val:
            left_index = mid_index + 1
        else:  # 相等
            find_index = mid_index
            break  # 找到一个就退出while

    return find_index


# 测试
res_index = binary_search(num_list, 1)
if res_index == -1:
    print("没有找到该数")
else:
    print(f"找到数, 对应的下标{res_index}")
