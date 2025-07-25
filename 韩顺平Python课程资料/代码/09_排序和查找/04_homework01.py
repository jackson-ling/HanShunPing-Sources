# @Version  : 1.0
# @Author   : 韩顺平

# 随机生成10个整数(1-100的范围)保存到列表，使用冒泡排序，对其进行从大到小排序 10min


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


# 完成排序
bubble_sort(lst_num)
print("排序后 lst_num", lst_num)
