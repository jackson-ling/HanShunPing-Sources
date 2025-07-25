# @Version  : 1.0
# @Author   : 韩顺平


# 随机生成10个整数(1-100的范围)保存到列表
import random

lst_num = []
for _ in range(10):
    lst_num.append(random.randint(1, 100))

print("排序前 lst_num", lst_num)


# 使用冒泡排序，对其进行从大到小排序
def bubble_sort(my_list):
    """
    功能: 对传入的列表排序-顺序是从大到小
    :param my_list: 传入的列表
    :return: 无
    """
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]


# 编写二分查找函数
def binary_search(my_list, find_val):
    """
    功能: 完成二分查找
    :param my_list: 要查找的列表(该列表是有大小顺序)
    :param find_val: 要查找的元素/值
    :return: 如果找到返回对应的下标, 如果没有找到,返回-1
    """

    left_index, right_index = 0, len(my_list) - 1
    find_index = -1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if my_list[mid_index] > find_val:
            # 到列表的右边查找
            left_index = mid_index + 1
        elif my_list[mid_index] < find_val:
            # 到列表的左边查找
            right_index = mid_index - 1
        else:
            find_index = mid_index
            break  #

    return find_index


# 完成排序
bubble_sort(lst_num)
print("排序后 lst_num", lst_num)

# 使用二分查找，来查找是否有8这个元素，并返回下标, 没有找到, 返回-1
res_index = binary_search(lst_num, 8)
if res_index == -1:
    print("没有在列表中找到8")
else:
    print(f"在列表中找到8, 对应的下标/索引{res_index}")
